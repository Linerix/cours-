import json
def save_credentials(login, password):
    with open('credentials.json', 'w') as file:
        credentials = {'login': login,'password': password}
        json.dump(credentials, file)
save_credentials('my_login', 'my_password')