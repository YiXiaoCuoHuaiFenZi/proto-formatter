import os
from proto_formatter.formatter import Formatter
from proto_formatter.parser import ProtoParser
from helper import read_proto, test_path

original_file_path = os.path.join(test_path, 'test_data_1.proto')


def test_parse_align():
    expected_text = read_proto('formatted_test_data_1.proto')
    parser = ProtoParser()
    protobuf_obj = parser.load(original_file_path)

    actual_text = Formatter().to_string(protobuf_obj)

    assert expected_text == actual_text


def test_parse_align_with_equal_sign():
    expected_text = read_proto('formatted_test_data_1_align_with_equal_sign.proto')
    parser = ProtoParser()
    protobuf_obj = parser.load(original_file_path)

    actual_text = Formatter(equal_sign=True).to_string(protobuf_obj)

    assert expected_text == actual_text


def test_parse_align_with_equal_sign_4_indents():
    expected_text = read_proto('formatted_test_data_1_align_with_equal_sign_4_indents.proto')
    parser = ProtoParser()
    protobuf_obj = parser.load(original_file_path)

    actual_text = Formatter(equal_sign=True, indents=4).to_string(protobuf_obj)

    assert expected_text == actual_text


def test_parse_align_with_4_indents_all_top_comments():
    expected_text = read_proto('formatted_test_data_1_align_with_4_indents_all_top_comments.proto')
    parser = ProtoParser()
    protobuf_obj = parser.load(original_file_path)

    actual_text = Formatter(indents=4, all_top_comments=True).to_string(protobuf_obj)

    assert expected_text == actual_text


def test_parse_align_with_equal_sign_4_indents_all_top_comments():
    expected_text = read_proto('formatted_test_data_1_align_with_equal_sign_4_indents_all_top_comments.proto')
    parser = ProtoParser()
    protobuf_obj = parser.load(original_file_path)

    actual_text = Formatter(equal_sign=True, indents=4, all_top_comments=True).to_string(protobuf_obj)

    assert expected_text == actual_text
