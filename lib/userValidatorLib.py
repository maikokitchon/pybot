import json

def userValidatorLib(user_info):
    is_authorized = False
    user = json.load(open('./data/user.json'))
    for allowed_user_email in user['allowed_user_email']:
        if allowed_user_email == user_info['user']['profile']['email']:
            is_authorized = True
            break
    return is_authorized