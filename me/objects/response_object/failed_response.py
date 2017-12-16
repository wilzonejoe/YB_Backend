from common_response import common_response

class failed_response(common_response):
    """
        Function: Parent class for every "Failed" response
    """
    def __init__(self, status_code= None, headers= None, message = None, debug = None):
        body = {
            "message": message,
            "debug": debug
        }
        super(failed_response,self).__init__(status_code, headers, body)


class bad_request_response(failed_response):
    def __init__(self, headers= None, message = None, debug = None):
        super(bad_request_response,self).__init__(400, headers, message, debug)

class unauthorized_response(failed_response):
    def __init__(self, headers= None, message = None):
        super(unauthorized_response,self).__init__(401, headers, message)

class insufficient_privilege_response(failed_response):
    def __init__(self, headers= None, message = None):
        super(insufficient_privilege_response,self).__init__(403, headers, message)

class not_found_response(failed_response):
    def __init__(self, headers= None, message = None):
        super(not_found_response,self).__init__(404, headers, message)

class not_supported_response(failed_response):
    def __init__(self, headers= None, message = None):
        super(not_supported_response,self).__init__(405, headers, message)

class conflict_response(failed_response):
    def __init__(self, headers= None, message = None):
        super(conflict_response,self).__init__(409, headers, message)

class internal_server_error_response(failed_response):
    def __init__(self, headers= None,  message = None):
        super(internal_server_error_response,self).__init__(500, headers, "Internal server error : " + message)