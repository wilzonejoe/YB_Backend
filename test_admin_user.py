from admin.users.controller import handler as users
from me.controller import handler as me

# Test ADD
event= {
    "httpMethod": "POST",
    "body": "{\"firstName\":\"Joe\", \"lastName\":\"Wilson\", \"phoneNumber\":\"29123781237\", \"mobilePhoneNumber\":\"213123432\"}",
    "requestContext":{
        "authorizer":{
            "claims":{
                "sub":"695f5f6b-a7c9-4e98-8cc7-a98f977admin",
                "username":"admin"
            }
        }
    }
}

print "[Basic Flow] Create User : " + str(me(event, None))


# Test ADD
event= {
    "httpMethod": "PUT",
    "body": "{\"roleId\":\"3\", \"crmId\":\"1\", \"firstName\":\"Joe\", \"lastName\":\"Wilson\", \"phoneNumber\":\"29123781237\", \"mobilePhoneNumber\":\"213123432\"}",
    "pathParameters":{
        "id":"695f5f6b-a7c9-4e98-8cc7-a98f977admin"
    },
    "requestContext":{
        "authorizer":{
            "claims":{
                "sub":"695f5f6b-a7c9-4e98-8cc7-a98f977admin",
                "username":"admin"
            }
        }
    }
}

print "[Basic Flow] Update User : " + str(users(event, None))

# Test ADD
event= {
    "httpMethod": "POST",
    "body": "{\"firstName\":\"Joe\", \"lastName\":\"Wilson\", \"phoneNumber\":\"29123781237\", \"mobilePhoneNumber\":\"213123432\"}",
    "requestContext":{
        "authorizer":{
            "claims":{
                "sub":"695f5f6b-a7c9-4e98-8cc7-a98f977ca94a",
                "username":"username0"
            }
        }
    }
}

print "[Basic Flow] Create User : " + str(me(event, None))

# Test ADD
event= {
    "httpMethod": "POST",
    "body": "{\"firstName\":\"Wilson\", \"lastName\":\"Joe\", \"phoneNumber\":\"29123781237\", \"mobilePhoneNumber\":\"213123432\"}",
    "requestContext":{
        "authorizer":{
            "claims":{
                "sub":"695f5f6b-a7c9-4e98-8cc7-a98f977ca94b",
                "username":"username1"
            }
        }
    }
}

print "[Basic Flow] Create User : " + str(me(event, None))

# Test ADD
event= {
    "httpMethod": "POST",
    "body": "{\"firstName\":\"Miguel\", \"lastName\":\"Miguel Saavedra\", \"phoneNumber\":\"29123781237\", \"mobilePhoneNumber\":\"213123432\"}",
    "requestContext":{
        "authorizer":{
            "claims":{
                "sub":"695f5f6b-a7c9-4e98-8cc7-a98f977ca94c",
                "username":"username2"
            }
        }
    }
}

print "[Basic Flow] Create User : " + str(me(event, None))

# Test GET
event= {
    "httpMethod": "GET",
    "body": "",
    "pathParameters":None,
    "requestContext":{
        "authorizer":{
            "claims":{
                "sub":"695f5f6b-a7c9-4e98-8cc7-a98f977admin",
                "username":"admin"
            }
        }
    }
}

print "[Basic Flow] List User: " + str(users(event, None))

# Test GET
event= {
    "httpMethod": "GET",
    "body": "",
    "pathParameters":{
        "id":"695f5f6b-a7c9-4e98-8cc7-a98f977ca94c"
    },
    "requestContext":{
        "authorizer":{
            "claims":{
                "sub":"695f5f6b-a7c9-4e98-8cc7-a98f977admin",
                "username":"admin"
            }
        }
    }
}

print "[Basic Flow] Get User By Id: " + str(users(event, None))


# Test GET
event= {
    "httpMethod": "DELETE",
    "body": "",
    "pathParameters":{
        "id":"695f5f6b-a7c9-4e98-8cc7-a98f977ca94c"
    },
    "requestContext":{
        "authorizer":{
            "claims":{
                "sub":"695f5f6b-a7c9-4e98-8cc7-a98f977admin",
                "username":"admin"
            }
        }
    }
}

print "[Basic Flow] Delete User: " + str(users(event, None))

# Test GET
event= {
    "httpMethod": "DELETE",
    "body": "",
    "pathParameters":{
        "id":"695f5f6b-a7c9-4e98-8cc7-a98f977ca94b"
    },
    "requestContext":{
        "authorizer":{
            "claims":{
                "sub":"695f5f6b-a7c9-4e98-8cc7-a98f977admin",
                "username":"admin"
            }
        }
    }
}

print "[Basic Flow] Delete User: " + str(users(event, None))

# Test GET
event= {
    "httpMethod": "DELETE",
    "body": "",
    "pathParameters":{
        "id":"695f5f6b-a7c9-4e98-8cc7-a98f977ca94a"
    },
    "requestContext":{
        "authorizer":{
            "claims":{
                "sub":"695f5f6b-a7c9-4e98-8cc7-a98f977admin",
                "username":"admin"
            }
        }
    }
}

print "[Basic Flow] Delete User: " + str(users(event, None))



