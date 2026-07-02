import sender_stand_request
import data

def get_new_user_token():
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # 2. Llamamos a la función que hace la petición HTTP pasando el cuerpo
    respuesta = sender_stand_request.post_new_user(current_body)
    # 3. Convertimos la respuesta a JSON y extraemos el authToken para devolverlo
    return respuesta.json()["authToken"]

# Función de prueba positiva
def positive_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_token
    user_token = get_new_user_token()
    # El resultado de la solicitud para obtener el token se guarda en la variable user_response
    user_response = sender_stand_request.post_new_kit(kit_body,user_token)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo name está en la respuesta y contiene un valor
    assert user_response.json()["name"] == kit_body["name"]

# Función de prueba negativa
def negative_assert(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable token
    user_token = get_new_user_token()

    # Comprueba si la variable "response" almacena el resultado de la solicitud.
    response = sender_stand_request.post_new_kit(kit_body,user_token)

    # Comprueba si la respuesta contiene el código 400.
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["code"] == 400
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

# Función de prueba negativa
# La respuesta contiene el siguiente mensaje de error: "No se han enviado todos los parámetros requeridos"
def negative_assert_no_kit_body(kit_body):
    # El cuerpo de la solicitud actualizada se guarda en la variable token
    user_token = get_new_user_token()
    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_new_kit(kit_body,user_token)

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400
    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se han enviado todos los parámetros requeridos"

# Prueba 1. Creación de un nuevo kit con una caracter
# El parámetro "name" contiene un caracter
def test_create_new_kit_1_letter_in_name_get_success_response():
    positive_assert(data.get_kit_body("a"))

# Prueba 2. Creación de un nuevo kit con 511 caracteres
# El parámetro "name" contiene 511 caracteres
def test_create_new_kit_511_letters_in_name_get_success_response():
    positive_assert(data.get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"))

# Prueba 3. Error
# El parámetro "name" contiene un string vacío
def test_create_new_kit_empty_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = data.get_kit_body("")
    # Comprueba la respuesta
    negative_assert(kit_body)

# Prueba 4. Error
# El parámetro "name" contiene 513 caracteres
def test_create_new_kit_513_letters_in_name_get_error_response():
    kit_body = data.get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcDa")
    # Comprueba la respuesta
    negative_assert(kit_body)

# Prueba 5. Creación de un nuevo kit con caracteres especiales
# El parámetro "name" contiene un string de caracteres especiales
def test_create_new_kit_has_special_symbol_in_name_get_success_response():
    positive_assert(data.get_kit_body("\"№%@\","))

# Prueba 6. Creación de un nuevo kit con espacios entre si
# El parámetro "Name" contiene palabras con espacios
def test_create_new_kit_has_space_in_name_get_success_response():
    positive_assert(data.get_kit_body("A Aaa"))

# Prueba 7. Creación de un nuevo kit con numeros
# El parámetro "Name" contiene numeros
def test_create_new_kit_has_number_in_name_get_success_response():
    positive_assert(data.get_kit_body("123"))

# Prueba 8. Error
# El parámetro no contiene name
def test_create_new_kit_no_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "kit_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    kit_body = data.kit_body.copy()
    # El parámetro "name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_no_kit_body(kit_body)

# Prueba 9. Error
# Se ha pasado un tipo de parámetro diferente (número)
def test_create_new_kit_number_type_name_get_error_response():
    # Copiamos el diccionario base para no alterar el archivo de datos original
    kit_body = data.kit_body.copy()

    # Cambiamos el valor del parámetro "name" por un número entero
    kit_body["name"] = 123

    # Comprobamos que la API devuelva el error correspondiente
    negative_assert(kit_body)