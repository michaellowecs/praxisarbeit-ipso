Tenant Management
-----------------
________________________________________
Details und benötigte Ressourcen
- Flask app
- postgres db
- docker

Clone und ausführen
```
docker-compose build
docker-compose up
```

Datenbank erstellen
```
docker-compose exec web flask db upgrade
```
Quellen
Microsoft Dokumentation	https://docs.microsoft.com/en-us/

Docker Dokumenation	https://docs.docker.com/

Allgemeine Infos zu Docker, Flask und Postgres Datenbank	https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/


