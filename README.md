


# Docker file for Postgres image:
  ==============================
Dockerfile:

    FROM postgres:latest
    ENV POSTGRES_PASSWORD=password1
    ENV POSTGRES_USER=postgres
    ENV POSTGRES_DB=postgres
    COPY /docker-entrypoint-initdb.d/sql1.sql docker-entrypoint-initdb.d/sql1.sql


docker-entrypoint-initb.d:
=========================
    docker-entrypoint-initdb.d/sql1.sql

    CREATE TABLE IF NOT EXISTS userdetail (
      firstname VARCHAR(20),
      lastname  VARCHAR(20)
);




# Reference:

      postgresql://{username}:{password}@localhost:5432/{database}'.format(
                  username='postgres',
                  password='password1',
                  database='postgres'
         )
         
#requirements.txt

      flask
      flask-sqlalchemy
      psycopg2
      SQLAlchemy



#Python dockerfile:

           FROM python:latest
           WORKDIR /code
           RUN python3 -m pip install --upgrade pip
           RUN python3 -m pip install virtualenv
           RUN python3 -m venv virtual
           RUN . virtual/bin/activate
           ADD requirements.txt requirements.txt
           RUN pip install -r requirements.txt
           COPY app.py app.py
           CMD ["python", "app.py"]



#Docker compose:


        version: "3.8"
        services:
          app:
            build: ./app/
            container_name: app1
            ports:
            - 8000:5000
            links:
            - db
            networks:
            - python-postgres

          db:
            build: ./database/
            container_name: db1
            ports:
            - 5432:5432
            volumes:
            - /var/postgres/data:/var/lib/postgres/data
            networks:
            - python-postgres

      networks:
      python-postgres:
         driver : bridge
         name   : sample



# Postgres SQL:

    docker run --name db -e POSTGRES_PASSWORD=password1 -d -p 5432:5432 db:v1
    docker exec -it db bash
    psql -h 52.86.115.130 -p 5432 -U postgres
    postgres=# \l
    postgres=# \c postgres    ---to connect
    postgres=# select * from userdetail;
    
    \q to quit

# Problem is :

  docker run --name web-app --link db:db -p 8000:5000 web:v1



![image](https://user-images.githubusercontent.com/54719289/106527293-0783f200-650d-11eb-888c-99029999ee37.png)


