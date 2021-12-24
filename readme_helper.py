from src.proto_formatter import format_str

proto_str = """

syntax = "proto3";

package sc.mocker;

option java_package = "net.skyscanner.mocker.schema";
option java_outer_classname = "SaveProto";
option java_multiple_files = true;

// All HTTP methods.
enum HTTPMethod {
    HTTP_METHOD_UNSPECIFIED  = 0; // Unspecified http method
    HTTP_METHOD_GET = 1;// HTTP GET method
    HTTP_METHOD_HEAD = 2;// HTTP HEAD method
    HTTP_METHOD_POST = 3;// HTTP POST method
    HTTP_METHOD_PUT = 4;// HTTP PUT method
    HTTP_METHOD_DELETE = 5;// HTTP DELETE method
    HTTP_METHOD_CONNECT = 6;// HTTP CONNECT method
    HTTP_METHOD_OPTIONS = 7;// HTTP OPTIONS method
    HTTP_METHOD_TRACE = 8;// HTTP TRACE method
}
// The request message of save API. 
// Including full request and response data of the third part service.
message MockDataRequest{
    string session_id = 1; // UUID to identify this request, will be used to query dat from S3
    HTTPMethod http_method = 2; // the http method, GET, POST...
    string url = 3;//Original third part request url, may be used to create matching rules
    string request_cookies = 4;// The original request cookies of the third part if has, most of time for web GET query.
    map<string, string> request_headers = 5;// The original request headers to the third part.
    string request_body = 6;// The original request body to the third part.
    map<string, string> response_headers = 7;// The original response headers to the third part.
    string response_body = 8;// The original response body to the third part.
    uint32 response_delay_time = 9;// The delay time when retrieve the response data.
}

// API process status result.
enum Status  {
    STATUS_UNSPECIFIED = 0;// Unspecified response status

    STATUS_SUCCESS = 1;// Successful status
    STATUS_FAIL = 2;// FAIL status
}

// The response message of save API.
// Including the UUID of the saved data and process status.
// Error message will not be empty if status is FAIL   
message MockDataResponse {
    string session_id = 1; // UUID to identify the mocked data.
    Status status = 2; // Save operation result, fail or success
    string error=3;//Error message if API call failed.
}


service Save {
    rpc Save (MockDataRequest) returns (MockDataResponse);
}
"""
formatted_proto_str = format_str(proto_str, align_by_equal_sign=True, comment_max_length=120, indents=4)
print(formatted_proto_str)
