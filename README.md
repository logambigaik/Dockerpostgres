


# Docker file for Postgres image:
  ==============================

Dockerfile:

    FROM postgres:11.5
    ENV POSTGRES_HOST_AUTH_METHOD=trust
    ENV POSTGRES_USERNAME='flaskdb'
    ENV POSTGRES_PASSWORD='Password1'
    COPY ./docker-entrypoint-initdb.d/sql1.sql docker-entrypoint-initdb.d/sql1.sql


docker-entrypoint-initb.d:
=========================


    CREATE USER flaskdb WITH ENCRYPTED PASSWORD 'Password1';
    CREATE DATABASE flaskdb;
    GRANT ALL PRIVILEGES ON DATABASE flaskdb TO flaskdb;






# Reference:

            #Establishing the connection
              conn = psycopg2.connect(
                    database='flaskdb', user='flaskdb', password='Password1', host='mydb', port= '5432'
              )

            # Note : host is db-container name not localhost or 127.0.0.1 in docker
         
#requirements.txt

      flask
      psycopg2
      



# Python dockerfile:

          @@ With Virtual
          
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
          
          @@ Another one without virtual:
          
          FROM python:latest
          WORKDIR /code
          ADD requirements.txt requirements.txt
          RUN pip install -r requirements.txt
          COPY app.py app.py
          COPY templates/    templates/
          CMD ["python", "app.py"]

 
# Docker compose:

          version: "3.8"
          services:
          app:
            image: web:v1
            container_name: app
            ports:
            - 5000:5000
            links:
            - db
            networks:
            - python-postgres

          db:
            image: mydb:v1
            container_name: mydb
            restart: always
            ports:
            - 5432:5432
            environment:
            - POSTGRES_HOST_AUTH_METHOD=trust
            - PGDATA='/var/lib/postgresql/data'
            volumes:
            - /var/postgres/data:/var/lib/postgres/data
            networks:
            - python-postgres

          networks:
          python-postgres:
             driver : bridge
              name: python-postgres
 
 
       
    @@@Docker-compose file:
![image](https://user-images.githubusercontent.com/54719289/106786604-bdb61b80-6674-11eb-9635-4351d52da726.png)


    @@@mydb log after docker-compose up:
![image](https://user-images.githubusercontent.com/54719289/106785508-78451e80-6673-11eb-9fe3-840d59611b17.png)

    @@@mydb-docker-compose up:
![image](https://user-images.githubusercontent.com/54719289/106785651-a165af00-6673-11eb-87cc-4715526c0152.png)

    @@@Browser
![image](https://user-images.githubusercontent.com/54719289/106787199-6f554c80-6675-11eb-8dcd-bc63b9f382a8.png)

 
     ######################################################################################################
     ##  NOTES
     ######################################################################################################
     
     # Postgres SQL:   

    docker run --name db -e POSTGRES_PASSWORD=Password1 -d -p 5432:5432 db:v1
    docker exec -it db bash
    psql -U flaskdb
    postgres=# \l
    postgres=# \c flaskdb   ---to connect
    postgres=# select * from userdetail;
    
    \q to quit

      #In case connection refuse in local:
          1. Modify two configure files
              # vi /var/lib/pgsql/data/postgresql.conf
                Replace the line:
                listen_addresses = 'localhost'  -> listen_addresses = '*'


          2. Modify two configure files
              # vi /var/lib/pgsql/data/postgresql.conf
              Replaced the line:
              listen_addresses = 'localhost'  -> listen_addresses = '*'
              
              # vi /var/lib/pgsql/data/pg_hba.conf
               Add the line at the very end:
              host all all 0.0.0.0/0 trust
              (If IPv6: host all all ::/0 trust) 
      
          3. Restart the database service
              # service postgresql restart

#### pg_dump:

          docker exec container-name pg_dump -U db_user dbname > dbdump_file
          docker exec mydb pg_dump -U flaskdb flaskdb > 2.sql
          
![image](https://user-images.githubusercontent.com/54719289/107149160-21925a00-697d-11eb-83d9-0e1ab59c7eea.png)


      docker exec mydb pg_dump -U flaskdb flaskdb | gzip > 2.gz

![image](https://user-images.githubusercontent.com/54719289/107150195-af247880-6982-11eb-8491-15d4f3a9e15a.png)

      unzip with : gzip -d 2.gz

![image](https://user-images.githubusercontent.com/54719289/107150335-530e2400-6983-11eb-9918-876e13dfbfe0.png)
![image](https://user-images.githubusercontent.com/54719289/107150353-68834e00-6983-11eb-91cc-2994359fdc7c.png)


  
  
  
  
  
  
  
 

