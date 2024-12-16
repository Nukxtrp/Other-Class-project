class client_list:
    client_dict = {}

    def __init__(self) -> None:
        pass

    def add_client(self, username, client):
        self.client_dict[username] = client

    def delete_client(self, username):
        self.client_dict.pop(username)

    def grab_username(self, username):
        result = self.client_dict[username]
        if result == None:
            raise LookupError()
        else:
            return result
    
    def grab_all(self):
        return list(self.client_dict.values())
    