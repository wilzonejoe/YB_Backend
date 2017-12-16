import json

from users_functions import users_functions
from objects import api_gateway
from objects.response_object import successful_response
from objects.response_object import failed_response
from custom_exception.bad_request_exception import bad_request_exception
from custom_exception.not_found_exception import not_found_exception
from custom_exception.conflict_exception import conflict_exception

def handler(event, context):
    # Extracting information from API Gateway
    info = api_gateway.information(event)

    # Extracting information from contants.json
    with open("constants.json", "r") as resources_file:
        resources = json.loads(resources_file.read())

    try:
        # Route function to the right destination
        if info.http_method == 'GET':
            # route to get_user method to get user to database, if none found then return not found exception (404)

            if info.request_id is not None:
                resp = users_functions.get_user(info.request_id, resources)
                if resp is None:
                    raise not_found_exception("User id : " + info.request_id + " is not found")
            else:
                resp = users_functions.list_users(resources)

            return successful_response.ok_response(None, resp).dictate()
        elif info.http_method == 'PUT':
            # route to update_user method to update user to database, expected to return ok if successful (200)
            resp = users_functions.update_user(info.userId, info.body, resources)
            return successful_response.ok_response(None, resp).dictate()
        elif info.http_method == 'DELETE':
            # route to delete_user method to delete user to database, expected to return no content if successful (204)
            resp = users_functions.delete_user(info.userId, resources)
            return successful_response.no_content_response(None, resp).dictate()
    except bad_request_exception as e:
        # Throw bad request (400)
        # Show debug if there is debug key in the message
        if "debug" in e.message :
            message = e.message["message"]
            debug = e.message["debug"]
        else:
            message = e.message
            debug = None
        return failed_response.bad_request_response(None, message, debug).dictate()
    except not_found_exception as e:
        # Throw not found exception (404)
        return failed_response.not_found_response(None, e.message).dictate()
    except conflict_exception as e:
        # Throw conflict exception (409)
        return failed_response.conflict_response(None, e.message).dictate()
    except Exception as e:
        # Throw unknown/uncaught(500)
        return failed_response.internal_server_error_response(None, e.message).dictate()

    # Throw not supported exception(405) since non of the request above is satisfied
    return failed_response.not_supported_response(None, "Your request is not supported").dictate()
