import os
from copy import deepcopy
from proto_formatter import format_file

test_path = os.path.dirname(os.path.realpath(__file__))


def read_lines(file_path):
    with open(file_path) as f:
        content = f.read()
        content = content.strip()
        lines = content.split('\n')
        return lines


def read_proto(proto_file_name):
    fp = os.path.join(test_path, proto_file_name)
    return read_file(fp)


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def write_file(file_path, content):
    with open(file_path, 'w') as f:
        return f.write(content)


def create_test_case_name(config):
    return f'indents_{config["indents"]}_top_comment_{config["top_comment"]}_align_by_equal_sign_{config["align_by_equal_sign"]}_flatten_{config["flatten"]}_comment_max_length_{config["comment_max_length"]}'.lower()


def create_formatted_file_name(test_file, config):
    part = create_test_case_name(config)
    return f'formatted_{test_file.replace(".proto", "")}_{part}.proto'.lower()


def make_test_data():
    test_files = ['test_data_1.proto', 'test_data_2.proto', 'test_data_3.proto', 'test_data_4.proto']
    configs = [
        {
            'indents': 2,
            'top_comment': False,
            'align_by_equal_sign': False,
            'flatten': False,
            'comment_max_length': None
        },
        {
            'indents': 2,
            'top_comment': False,
            'align_by_equal_sign': True,
            'flatten': True,
            'comment_max_length': None
        },
        {
            'indents': 4,
            'top_comment': False,
            'align_by_equal_sign': True,
            'flatten': False,
            'comment_max_length': None
        },
        {
            'indents': 4,
            'top_comment': True,
            'align_by_equal_sign': False,
            'flatten': False,
            'comment_max_length': None
        },
        {
            'indents': 4,
            'top_comment': True,
            'align_by_equal_sign': True,
            'flatten': False,
            'comment_max_length': None
        },
        {
            'indents': 4,
            'top_comment': True,
            'align_by_equal_sign': True,
            'flatten': True,
            'comment_max_length': None
        },
        {
            'indents': 4,
            'top_comment': True,
            'align_by_equal_sign': True,
            'flatten': True,
            'comment_max_length': 50
        },
        {
            'indents': 4,
            'top_comment': False,
            'align_by_equal_sign': True,
            'flatten': True,
            'comment_max_length': 50
        }
    ]

    test_cases = []
    for test_file in test_files:
        for config in configs:
            formatted_file_name = create_formatted_file_name(test_file, config)
            format_file(
                fp=test_file,
                indents=config['indents'],
                top_comment=config['top_comment'],
                align_by_equal_sign=config['align_by_equal_sign'],
                flatten=config['flatten'],
                comment_max_length=config['comment_max_length'],
                new_fp=formatted_file_name
            )

            c = deepcopy(config)
            c.update({
                'test_case_name': formatted_file_name.replace("formatted_test_data_", "").replace(".proto", ""),
                'original_file': test_file,
                'formatted_file': formatted_file_name
            })
            test_cases.append(c)

    return test_cases


def create_test_cases(test_cases):
    content = """import os
from proto_formatter import format_str
from helper import read_proto, read_file, test_path


"""

    cases = []

    case_template = """def test_format_str_{}():
    expected_text = read_proto('{}')

    original_file_path = os.path.join(test_path, '{}')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents={}, top_comment={}, align_by_equal_sign={}, flatten={}, comment_max_length={})

    assert expected_text == actual_text"""

    for config in test_cases:
        print(f"create test case {config['test_case_name']}")
        case = case_template.format(
            config['test_case_name'],
            config['formatted_file'],
            config['original_file'],
            config['indents'],
            config['top_comment'],
            config['align_by_equal_sign'],
            config['flatten'],
            config['comment_max_length']
        )
        cases.append(case)

    content = content + "\n\n\n".join(cases) + "\n"

    write_file('test_format_str.py', content)


if __name__ == '__main__':
    print('create test data files...')
    test_data = make_test_data()

    print('create test cases...')
    create_test_cases(test_data)
    print('Done')
