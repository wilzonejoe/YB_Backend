class information(object):
    def __init__(self, event):
        """
            Function: Extract necessary information from event object

            Params:
            @event : containing data retrieved by AWS api gateway
        """
        self.httpMethod = event["httpMethod"]
        self.body = event["body"]
        self.userId = "695f5f6b-a7c9-4e98-8cc7-a98f977ca94b"
        self.username = "username2"
        # self.user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
        # self.user_name = event["requestContext"]["authorizer"]["claims"]["username"]