import os
from proto_formatter import format_str
from helper import read_proto, read_file, test_path


def test_format_str_1_indents_2_top_comment_false_align_by_equal_sign_false_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_1_indents_2_top_comment_false_align_by_equal_sign_false_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, top_comment=False, align_by_equal_sign=False, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_1_indents_2_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_1_indents_2_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, top_comment=False, align_by_equal_sign=True, flatten=True, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_1_indents_4_top_comment_false_align_by_equal_sign_true_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_1_indents_4_top_comment_false_align_by_equal_sign_true_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=False, align_by_equal_sign=True, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_1_indents_4_top_comment_true_align_by_equal_sign_false_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_1_indents_4_top_comment_true_align_by_equal_sign_false_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=False, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_1_indents_4_top_comment_true_align_by_equal_sign_true_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_1_indents_4_top_comment_true_align_by_equal_sign_true_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_1_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_1_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=True, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_1_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_50():
    expected_text = read_proto('formatted_test_data_1_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_50.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=True, comment_max_length=50)

    assert expected_text == actual_text


def test_format_str_1_indents_4_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_50():
    expected_text = read_proto('formatted_test_data_1_indents_4_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_50.proto')

    original_file_path = os.path.join(test_path, 'test_data_1.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=False, align_by_equal_sign=True, flatten=True, comment_max_length=50)

    assert expected_text == actual_text


def test_format_str_2_indents_2_top_comment_false_align_by_equal_sign_false_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_2_indents_2_top_comment_false_align_by_equal_sign_false_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, top_comment=False, align_by_equal_sign=False, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_2_indents_2_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_2_indents_2_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, top_comment=False, align_by_equal_sign=True, flatten=True, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_2_indents_4_top_comment_false_align_by_equal_sign_true_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_2_indents_4_top_comment_false_align_by_equal_sign_true_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=False, align_by_equal_sign=True, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_2_indents_4_top_comment_true_align_by_equal_sign_false_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_2_indents_4_top_comment_true_align_by_equal_sign_false_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=False, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_2_indents_4_top_comment_true_align_by_equal_sign_true_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_2_indents_4_top_comment_true_align_by_equal_sign_true_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_2_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_2_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=True, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_2_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_50():
    expected_text = read_proto('formatted_test_data_2_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_50.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=True, comment_max_length=50)

    assert expected_text == actual_text


def test_format_str_2_indents_4_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_50():
    expected_text = read_proto('formatted_test_data_2_indents_4_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_50.proto')

    original_file_path = os.path.join(test_path, 'test_data_2.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=False, align_by_equal_sign=True, flatten=True, comment_max_length=50)

    assert expected_text == actual_text


def test_format_str_3_indents_2_top_comment_false_align_by_equal_sign_false_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_3_indents_2_top_comment_false_align_by_equal_sign_false_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, top_comment=False, align_by_equal_sign=False, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_3_indents_2_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_3_indents_2_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, top_comment=False, align_by_equal_sign=True, flatten=True, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_3_indents_4_top_comment_false_align_by_equal_sign_true_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_3_indents_4_top_comment_false_align_by_equal_sign_true_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=False, align_by_equal_sign=True, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_3_indents_4_top_comment_true_align_by_equal_sign_false_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_3_indents_4_top_comment_true_align_by_equal_sign_false_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=False, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_3_indents_4_top_comment_true_align_by_equal_sign_true_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_3_indents_4_top_comment_true_align_by_equal_sign_true_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_3_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_3_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=True, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_3_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_50():
    expected_text = read_proto('formatted_test_data_3_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_50.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=True, comment_max_length=50)

    assert expected_text == actual_text


def test_format_str_3_indents_4_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_50():
    expected_text = read_proto('formatted_test_data_3_indents_4_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_50.proto')

    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=False, align_by_equal_sign=True, flatten=True, comment_max_length=50)

    assert expected_text == actual_text


def test_format_str_4_indents_2_top_comment_false_align_by_equal_sign_false_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_4_indents_2_top_comment_false_align_by_equal_sign_false_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, top_comment=False, align_by_equal_sign=False, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_4_indents_2_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_4_indents_2_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=2, top_comment=False, align_by_equal_sign=True, flatten=True, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_4_indents_4_top_comment_false_align_by_equal_sign_true_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_4_indents_4_top_comment_false_align_by_equal_sign_true_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=False, align_by_equal_sign=True, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_4_indents_4_top_comment_true_align_by_equal_sign_false_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_4_indents_4_top_comment_true_align_by_equal_sign_false_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=False, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_4_indents_4_top_comment_true_align_by_equal_sign_true_flatten_false_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_4_indents_4_top_comment_true_align_by_equal_sign_true_flatten_false_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=False, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_4_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_none():
    expected_text = read_proto('formatted_test_data_4_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_none.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=True, comment_max_length=None)

    assert expected_text == actual_text


def test_format_str_4_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_50():
    expected_text = read_proto('formatted_test_data_4_indents_4_top_comment_true_align_by_equal_sign_true_flatten_true_comment_max_length_50.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=True, align_by_equal_sign=True, flatten=True, comment_max_length=50)

    assert expected_text == actual_text


def test_format_str_4_indents_4_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_50():
    expected_text = read_proto('formatted_test_data_4_indents_4_top_comment_false_align_by_equal_sign_true_flatten_true_comment_max_length_50.proto')

    original_file_path = os.path.join(test_path, 'test_data_4.proto')
    proto_str = read_file(original_file_path)
    actual_text = format_str(proto_str, indents=4, top_comment=False, align_by_equal_sign=True, flatten=True, comment_max_length=50)

    assert expected_text == actual_text
