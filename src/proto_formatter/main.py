import os
import sys
import types

from argparse import ArgumentParser

from . import format_file
from .util import to_lines, add_prefix, replace_at_start, print_info, proto_print, read_file


def _get_proto_files(root_path):
    proto_files = []
    for path, sub_dirs, files in os.walk(root_path):
        for name in files:
            if name.endswith('.proto'):
                proto_files.append(os.path.join(path, name))
    return proto_files


def get_option_max_length(parser: ArgumentParser):
    actions = parser._actions
    max_length = 0
    for action in actions:
        for option_string in action.option_strings:
            if max_length < len(option_string):
                max_length = len(option_string)
        if action.choices:
            for parser_name, parser in action.choices.items():
                if max_length < len(parser_name):
                    max_length = len(parser_name)
                for option_string_action in parser._option_string_actions:
                    if max_length < len(option_string_action):
                        max_length = len(option_string_action)

    return max_length


def format_actions(max_length_of_options, actions):
    spaces = 4  # space amount between option and help

    lines = ['general options:']
    for action in actions:
        if action.option_strings:
            fill_spaces_amount = max_length_of_options - len(action.option_strings[0]) + spaces
            line = f"{' ' * 2}{action.option_strings[0]}{' ' * fill_spaces_amount}{action.help}"
            lines.append(line)

    return lines


def format_usage_line(name, description, max_length_of_option_names):
    one_space = ' '
    indents = 2
    space_between_name_description = 8
    help_start_index = max_length_of_option_names + space_between_name_description
    help_text_max_length = 80

    name = f"{one_space * indents}{name}"

    option_lines = to_lines(description, help_text_max_length)
    option_lines = add_prefix(option_lines, one_space * help_start_index)
    option_lines[0] = replace_at_start(option_lines[0], name)
    return option_lines


def make_usage(parser: ArgumentParser):
    commands_lines = []
    option_lines = ["", "general options:"]

    max_length_of_option_names = get_option_max_length(parser)
    actions = parser._actions

    for action in actions:
        for option_string in action.option_strings:
            option_lines.extend(format_usage_line(option_string, action.help, max_length_of_option_names))

        if action.choices:
            for command, sub_parser in action.choices.items():
                commands_lines.extend(format_usage_line(command, sub_parser.description, max_length_of_option_names))
                for action_name, action_value in sub_parser._option_string_actions.items():
                    for option_string in action_value.option_strings:
                        option_lines.extend(
                            format_usage_line(option_string, action_value.help, max_length_of_option_names))
    content = """
{prefix_stars}
*  {description}  *
{suffix_stars}

usage:
  proto_formatter <command> [options]

commands:
"""
    prefix_stars = "*" * (len(parser.description) + 6)
    suffix_stars = prefix_stars
    content = content.format(description=parser.description, prefix_stars=prefix_stars, suffix_stars=suffix_stars)
    content = content + '\n'.join(commands_lines + option_lines)
    return content


def new_format_usage(self):
    formatter = self._get_formatter()
    # usage
    formatter.add_usage(self.usage, self._actions, self._mutually_exclusive_groups)

    lines = formatter.format_help().split('\n')
    lines[0] = ''  # replace the prefix "usage:"
    return '\n'.join(lines)


def new_format_help(self):
    formatter = self._get_formatter()
    # usage
    formatter.add_usage(self.usage, self._actions, self._mutually_exclusive_groups)

    lines = formatter.format_help().split('\n')
    lines[0] = ''  # replace the prefix "usage:"
    return '\n'.join(lines)


def main():
    parser = ArgumentParser(description="Format protobuf file(s) from a specific target.")  # add_help=False,
    sub_parser = parser.add_subparsers(dest='command')
    format_parser = sub_parser.add_parser('format', description='format protobuf files', add_help=False)
    view_parser = sub_parser.add_parser('view', description="view file", add_help=False)
    view_parser.add_argument(
        "--file",
        type=str,
        help="target protobuf file, only used for command 'view'"
    )
    format_parser.add_argument(
        "--files",
        type=str,
        nargs="+",
        help="target protobuf files need to be formatted."
    )
    format_parser.add_argument(
        "--folder",
        type=str,
        default=os.getcwd(),
        help="target directory, default is current directory, all protobuf files under it including all subdirectories will be formatted."
    )
    format_parser.add_argument(
        "--indents",
        type=int,
        help="the number of indented spaces, default is 4",
        default=4
    )
    format_parser.add_argument(
        "--top-comment",
        type=bool,
        default=False,
        help="format all comments as top comments(above the target line), default is False"
    )
    format_parser.add_argument(
        "--align-by-equal-sign",
        type=bool,
        default=True,
        help="align the code by equal sign: True or False, default is True"
    )
    format_parser.add_argument(
        "--flatten",
        type=bool,
        default=False,
        help="flatten nested objects, default is False"
    )
    format_parser.add_argument(
        "--comment-max-length",
        type=int,
        default=999999,
        help="the max length of comment line, default is 999999."
    )
    usage = make_usage(parser)
    parser.usage = usage
    # patch format_help method to use custom usage message
    parser.format_help = types.MethodType(new_format_help, parser)
    # patch format_usage method to use custom usage message
    parser.format_usage = types.MethodType(new_format_usage, parser)
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_usage()
        sys.exit(0)

    if args.command == 'format':
        root_path = os.getcwd()
        if args.files:
            proto_files = [os.path.join(root_path, file) for file in args.files]
        elif args.folder:
            # get all proto files in the specified folder and all sub folders
            proto_files = _get_proto_files(args.folder)
        else:
            # get all proto files in the current folder and all sub folders
            proto_files = _get_proto_files(os.getcwd())

        proto_files = list(set(proto_files))  # remove duplicates
        for fp in proto_files:
            print_info(f"formatting {fp.replace(root_path, '')}")
            format_file(
                fp,
                indents=args.indents,
                top_comment=args.top_comment,
                align_by_equal_sign=args.align_by_equal_sign,
                flatten=args.flatten,
                comment_max_length=args.comment_max_length,
                new_fp=None
            )
        print_info("Done!")

    if args.command == 'view':
        args = parser.parse_args()
        fp = os.path.join(os.getcwd(), args.file)
        proto_print(read_file(fp))
