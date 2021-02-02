FROM postgres:11.5
USER postgres
ENV POSTGRES_HOST_AUTH_METHOD=trust
ENV POSTGRES_PASSWORD='Password1'
ENV POSTGRES_USER='postgres'
ENV POSTGRES_DB='postgres'
ADD ./docker-entrypoint-initdb.d/sql1.sql /docker-entrypoint-initdb.d/sql1.sql
