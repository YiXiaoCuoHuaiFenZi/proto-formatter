import os
from proto_formatter import format_file
from helper import read_proto, test_path


def test_format_file_align():
    new_fp = os.path.join(test_path, 'formatted_test_data_2.proto')
    if os.path.exists(new_fp):
        os.remove(new_fp)

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    format_file(original_file_path, new_fp=new_fp)
    expected_text = read_proto('formatted_test_data_1_indents_2_all_top_comments_false_equal_sign_false_flatten_false.proto')
    actual_text = read_proto(new_fp)

    if os.path.exists(new_fp):
        os.remove(new_fp)

    assert expected_text == actual_text
