# inteia-challenge

## Tecnologías
- **Backend:** FastAPI
- **Server:** Uvicorn
- **DB:** PostgreSQL
- **ORM:** SQLAlchemy
- **Serialization:** Pydantic
- **Docs:** Swagger
- **Test:** Pytest
- **Containerization:** Docker

## Crear ambiente de desarrollo
1. Actualizar `.env` con variables de entorno necesarias
1. Crear ambiente virtual

    ```bash
        python3 -m venv .venv
    ```
1. Instalar dependencias

    ```bash
        pip install -r requirements.txt
    ```
1. Correr servidor de desarrollo

    ```bash
        fastapi dev app/main.py
    ```

1. Correr casos de pruebas
    ```bash
        pytest -v
    ```

## Construir y correr imagen para producción
1. Construir imagen
    ```bash
        docker build -t challenge .
    ```
1. Correr imagen
    ```bash
        # IMPORTANTE: Solo funciona en linux en MacOS y Windows hay que
        # declarar la variable de entorno POSTGRES_HOSTNAME
        docker run --network host -d -p 8000:8000 challenge
    ```
## Preguntas adicionales
1. ¿Cómo manejarías la autenticación y autorización en la API?
    - Con un protocolo como oAuth2.0, a tavés de llaves privadas
1. ¿Qué estrategias utilizarías para escalar la aplicación?
    - Verticalmente: El servicio corre en `gunicorn` que es un servidor que permite escalamiento de workers dentro de la misma instancia del programa
    - Horizontalmente: Aprovecharía que está en un `Docker` para desplegarlo en `Kubernetes` y de allí balanceadores de carga se encargan de las políticas de escalamiento entre pods

1.  ¿Cómo implementarías la paginación en los endpoints que devuelven listas de libros?
    - Existen librerías para hacer no más la paginación en el caso de fastapi, en caso contrario se tendría que hacer una clase de paginación y cambiar los modelos de respuesta para siempre incluir esos parámetros, digo que se tendría que hacer una clase en vez de manejarlo en la misma vista en orden de los principios Object Oriented.

1. ¿Cómo asegurarías la seguridad de la aplicación (protección contra inyecciones SQL, XSS, etc.)?
    - Para protección SQL estamos usando ORM, con protocolos con oAuth2.0 se garantiza permisos y autorización, utilizando protocolos seguros como HTTPS garantizamos que los datos estén encriptados, en un escenario en el que corre en un cluster asegurarse sólo las exposiciones necesarias de los puertos que tengan que comunicarse al exterior en las puertas de enlace.