# 🛒 Proyecto Urban Grocers - Pruebas Automatizadas de API (`name` de un Kit)

## 📌 Título del Proyecto
**Proyecto Urban Grocers: Pruebas Automatizadas y Validación de API para la Creación de Kits**

## 📝 Descripción General del Proyecto
Este proyecto está enfocado en la automatización de pruebas para la API REST de la aplicación de compras en línea **Urban Grocers**, específicamente evaluando el comportamiento del parámetro `name` en el endpoint de creación de kits de usuario. La suite de pruebas valida la lógica del backend mediante peticiones HTTP, asegurando que el sistema acepte o rechace cadenas de texto según los límites y restricciones especificadas en la documentación oficial de la API.

---

## 🎯 Objetivos
* 📌 **Validación de Reglas de Negocio:** Verificar que el parámetro `name` cumpla rigurosamente con los criterios de aceptación (longitud de caracteres, tipos de datos permitidos, caracteres especiales y sensibilidad a campos vacíos/nulos).
* 📌 **Automatización de Pruebas de API:** Implementar un conjunto de pruebas funcionales y de regresión automatizadas utilizando Python, `pytest` y `requests`.
* 📌 **Identificación de Incidencias:** Detectar discrepancias entre la especificación del API y la respuesta real del servidor (códigos de estado HTTP y cuerpo de respuesta).
* 📌 **Garantía de Calidad:** Asegurar que las funcionalidades clave del flujo de usuario y la creación de datos no afecten la estabilidad global de la plataforma.

---

## 📐 Alcance de las Pruebas
El alcance abarca la validación funcional del endpoint de creación de kits y flujos de soporte en la API de Urban Grocers:

* 🟢 **Creación de Usuarios y Autenticación:** Envío de solicitudes `POST /api/v1/users` para generar el token de autorización (`authToken`) necesario.
* 🟢 **Validación del Parámetro `name` en Kits:** Envío de solicitudes `POST /api/v1/kits` evaluando combinaciones de límites (clases de equivalencia y valores límite).
* 🟢 **Consulta de Información:** Envíos `GET` para obtener información sobre usuarios y documentación técnica de soporte.
* 🟢 **Casos de Esquina y Errores:** Validación de códigos de estado HTTP esperados (por ejemplo, `201 Created` vs `400 Bad Request`).

---

## 🧪 Estrategia de Pruebas
La estrategia se centró en la combinación de análisis estático de requerimientos y pruebas dinámicas automatizadas:

1. 📋 **Análisis de Requerimientos:** Revisión exhaustiva de la documentación en Swagger/Apidoc para definir la matriz de pruebas.
2. 📐 **Partición de Equivalencia y Valores Límite:** Diseño de casos de prueba considerando:
   * Mínimo y máximo de caracteres permitidos (ej. 1 carácter, 511 caracteres, 512 caracteres).
   * Uso de caracteres especiales, números y espacios.
   * Ausencia del parámetro o envío de valores nulos/vacíos.
3. ⚙️ **Flujo de Ejecución Automatizado:**
   * Generación dinámica de un nuevo usuario antes de cada prueba para obtener un token de autorización válido.
   * Envío del payload con la variación del parámetro `name`.
   * Aserción de los códigos de respuesta (`status_code`) y la estructura del JSON devuelto.

---

## 🔬 Tipos de Pruebas
* 🔌 **Pruebas de API / Backend Testing:** Validación de endpoints REST mediante solicitudes HTTP `POST` y `GET`.
* 🔄 **Pruebas Funcionales Automatizadas:** Verificación de lógica de negocio en el backend.
* 🔍 **Pruebas de Regresión:** Ejecución continua de la suite para verificar que cambios en el código no rompan funcionalidades existentes.
* 📊 **Pruebas de Valores Límite y Clases de Equivalencia:** Cobertura exhaustiva de entradas válidas e inválidas para el parámetro `name`.

---

## 🛠️ Herramientas y Tecnologías
* 🐍 **Lenguaje de Programación:** Python
* 🧪 **Framework de Pruebas:** Pytest
* 🌐 **Librería HTTP:** Requests
* 💻 **IDE:** PyCharm
* 🚀 **Pruebas Manuales de API & Endpoints:** Postman
* 🐞 **Gestión de Defectos y Casos de Prueba:** JIRA
* 📚 **Documentación de API:** Apidoc / Swagger
* 📊 **Hojas de Cálculo:** Google Sheets / Microsoft Excel

---

## 📋 Casos de Prueba
Se diseñaron e implementaron más de **50 casos de prueba** cubriendo escenarios positivos y negativos para el campo `name`:

| ID Caso | Descripción / Parámetro `name` | Tipo de Prueba | Resultado Esperado (Status Code) |
| :--- | :--- | :--- | :--- |
| **TC01** | `name` con 1 carácter (límite inferior válido) | Valor Límite | `201 Created` |
| **TC02** | `name` con 511 caracteres (límite superior válido) | Valor Límite | `201 Created` |
| **TC03** | `name` con 0 caracteres (campo vacío) | Valor Límite | `400 Bad Request` |
| **TC04** | `name` con 512 caracteres (excede límite) | Valor Límite | `400 Bad Request` |
| **TC05** | `name` con caracteres especiales (ej. `"№%@,"`) | Clase de Equivalencia | `201 Created` |
| **TC06** | `name` con espacios intermedios y guiones | Clase de Equivalencia | `201 Created` |
| **TC07** | `name` compuesto solo por números (cadena) | Clase de Equivalencia | `201 Created` |
| **TC08** | Parámetro `name` ausente en el payload | Error / Negativa | `400 Bad Request` |
| **TC09** | Parámetro `name` con tipo de dato incorrecto (número entero) | Error / Negativa | `400 Bad Request` |

---

## 🐛 Reporte de Defectos
Durante la fase de validación funcional y automatizada se generaron **más de 50 reportes de incidentes en JIRA**, clasificando los bugs según su severidad y prioridad:

* 🚨 **Defectos de Integración / API:** Discrepancias entre la respuesta HTTP recibida y la documentada en Swagger (por ejemplo, retorno de `500 Internal Server Error` en lugar de `400 Bad Request` ante payloads malformados).
* 🎨 **Defectos de UI / Diseño:** Inconsistencias visuales en la aplicación frontend al intentar desplegar nombres de kits con caracteres especiales o cadenas de longitud máxima.
* ⚠️ **Defectos de Validación:** Aceptación de parámetros `name` que superaban los límites establecidos por la documentación técnica.

---

## 📊 Resultados y Métricas
* 🎯 **Casos de Prueba Ejecutados:** +50 casos de prueba automatizados y manuales.
* 🐛 **Reportes de Incidencias:** +50 tiques creados en JIRA con pasos detallados de reproducción, logs de respuesta de API y capturas de pantalla.
* 📈 **Cobertura de Código de Pruebas:** 100% de los escenarios límites contemplados para la creación de kits.
* ✅ **Resultado del Proyecto:** La detección temprana de errores permitió corregir las fallas en la validación del backend y ajustar la interfaz, logrando desplegar una versión estable y lista para producción.

---

## 📂 Evidencias y Documentación
* 📄 **Documentación Técnica de la API (Apidoc):** [Documentación de la API Urban Grocers](https://cnt-e38aa848-027b-402d-a21d-8e926b38a46b.containerhub.tripleten-services.com/docs/)
* 📊 **Matriz de Pruebas y Checklist en Google Sheets:** [Ver Matriz de Pruebas Urban Grocers](https://docs.google.com/spreadsheets/d/1I29Hq3Yjn2_R80mP2fW6kzffuNDEyUNi/edit?usp=sharing&ouid=117662769631159222767&rtpof=true&sd=true)

---

## 📁 Estructura del Repositorio
```text
urban-grocers-api-tests/
├── data.py              # Payloads de prueba y datos de usuario/kit
├── sender_stand_request.py # Funciones para envío de solicitudes HTTP (POST/GET)
├── create_kit_name_kit_test.py # Suite de pruebas automatizadas con Pytest
├── configuration.py     # URLs base y rutas de endpoints
├── README.md            # Documentación general del proyecto
└── requirements.txt     # Dependencias del proyecto (pytest, requests)
```

### ⚙️ Instrucciones de Ejecución
1. Instalar las dependencias requeridas:
   ```bash
   pip install pytest requests
   ```
2. Ejecutar la suite completa de pruebas automatizadas:
   ```bash
   pytest
   ```

---

## 💡 Principales Aprendizajes
* 🧠 **Automatización de Pruebas de API con Python:** Creación de scripts modulares con separación de responsabilidades (configuración, datos, cliente HTTP y aserciones).
* 🔑 **Manejo de Tokens y Autenticación:** Automatización del flujo completo donde la creación de un recurso depende del token obtenido en un endpoint previo (`authToken`).
* 📐 **Análisis Crítico de Especificaciones:** Detección de brechas entre la documentación teórica de la API y el comportamiento real de los servicios backend.
* 📝 **Gestión Profesional de Incidencias:** Documentación clara de fallas en JIRA incluyendo requests, responses, headers y comportamientos esperados vs reales.

---

## 🚀 Mejoras Futuras
* ⚙️ **Integración Continua (CI/CD):** Configurar GitHub Actions o Jenkins para la ejecución automática de la suite de `pytest` en cada commit.
* 📊 **Generación de Reportes Visuales:** Implementar `Allure Report` para obtener reportes gráficos detallados de la ejecución de pruebas.
* ⚡ **Pruebas de Carga Básicas:** Incorporar scripts con Locust para evaluar la respuesta de la API bajo peticiones concurrentes.
