import os
from proto_formatter.object_parser import ObjectParser
from helper import test_path, read_lines

original_file_path_1 = os.path.join(test_path, 'test_data_1.proto')
original_file_path_2 = os.path.join(test_path, 'test_data_2.proto')
original_file_path_3 = os.path.join(test_path, 'test_data_3.proto')


def test_parse_object_netesed():
    lines = read_lines(original_file_path_3)
    op = ObjectParser()
    op.parse(lines)

    assert len(op.objects) == 3
    assert op.objects[0].name == 'Outer'
    assert op.objects[0].elements[0].name == 'MiddleAA'
    assert op.objects[0].elements[0].elements[0].name == 'Inner'
    assert op.objects[0].elements[0].elements[0].elements[1].name == 'booly'
    assert op.objects[1].name == 'Outer2'
    assert op.objects[2].name == 'Demo'
