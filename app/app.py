from flask import Flask, request, render_template,jsonify
import psycopg2


#Establishing the connection
conn = psycopg2.connect(
   database="postgres", user='loga', password='Password1', host='db', port= '5432'
)


app=Flask(__name__)

db = conn.cursor()

print("Successfully connectedwith postgres")

db.execute("CREATE TABLE IF NOT EXISTS userdetail(firstname VARCHAR(20),lastname VARCHAR(20))")

conn.commit()

print("Table is created succesffuly")


#app=Flask(__name__)

@app.route("/",methods=['POST','GET'])

def index():
    if request.method == "POST":
        print('Hi')
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        sql1="INSERT INTO userdetail(firstname,lastname) VALUES (%s,%s)"
        db.execute(sql1,[firstName,lastName])
        print("Inserted value into table")
        conn.commit()
        sql2="SELECT * FROM userdetail WHERE firstname=%s AND lastname=%s"
        db.execute(sql2,[firstName,lastName])
        print(db.fetchall())
        #conn.close()

        get_row="SELECT * FROM userdetail WHERE firstname=%s and lastname=%s"
        db.execute(get_row,[firstName,lastName])
        result=[]
        for row in db.fetchall():
            print(row[0])

            obj={
                 "firstname":row[0],
                 "lastname":row[1]
               }

            result.append(obj)
 
        response = jsonify(result)
        response.status_code=200
        return(response)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
