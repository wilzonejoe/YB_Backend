from admin.users.controller import handler as users
from me.controller import handler as me

# Test ADD
event= {
    "httpMethod": "POST",
    "body": "{\"firstName\":\"Wilson\", \"lastName\":\"Joe\", \"phoneNumber\":\"29123781237\", \"mobilePhoneNumber\":\"213123432\"}",
}

print "[Basic Flow] Create User : " + str(me(event, None))

# Test GET
event= {
    "httpMethod": "GET",
    "body": "",
    "pathParameters":None
}

print "[Basic Flow] List User: " + str(users(event, None))