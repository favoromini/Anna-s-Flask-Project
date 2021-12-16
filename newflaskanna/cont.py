from flask import Flask, render_template,request, redirect
from db import mydb, mycursor


app = Flask(__name__)


@app.route('/')
def index():
    mycursor.execute("SELECT * FROM Cloth")
    cloth = mycursor.fetchall()
    return render_template('index.html',cloth = cloth)



@app.route('/gotoadmin')
def gotoadmin():
    mycursor.execute("SELECT * FROM Cloth")
    cloth = mycursor.fetchall()
    return render_template('adminpage.html',cloth = cloth)




@app.route('/addcloth', methods=['GET', 'POST'])
def addcloth():
    if request.method == 'GET':
        return render_template('adddata.html')
    if request.method == 'POST':
          # _ = request.form['name']
        _clothname = request.form['clothname']
        _tailorname = request.form['tailorname']
        _design = request.form['design']
        _size = request.form['size']
        _price = request.form['price']
     
        sql = 'INSERT INTO Cloth(clothname,tailorname,design,size,price) VALUE (%s, %s,%s, %s,%s)'
        val = (_clothname, _tailorname,_design,_size, _price)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM Cloth")
        cloth = mycursor.fetchall()
        return render_template('index.html', cloth = cloth)






@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_cloth(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM Cloth WHERE ID={id}')
        cloth = mycursor.fetchone()
        return render_template('editdata.html', cloth = cloth)
    if request.method == 'POST':
        _clothname = request.form['clothname']
        _tailorname = request.form['tailorname']
        _design = request.form['design']
        _size = request.form['size']
        _price = request.form['price']
        sql = f'UPDATE Cloth SET clothname = %s, tailorname = %s, design = %s, size = %s, price = %s WHERE ID = %s'
        values = (_clothname, _tailorname,_design,_size, _price,id)
        mycursor.execute(sql, values)
        mycursor.execute("SELECT * FROM Cloth")
        cloth = mycursor.fetchall()
        mydb.commit()
        return render_template('index.html', cloth = cloth)





@app.route('/delete/<int:id>')
def delete_cloth(id):
    sql = f'DELETE FROM Cloth WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    mycursor.execute("SELECT * FROM Cloth")
    cloth = mycursor.fetchall()
    return render_template('index.html', cloth = cloth)







if __name__ == '__main__':
        app.run()




