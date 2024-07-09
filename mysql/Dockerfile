FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=marketing_db

COPY marketing_db.sql /docker-entrypoint-initdb.d/