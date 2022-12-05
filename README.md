## Description

An Online Cinema API Micro Service written on FastAPI and covered with
functional tests. The application requests Elasticsearch for information about
movies, genres, and film crew members. Requesting allows parametrization.
Responses are cached with aioredis.

The code follows the SOLID and REST API principles. The micro service is
covered with functional tests written with pytest and factory-boy. The testing
environment is separated from the micro service itself by inheriting its image
in Docker Compose.

## Authors

* [Alexander Oorzhak](https://github.com/Oorzhakau)
* [Vitaly Shchurov](https://github.com/erlido)

## Technologies:

* FastAPI;
* Elasticsearch;
* pytest;
* aioredis;
* Docker Compose;
* Nginx.

## Setup (database data is not present in the repository):

1. Clone the repository.

2. Create an '.env' file based on '.env.example'. Change <PWD> for the database
   volume. Change other values, if needed.

3. Run the following command from the project directory (after starting, the
   app will automatically begin transferring data from PostgreSQL to
   Elasticsearch. This may take a little while, the logs will be printed to
   stdout):

   ```
   docker-compose -f docker-compose.yml up --build
   ```

   To run without the application, type:

   ```
   docker-compose -f docker-compose.dev.yml up --build
   ```

4. OpenApi documentation is available at `http://127.0.0.1/api/openapi#/`.

