from me.controller import handler

# Test ADD
event= {
    "httpMethod": "POST",
    "body": "{\"firstName\":\"Wilson\", \"phoneNumber\":\"29123781237\", \"mobilePhoneNumber\":\"213123432\"}",
    "requestContext": {
        "authorizer": {
            "claims": {
                "sub": "695f5f6b-a7c9-4e98-8cc7-a98f977ca94b",
                "username": "username1"
            }
        }
    }
}

print "[Exception Flow] Create User Without Last Name : " + str(handler(event, None))

# Test ADD
event= {
    "httpMethod": "POST",
    "body": "{\"lastName\":\"Joe\", \"phoneNumber\":\"29123781237\", \"mobilePhoneNumber\":\"213123432\"}",
    "requestContext": {
        "authorizer": {
            "claims": {
                "sub": "695f5f6b-a7c9-4e98-8cc7-a98f977ca94b",
                "username": "username1"
            }
        }
    }
}

print "[Exception Flow] Create User Without First Name : " + str(handler(event, None))

# Test ADD
event= {
    "httpMethod": "POST",
    "body": "{\"firstName\":\"Wilson\", \"lastName\":\"Joe\", \"phoneNumber\":\"29123781237\", \"mobilePhoneNumber\":\"213123432\"}",
    "requestContext": {
        "authorizer": {
            "claims": {
                "sub": "695f5f6b-a7c9-4e98-8cc7-a98f977ca94b",
                "username": "username1"
            }
        }
    }
}

print "[Basic Flow] Create User With All Field Present: " + str(handler(event, None))

# Test ADD
event= {
    "httpMethod": "POST",
    "body": "{\"firstName\":\"Wilson\", \"lastName\":\"Joe\", \"phoneNumber\":\"29123781237\", \"mobilePhoneNumber\":\"213123432\"}",
    "requestContext": {
        "authorizer": {
            "claims": {
                "sub": "695f5f6b-a7c9-4e98-8cc7-a98f977ca94b",
                "username": "username1"
            }
        }
    }
}

print "[Exception Flow] Created User With Existing Id: " + str(handler(event, None))

# Test GET
event= {
    "httpMethod": "GET",
    "body": "",
    "requestContext": {
        "authorizer": {
            "claims": {
                "sub": "695f5f6b-a7c9-4e98-8cc7-a98f977ca94b",
                "username": "username1"
            }
        }
    }
}

print "[Basic Flow] GET User: " + str(handler(event, None))

# Test UPDATE
event= {
    "httpMethod": "PUT",
    "body": "{\"firstName\":\"Wilson1\", \"lastName\":\"Joe1\", \"phoneNumber\":\"29123781237\", \"mobilePhoneNumber\":\"213123432\"}",
    "requestContext": {
        "authorizer": {
            "claims": {
                "sub": "695f5f6b-a7c9-4e98-8cc7-a98f977ca94b",
                "username": "username1"
            }
        }
    }
}

print "[Basic Flow] Update User: " + str(handler(event, None))

# Test GET
event= {
    "httpMethod": "GET",
    "body": "",
    "requestContext": {
        "authorizer": {
            "claims": {
                "sub": "695f5f6b-a7c9-4e98-8cc7-a98f977ca94b",
                "username": "username1"
            }
        }
    }
}

print "[Basic Flow] Get User : " + str(handler(event, None))


# Test DELETE
event= {
    "httpMethod": "DELETE",
    "body": "",
    "requestContext": {
        "authorizer": {
            "claims": {
                "sub": "695f5f6b-a7c9-4e98-8cc7-a98f977ca94b",
                "username": "username1"
            }
        }
    }
}

print "[Basic Flow] Delete User  : " + str(handler(event, None))

# Test GET
event= {
    "httpMethod": "GET",
    "body": "",
    "requestContext": {
        "authorizer": {
            "claims": {
                "sub": "695f5f6b-a7c9-4e98-8cc7-a98f977ca94b",
                "username": "username1"
            }
        }
    }
}

print "[Basic Flow] Get User : " + str(handler(event, None))

