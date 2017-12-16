from ..custom_exception.bad_request_exception import bad_request_exception

class user_data(object):
    def __init__(self, id = None, username = None, roleId = None, crmId = None, firstName= None, lastName= None, phoneNumber= None, mobilePhoneNumber = None, *args, **kwargs):
        self.id = id
        self.username = username
        self.role_id = roleId
        self.crm_id = crmId
        self.first_name = firstName
        self.last_name= lastName
        self.phone_number = phoneNumber
        self.mobile_phone_number = mobilePhoneNumber

    def validate(self):
        field_error = []

        if self.first_name is None or self.first_name is "":
            field_error.append({"field": "firstName", "message" : "firstName should not be null or empty" })

        if self.last_name is None or self.last_name is "":
            field_error.append({"field": "lastName", "message" : "lastName should not be null or empty" })

        if self.role_id is None or self.role_id is "":
            field_error.append({"field": "roleId", "message" : "roleId should not be null or empty" })

        if self.crm_id is None or self.crm_id is "":
            field_error.append({"field": "crmId", "message" : "crmId should not be null or empty" })

        if len(field_error):
            error_content = {"message":"Field validation error.", "debug": field_error}
            raise bad_request_exception(error_content)