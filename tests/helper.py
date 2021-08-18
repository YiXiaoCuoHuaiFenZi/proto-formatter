import os
from proto_formatter.formatter import Formatter
from proto_formatter.parser import ProtoParser

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


def make_test_data():
    c = [
        {
            'file_name': 'formatted_test_data_1.proto',
            'indents': 2,
            'all_top_comments': False,
            'equal_sign': False
        },
        {
            'file_name': 'formatted_test_data_1_align_with_equal_sign.proto',
            'indents': 2,
            'all_top_comments': False,
            'equal_sign': True
        },
        {
            'file_name': 'formatted_test_data_1_align_with_equal_sign_4_indents.proto',
            'indents': 4,
            'all_top_comments': False,
            'equal_sign': True
        },
        {
            'file_name': 'formatted_test_data_1_align_with_4_indents_all_top_comments.proto',
            'indents': 4,
            'all_top_comments': True,
            'equal_sign': False
        },
        {
            'file_name': 'formatted_test_data_1_align_with_equal_sign_4_indents_all_top_comments.proto',
            'indents': 4,
            'all_top_comments': True,
            'equal_sign': True
        }
    ]
    parser = ProtoParser()
    protobuf_obj = parser.load('test_data_1.proto')

    for e in c:
        actual_text = Formatter(indents=e['indents'], all_top_comments=e['all_top_comments'],
                                equal_sign=e['equal_sign']).to_string(protobuf_obj)
        write_file(e['file_name'], actual_text)


if __name__ == '__main__':
    print('create test data files...')
    make_test_data()
