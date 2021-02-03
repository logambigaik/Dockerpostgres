FROM postgres:11.5
ENV POSTGRES_HOST_AUTH_METHOD=trust
ENV POSTGRES_USERNAME='flaskdb'
ENV POSTGRES_PASSWORD='Password1'
COPY ./docker-entrypoint-initdb.d/sql1.sql docker-entrypoint-initdb.d/sql1.sql
