# Rest Flask Cookiecutter

## How To Use

1. install [cookiecutter](https://github.com/audreyr/cookiecutter):

   ```shell
   $ pip install --user cookiecutter
   ```

   or any way supported by the documentation.

2. create scaffold:

   ```shell
   $ cookiecutter https://github.com/MisLink/rest-flask-cookiecutter.git
   ```

3. install [poetry](https://github.com/sdispater/poetry):

   ```shell
   $ curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
   ```

   or any way supported by the documentation.

4. install dependencies:

   ```shell
   $ poetry install
   ```

5. then it's ready to run:

   ```shell
   $ flask run
   ```

6. a status api is equipped:

   ```shell
   $ flask routes
   Endpoint    Methods  Rule
   ----------  -------  -----------------------
   api.status  GET      /api/1.0/status
   static      GET      /static/<path:filename>
   ```

## To-Do

- [ ] write request log
- [ ] improve atomic
- and so on...
