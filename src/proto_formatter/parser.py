from enum import Enum

from proto_formatter.constant import Constant
from proto_formatter.comment import CommentParser
from proto_formatter.detector import Detector
from proto_formatter.enum_parser import EnumParser
# from proto_formatter.formatter import Formatter
from proto_formatter.import_parser import ImportParser
from proto_formatter.message_parser import MessageParser
from proto_formatter.option_parser import OptionParser
from proto_formatter.package_parser import PackageParser
from proto_formatter.proto import ProtoBufStructure
from proto_formatter.service_parser import ServiceParser
from proto_formatter.syntax_parser import SyntaxParser
from proto_formatter.util import remove_prefix, remove_suffix


class ProtoParser(Constant):
    def __init__(self):
        self.protobuf_obj = ProtoBufStructure()

    def read_lines(self, path):
        with open(path) as f:
            content = f.read()
            content = content.strip()
            lines = content.split('\n')
            return lines

    def parse(self, lines):
        keyword, comments = Detector().get_object_type(lines)
        parser = self.get_parser(keyword)
        if parser is None:
            return self.protobuf_obj

        if isinstance(parser, MessageParser):
            parser.parse_and_add(self.protobuf_obj, lines, comments)
        elif isinstance(parser, EnumParser):
            parser.parse_and_add(self.protobuf_obj, lines, comments)
        elif isinstance(parser, ServiceParser):
            parser.parse_and_add(self.protobuf_obj, lines, comments)
        else:
            line = lines.pop(0)
            parser.parse_and_add(self.protobuf_obj, line, comments)

        if len(lines) == 0:
            return self.protobuf_obj

        return self.parse(lines)

    def get_parser(self, keyword):
        if keyword == 'syntax':
            return SyntaxParser()
        elif keyword == 'package':
            return PackageParser()
        elif keyword == 'option':
            return OptionParser()
        elif keyword == 'import':
            return ImportParser()
        elif keyword == 'message':
            return MessageParser()
        elif keyword == 'enum':
            return EnumParser()
        elif keyword == 'service':
            return ServiceParser()
