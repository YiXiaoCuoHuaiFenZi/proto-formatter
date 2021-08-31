import os
from proto_formatter import format_str
from helper import read_proto, read_file, test_path


def test_format_str_1_indents_2_all_top_comments_false_equal_sign_false():
    expected_text = read_proto('formatted_test_data_1_indents_2_all_top_comments_false_equal_sign_false.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, all_top_comments=False, equal_sign=False)

    assert expected_text == actual_text


def test_format_str_1_indents_2_all_top_comments_false_equal_sign_true():
    expected_text = read_proto('formatted_test_data_1_indents_2_all_top_comments_false_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, all_top_comments=False, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_1_indents_4_all_top_comments_false_equal_sign_true():
    expected_text = read_proto('formatted_test_data_1_indents_4_all_top_comments_false_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=False, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_1_indents_4_all_top_comments_true_equal_sign_false():
    expected_text = read_proto('formatted_test_data_1_indents_4_all_top_comments_true_equal_sign_false.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=True, equal_sign=False)

    assert expected_text == actual_text


def test_format_str_1_indents_4_all_top_comments_true_equal_sign_true():
    expected_text = read_proto('formatted_test_data_1_indents_4_all_top_comments_true_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=True, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_2_indents_2_all_top_comments_false_equal_sign_false():
    expected_text = read_proto('formatted_test_data_2_indents_2_all_top_comments_false_equal_sign_false.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, all_top_comments=False, equal_sign=False)

    assert expected_text == actual_text


def test_format_str_2_indents_2_all_top_comments_false_equal_sign_true():
    expected_text = read_proto('formatted_test_data_2_indents_2_all_top_comments_false_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, all_top_comments=False, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_2_indents_4_all_top_comments_false_equal_sign_true():
    expected_text = read_proto('formatted_test_data_2_indents_4_all_top_comments_false_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=False, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_2_indents_4_all_top_comments_true_equal_sign_false():
    expected_text = read_proto('formatted_test_data_2_indents_4_all_top_comments_true_equal_sign_false.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=True, equal_sign=False)

    assert expected_text == actual_text


def test_format_str_2_indents_4_all_top_comments_true_equal_sign_true():
    expected_text = read_proto('formatted_test_data_2_indents_4_all_top_comments_true_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=True, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_3_indents_2_all_top_comments_false_equal_sign_false():
    expected_text = read_proto('formatted_test_data_3_indents_2_all_top_comments_false_equal_sign_false.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, all_top_comments=False, equal_sign=False)

    assert expected_text == actual_text


def test_format_str_3_indents_2_all_top_comments_false_equal_sign_true():
    expected_text = read_proto('formatted_test_data_3_indents_2_all_top_comments_false_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, all_top_comments=False, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_3_indents_4_all_top_comments_false_equal_sign_true():
    expected_text = read_proto('formatted_test_data_3_indents_4_all_top_comments_false_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=False, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_3_indents_4_all_top_comments_true_equal_sign_false():
    expected_text = read_proto('formatted_test_data_3_indents_4_all_top_comments_true_equal_sign_false.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=True, equal_sign=False)

    assert expected_text == actual_text


def test_format_str_3_indents_4_all_top_comments_true_equal_sign_true():
    expected_text = read_proto('formatted_test_data_3_indents_4_all_top_comments_true_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=True, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_4_indents_2_all_top_comments_false_equal_sign_false():
    expected_text = read_proto('formatted_test_data_4_indents_2_all_top_comments_false_equal_sign_false.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, all_top_comments=False, equal_sign=False)

    assert expected_text == actual_text


def test_format_str_4_indents_2_all_top_comments_false_equal_sign_true():
    expected_text = read_proto('formatted_test_data_4_indents_2_all_top_comments_false_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, all_top_comments=False, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_4_indents_4_all_top_comments_false_equal_sign_true():
    expected_text = read_proto('formatted_test_data_4_indents_4_all_top_comments_false_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=False, equal_sign=True)

    assert expected_text == actual_text


def test_format_str_4_indents_4_all_top_comments_true_equal_sign_false():
    expected_text = read_proto('formatted_test_data_4_indents_4_all_top_comments_true_equal_sign_false.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=True, equal_sign=False)

    assert expected_text == actual_text


def test_format_str_4_indents_4_all_top_comments_true_equal_sign_true():
    expected_text = read_proto('formatted_test_data_4_indents_4_all_top_comments_true_equal_sign_true.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, all_top_comments=True, equal_sign=True)

    assert expected_text == actual_text
