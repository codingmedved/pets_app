Pets app with CRUD for pets via Djnago admin interface and API (Django Rest Framework)
Time for creation and testing: 1 hour 30 minutes


Pets can be viewed via Django admin interface and via API.
Admin has access to all pets, a user has access only to his own pets.
An admin has to create a user and provide login and password for pet owner to allow him to login to app
(both to Django admin and via API).

Login to admin url is http://localhost:8003/admin


To obtain access token for user send POST request to http://localhost:8003/api/v1/login/  with following bod format:
{"username": "some_username", "password": "some_password"}
Having a token include it to Header of any API request: Authorization: Token PUT_YOUR_TOKEN_HERE
To see all pets - send a request here:
http://localhost:8003/api/v1/pets/

To create a new pet send POST request here http://localhost:8003/api/v1/pets/ with such body format as an example:
{
"name": "Doge1",
"birthday": "2017-10-24",
"animal_kind": "dog"
}



