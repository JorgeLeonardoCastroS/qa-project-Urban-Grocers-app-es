headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Leonardo",
    "phone": "+57234567890",
    "address": "123 Elm Street, Hilltop"
}

kit_body = {
    "name": "A"
}
def get_kit_body(name):
    return {"name": name}