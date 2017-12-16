from common_response import common_response

class ok_response(common_response):
    def __init__(self, headers= None, body = None):
        super(ok_response,self).__init__(200, headers, body)

class created_response(common_response):
    def __init__(self, headers= None, body = None):
        super(created_response,self).__init__(201, headers, body)

class no_content_response(common_response):
    def __init__(self, headers= None, body = None):
        super(no_content_response,self).__init__(204, headers, body)