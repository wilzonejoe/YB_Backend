class information(object):
    def __init__(self, event):
        """
            Function: Extract necessary information from event object

            Params:
            @event : containing data retrieved by AWS api gateway
        """
        self.httpMethod = event["httpMethod"]
        self.body = event["body"]
        self.user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
        self.username = event["requestContext"]["authorizer"]["claims"]["username"]