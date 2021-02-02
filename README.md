


# Docker file for Postgres image:
  ==============================
Dockerfile:

    FROM postgres:11.5
    USER postgres
    ENV POSTGRES_HOST_AUTH_METHOD=trust
    ENV POSTGRES_PASSWORD='Password1'
    ENV POSTGRES_USER='loga'
    ENV POSTGRES_DB='postgres'
    WORKDIR  /var/lib/postgresql/data
    ADD ./docker-entrypoint-initdb.d/sql1.sql mydata/docker-entrypoint-initdb.d/sql1.sql
    ENV PGDATA=/var/lib/postgresql/data/mydata

docker-entrypoint-initb.d:
=========================
    CREATE USER loga WITH ENCRYPTED PASSWORD 'Password1';
    GRANT ALL PRIVILEGES ON DATABASE postgres TO loga;
    CREATE TABLE IF NOT EXISTS userdetail (
      firstname VARCHAR(20),
      lastname  VARCHAR(20)
    );





# Reference:

     conn = psycopg2.connect(
     database="postgres", user='loga', password='Password1', host='db', port= '5432'
)
    # Note : host is db-container name not localhost or 127.0.0.1 in docker
         
#requirements.txt

      flask
      psycopg2
      



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
          COPY templates/index.html  templates/index.html
          CMD ["python", "app.py"]
 
# Docker compose:

![image](https://user-images.githubusercontent.com/54719289/106668306-1f707a00-65d0-11eb-95e4-26422be7d68f.png)

    
# Postgres SQL:   

    docker run --name db -e POSTGRES_PASSWORD=Password1 -d -p 5432:5432 db:v1
    docker exec -it db bash
    psql -h 3.239.59.57 -p 5432 -U postgres
    postgres=# \l
    postgres=# \c postgres    ---to connect
    postgres=# select * from userdetail;
    
    \q to quit


    1. Modify two configure files
# vi /var/lib/pgsql/data/postgresql.conf
 Replace the line:
listen_addresses = 'localhost'  -> listen_addresses = '*'




1. Modify two configure files
# vi /var/lib/pgsql/data/postgresql.conf
 Replaced the line:
listen_addresses = 'localhost'  -> listen_addresses = '*'
# vi /var/lib/pgsql/data/pg_hba.conf
 Add the line at the very end:
host all all 0.0.0.0/0 trust
(If IPv6:
host all all ::/0 trust) 
2. Restart the database service
# service postgresql restart
3. Disable the firewall
# rcSuSEfirewall2 stop
# chkconfig SuSEfirewall2 off
# chkconfig SuSEfirewall2_init off



3.239.59.57

psql -h 3.239.59.57 -p 5432 -U postgres

# Docker run:

    After docker build
    docker images
    
    chown postgres:postgres docker-entrypoint-initdb.d/sql1.sql

    docker run --name=db -e POSTGRES_HOST_AUTH_METHOD=trust -e PGDATA=docker-entrypoint-initdb.d/sql1.sql db:v1
    docker run --name web --link db:db -p 5000:5000 web:v1



![image](https://user-images.githubusercontent.com/54719289/106667435-ee437a00-65ce-11eb-9918-cf98223dae2b.png)

# Docker compose failed in web in connectivity:

![image](https://user-images.githubusercontent.com/54719289/106669775-28624b00-65d2-11eb-9993-08eae2fab0b7.png)


