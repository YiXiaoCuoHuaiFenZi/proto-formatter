import os
from src.proto_formatter import format_file
from .helper import read_file, test_path


def test_format_file_align():
    new_fp = os.path.join(test_path, 'test_data', 'formatted', 'formatted_test_data_2.proto')
    if os.path.exists(new_fp):
        os.remove(new_fp)

    original_file_path = os.path.join(test_path, 'test_data', 'unformatted', 'test_data_2.proto')
    format_file(original_file_path, new_fp=new_fp)

    expected_text_fp = os.path.join(test_path, 'test_data', 'formatted',
                                    'formatted_test_data_2_indents_2_top_comment_false_align_by_equal_sign_false_flatten_false_comment_max_length_none.proto')
    expected_text = read_file(expected_text_fp)
    actual_text = read_file(new_fp)

    if os.path.exists(new_fp):
        os.remove(new_fp)

    assert expected_text == actual_text
