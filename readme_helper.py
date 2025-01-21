from proto_formatter import format_str

proto_str = """
    /*
    Person balabala
*/
    message Person {
    // comment of name a
required string name = 1; // comment of name b
/* 
comment of id a
// comment of id b
         */
        required int32 id = 2;// comment of id c
       optional string email = 3;// comment of email
}
"""
formatted_proto_str = format_str(proto_str)
print(formatted_proto_str)
