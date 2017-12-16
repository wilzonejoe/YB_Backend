import json
from sql_utils import sql_functions
from sql_utils import sql_scripts

class role_functions(object):
    @staticmethod
    def get_role(role_id, role_name, resources):
        sql_script = sql_scripts.Role["Get"].format(role_id, role_name)
        resp = sql_functions.sql_functions.list_data_from_table(resources, sql_script)
        if len(resp) == 0:
            return None
        else:
            return resp