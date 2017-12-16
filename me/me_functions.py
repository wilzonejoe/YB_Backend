import json
from objects.user_data import user_data
from sql_utils import sql_functions
from sql_utils import sql_scripts
from custom_exception.conflict_exception import conflict_exception
from custom_exception.not_found_exception import not_found_exception

class me_functions(object):
    @staticmethod
    def add_me(user_id, username, userData, resources):
        """
            function: Add myself (USER) into the database

            Params:
            @userId = cognito userId
            @username = cognito username
            @userData = JSON data which contains user data
            @resources = contains data to be used to access DB

            return: user object
        """

        json_object = json.loads(userData)
        sign_up_data = user_data(**json_object)
        sign_up_data.validate()

        # check if user exists
        if me_functions.get_me(user_id, resources) is not None:
            message = "User id : " + user_id + " existed"
            raise conflict_exception(message)

        sql_script = sql_scripts.User["Create"].format(user_id, username, sign_up_data.first_name, sign_up_data.last_name, sign_up_data.phone_number, sign_up_data.mobile_phone_number)
        sql_functions.sql_functions.insert_into_table(resources, sql_script)

        created_user_data = me_functions.get_me(user_id, resources)

        return created_user_data


    @staticmethod
    def get_me(user_id, resources):
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
            user = resp[0]
            return user_data(user[0], user[1], user[2], user[3], user[4], user[5]).__dict__



    @staticmethod
    def update_me(user_id, userData, resources):
        """
            function: Update myself (USER) into the database, username should not be updated

            Params:
            @userId = cognito userId
            @userData = JSON data which contains user data
            @resources = contains data to be used to access DB

            return: message
        """
        # check if user exists
        if me_functions.get_me(user_id, resources) is None:
            message = "User id : " + user_id + " is not found"
            raise not_found_exception(message)

        json_object = json.loads(userData)
        update_user_data = user_data(**json_object)

        sql_script = sql_scripts.User["Update"].format(update_user_data.first_name,
                                                       update_user_data.last_name, update_user_data.phone_number,
                                                       update_user_data.mobile_phone_number, user_id)
        sql_functions.sql_functions.execute_sql_command(resources, sql_script)

        resp = {
            "message": "user information updated successfully."
        }

        return resp


    @staticmethod
    def delete_me(user_id, resources):
        """
            function: Delete myself (USER) from the database

            Params:
            @userId = cognito userId
            @userData = JSON data which contains user data
            @resources = contains data to be used to access DB

            return: message
        """
        # check if user exists
        if me_functions.get_me(user_id, resources) is None:
            message = "User id : " + user_id + " is not found"
            raise not_found_exception(message)

        sql_script = sql_scripts.User["Delete"].format(user_id)
        sql_functions.sql_functions.insert_into_table(resources, sql_script)

        resp = {
            "message":"user deleted successfully."
        }

        return resp
