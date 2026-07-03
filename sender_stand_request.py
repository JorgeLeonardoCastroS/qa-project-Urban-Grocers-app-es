import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

def post_new_kit(kit_body,auth_token):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         # inserta la dirección URL completa
                         json=kit_body,  # inserta el nuevo kit de solicitud
                         headers={"Authorization": "Bearer " + auth_token})  # inserta los encabezados