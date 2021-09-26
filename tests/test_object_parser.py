import os
from proto_formatter.object_parser import ObjectParser
from .helper import test_path, read_lines


def test_parse_object_nested():
    original_file_path = os.path.join(test_path, 'test_data_3.proto')
    lines = read_lines(original_file_path)
    op = ObjectParser()
    op.parse(lines)

    assert len(op.objects) == 3
    assert op.objects[0].name == 'Outer'
    assert op.objects[0].elements[0].name == 'MiddleAA'
    assert op.objects[0].elements[0].elements[0].name == 'Inner'
    assert op.objects[0].elements[0].elements[0].elements[1].name == 'booly'
    assert op.objects[1].name == 'Outer2'
    assert op.objects[2].name == 'Demo'
