from src.proto_formatter import format_str

proto_str = """
// This file is copied from https://github.com/envoyproxy/protoc-gen-validate/blob/main/validate/validate.proto
// Created on 2021-12-22

syntax = "proto2";


// Validation rules applied at the message level
extend google.protobuf.MessageOptions {
    // Disabled nullifies any validation rules for this message, including any
    // message fields associated with it that do support validation.
    optional bool disabled = 1071;
    // Ignore skips generation of validation methods for this message.
    optional bool ignored = 1072;
}

"""
formatted_proto_str = format_str(proto_str, align_by_equal_sign=True, comment_max_length=120, indents=4)
print(formatted_proto_str)
