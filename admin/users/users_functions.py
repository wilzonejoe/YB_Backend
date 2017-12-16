import json
from objects.user_data import user_data
from sql_utils import sql_functions
from sql_utils import sql_scripts
from custom_exception.not_found_exception import not_found_exception

class users_functions(object):
    @staticmethod
    def list_users(resources):
        """
            function: Get myself (USER) into the database

            Params:
            @userId = cognito userId
            @username = cognito username
            @userData = JSON data which contains user data
            @resources = contains data to be used to access DB

            return: user_object
        """
        sql_script = sql_scripts.User["List"]
        resp = sql_functions.sql_functions.list_data_from_table(resources, sql_script)

        users = {
            "users": resp
        }
        return users

    @staticmethod
    def get_user(user_id, resources):
        """
            function: Get myself (USER) into the database

            Params:
            @userId = cognito userId
            @username = cognito username
            @userData = JSON data which contains user data
            @resources = contains data to be used to access DB

            return: user_object
        """
        sql_script = sql_scripts.User["Get"].format(user_id)
        resp = sql_functions.sql_functions.list_data_from_table(resources, sql_script)
        if len(resp) == 0:
            return None
        else:
            return resp

    @staticmethod
    def update_user(user_id, userData, resources):
        """
            function: Update myself (USER) into the database, username should not be updated

            Params:
            @userId = cognito userId
            @userData = JSON data which contains user data
            @resources = contains data to be used to access DB

            return: message
        """
        # check if user exists
        if users_functions.get_user(user_id, resources) is None:
            message = "User id : " + user_id + " is not found"
            raise not_found_exception(message)

        json_object = json.loads(userData)
        update_user_data = user_data(**json_object)
        update_user_data.validate()

        sql_script = sql_scripts.User["Update"].format(update_user_data.role_id, update_user_data.crm_id,
                                                       update_user_data.first_name, update_user_data.last_name,
                                                       update_user_data.phone_number, update_user_data.mobile_phone_number,
                                                       user_id)
        sql_functions.sql_functions.execute_sql_command(resources, sql_script)

        resp = {
            "message": "user information updated successfully."
        }

        return resp


    @staticmethod
    def delete_user(user_id, resources):
        """
            function: Delete myself (USER) from the database

            Params:
            @userId = cognito userId
            @userData = JSON data which contains user data
            @resources = contains data to be used to access DB

            return: message
        """
        # check if user exists
        if users_functions.get_user(user_id, resources) is None:
            message = "User id : " + user_id + " is not found"
            raise not_found_exception(message)

        sql_script = sql_scripts.User["Delete"].format(user_id)
        sql_functions.sql_functions.insert_into_table(resources, sql_script)

        resp = {
            "message":"user deleted successfully."
        }

        return resp
