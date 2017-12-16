class list_user_data(object):
    def __init__(self, id = None, username = None, firstName= None, lastName= None, role= None, crmName = None, *args, **kwargs):
        self.id = id
        self.username = username
        self.first_name = firstName
        self.last_name= lastName
        self.role = role
        self.crmName = crmName