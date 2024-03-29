class information(object):
    def __init__(self, event):
        """
            Function: Extract necessary information from event object

            Params:
            @event : containing data retrieved by AWS api gateway
        """
        self.http_method = event["httpMethod"]
        self.body = event["body"]
        self.request_id = None

        if event["pathParameters"] is not None:
            self.request_id = event["pathParameters"]["id"]

        self.user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
        self.user_name = event["requestContext"]["authorizer"]["claims"]["username"]