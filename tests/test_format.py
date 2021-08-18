import os
from proto_formatter import format_file, format_str
from helper import read_proto, read_file, test_path

original_file_path = os.path.join(test_path, 'test_data_1.proto')
original_file2_path = os.path.join(test_path, 'test_data_2.proto')


def test_format_str_align():
    expected_text = read_proto('formatted_test_data_1.proto')

    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str)

    assert expected_text == actual_text


def test_format_str_align_with_equal_sign():
    expected_text = read_proto('formatted_test_data_1_align_with_equal_sign.proto')

    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_align_with_equal_sign_4_indents():
    expected_text = read_proto('formatted_test_data_1_align_with_equal_sign_4_indents.proto')

    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, equal_sign=True, indents=4)

    assert expected_text == actual_text


def test_format_str_align_with_4_indents_all_top_comments():
    expected_text = read_proto('formatted_test_data_1_align_with_4_indents_all_top_comments.proto')

    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=True)

    assert expected_text == actual_text


def test_format_str_align_with_equal_sign_4_indents_all_top_comments():
    expected_text = read_proto('formatted_test_data_1_align_with_equal_sign_4_indents_all_top_comments.proto')

    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, equal_sign=True, indents=4, all_top_comments=True)

    assert expected_text == actual_text


def test_format_file_align():
    new_fp = os.path.join(test_path, 'formatted_test_data_2.proto')
    if os.path.exists(new_fp):
        os.remove(new_fp)

    format_file(original_file2_path, new_fp=new_fp)
    expected_text = read_proto('formatted_test_data_1.proto')
    actual_text = read_proto(new_fp)

    if os.path.exists(new_fp):
        os.remove(new_fp)

    assert expected_text == actual_text
