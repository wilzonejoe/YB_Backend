import json

from me_functions import me_functions
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
        if info.httpMethod == 'POST':
            #route to add_me method to add myself to database, expected to return created if successful (201)
            resp = me_functions.add_me(info.user_id, info.username, info.body, resources)
            return successful_response.created_response(None, resp).dictate()
        elif info.httpMethod == 'GET':
            # route to get_me method to get myself to database, if none found then return not found exception (404)
            resp = me_functions.get_me(info.user_id, resources)
            if resp is None:
                raise not_found_exception("User id : " + info.user_id + " is not found")
            return successful_response.ok_response(None, resp).dictate()
        elif info.httpMethod == 'PUT':
            # route to update_me method to update myself to database, expected to return ok if successful (200)
            resp = me_functions.update_me(info.user_id, info.body, resources)
            return successful_response.ok_response(None, resp).dictate()
        elif info.httpMethod == 'DELETE':
            # route to delete_me method to delete myself to database, expected to return no content if successful (204)
            resp = me_functions.delete_me(info.user_id, resources)
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
