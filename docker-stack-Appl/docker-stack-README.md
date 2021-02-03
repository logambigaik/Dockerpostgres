
# While running docker stack deploy, give the stack name as webapp, so that image will created as webapp_mydb.

        

        #Establishing the connection
        conn = psycopg2.connect(
        database='flaskdb', user='flaskdb', password='Password1', host='webapp_mydb', port= '5432'
        )

@@@@app.py

![image](https://user-images.githubusercontent.com/54719289/106822023-4dbf8980-66a4-11eb-881b-622a01feac93.png)

@@@ docker hub -After pushing into docker hub:

![image](https://user-images.githubusercontent.com/54719289/106822138-91b28e80-66a4-11eb-9f25-2d0c728967c5.png)


@@@docker stack deploy:

![image](https://user-images.githubusercontent.com/54719289/106822236-c292c380-66a4-11eb-92ce-630a0028d9c8.png)


@@@output-POST
![image](https://user-images.githubusercontent.com/54719289/106822342-fd94f700-66a4-11eb-9eb9-305b90178c4e.png)


@@@output:-GET

![image](https://user-images.githubusercontent.com/54719289/106822271-d807ed80-66a4-11eb-8e0a-d2d741fdfe62.png)

