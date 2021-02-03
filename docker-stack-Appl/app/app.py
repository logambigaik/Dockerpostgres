from flask import Flask, request, render_template,jsonify
import psycopg2


#Establishing the connection
conn = psycopg2.connect(
   database='flaskdb', user='flaskdb', password='Password1', host='webapp_mydb', port= '5432'
)


app=Flask(__name__)

db = conn.cursor()

print("Successfully connectedwith postgres")

db.execute("CREATE TABLE IF NOT EXISTS userdetail(empno integer,empname VARCHAR(20),design VARCHAR(20),salary real)")

conn.commit()

print("Table is created succesffuly")


#app=Flask(__name__)

@app.route("/",methods=['POST','GET'])
def index():
    if request.method == "POST":
        details = request.form
        empno   = int(details['empno'])
        empname = str(details['ename'])
        design  = str(details['desig'])
        salary  = int(details['salary'])
        db.execute("INSERT INTO userdetail(empno,empname,design,salary) VALUES (%s,%s,%s,%s)",(int(empno),empname,design,float(salary)))
        #db.execute(sql1,[empno,empname,design,salary])
        print("Inserted value into table")
        conn.commit()

        #get_row="SELECT * FROM userdetail WHERE empno=%s"
        db.execute("SELECT * FROM userdetail WHERE empno=%s",[empno])
        result=[]
        for row in db.fetchall():
            obj={
                 "empno":row[0],
                 "empname":row[1],
                 "design":row[2],
                 "salary":row[3]

               }

            result.append(obj)

        response = jsonify(result)
        response.status_code=200

        return(response)
    return render_template('index.html')

@app.route('/listallemp',methods=['GET'])
def listallemp():
    if request.method == "GET":
        db.execute("SELECT * FROM userdetail")
        result=db.fetchall();
        return render_template('list.html',result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
