from flask import Flask, render_template, redirect, url_for, request
import pymysql
app = Flask(__name__)

# open database connection
db = pymysql.connect("localhost", "root", "1234", "db")
# prepare a cursor object using cursor() method 
cursor = db.cursor() 
cursor.execute("DROP TABLE IF EXISTS Orders")
# Create table as per requirement
sql = "CREATE TABLE Orders (phone_num int(8) NOT NULL, name char(20) NOT NULL, pizza_type varchar(40) NOT NULL, pizza_size varchar(20) NOT NULL, pizza_quantity int NOT NULL);"
cursor.execute(sql)

@app.route("/checkout", methods = ['POST', 'GET']) 
def checkout(): 
    if request.method == 'POST': 
        order = []
        phone = request.form['num']
        name = request.form['guest']
        pizza1quantity = request.form['pizza1']
        pizza1size = request.form['pizza1size']
        pizza2quantity = request.form['pizza2']
        pizza2size = request.form['pizza2size']
        pizza3quantity = request.form['pizza3']
        pizza3size = request.form['pizza3size']
        pizza4quantity = request.form['pizza4']
        pizza4size = request.form['pizza4size']
        pizza5quantity = request.form['pizza5']
        pizza5size = request.form['pizza5size']
        pizza6quantity = request.form['pizza6']
        pizza6size = request.form['pizza6size']
        
        #Adding pizza favors
        if(pizza1quantity != "0"):
            order.append("Hawaiian Pizza")
            order.append(pizza1size)
            order.append(pizza1quantity)
            sql = "INSERT INTO Orders (phone_num, name, pizza_type, pizza_size, pizza_quantity) VALUES ('%s', '%s', '%s', '%s', '%s')" % (phone, name, 'Hawaiian Pizza', pizza1size, pizza1quantity)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if(pizza2quantity != "0"):
            order.append("Four Cheese Lover")
            order.append(pizza2size)
            order.append(pizza2quantity)
            sql = "INSERT INTO Orders (phone_num, name, pizza_type, pizza_size, pizza_quantity) VALUES ('%s', '%s', '%s', '%s', '%s')" % (phone, name, 'Four Cheese Lover', pizza2size, pizza2quantity)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if(pizza3quantity != "0"):
            order.append("Home Special Pizza")
            order.append(pizza3size)
            order.append(pizza3quantity)
            sql = "INSERT INTO Orders (phone_num, name, pizza_type, pizza_size, pizza_quantity) VALUES ('%s', '%s', '%s', '%s', '%s')" % (phone, name, 'Home Special Pizza', pizza3size, pizza3quantity)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if(pizza4quantity != "0"):
            order.append("Vegetarian Pizza")
            order.append(pizza4size)
            order.append(pizza4quantity)
            sql = "INSERT INTO Orders (phone_num, name, pizza_type, pizza_size, pizza_quantity) VALUES ('%s', '%s', '%s', '%s', '%s')" % (phone, name, 'Vegetarian Pizza', pizza4size, pizza4quantity)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if(pizza5quantity != "0"):
            order.append("Killer Bee Pizza")
            order.append(pizza5size)
            order.append(pizza5quantity)
            sql = "INSERT INTO Orders (phone_num, name, pizza_type, pizza_size, pizza_quantity) VALUES ('%s', '%s', '%s', '%s', '%s')" % (phone, name, 'Killer Bee Pizza', pizza5size, pizza5quantity)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if(pizza6quantity != "0"):
            order.append("Carbonara Pizza")
            order.append(pizza6size)
            order.append(pizza6quantity)
            sql = "INSERT INTO Orders (phone_num, name, pizza_type, pizza_size, pizza_quantity) VALUES ('%s', '%s', '%s', '%s', '%s')" % (phone, name, 'Carbonara Pizza', pizza6size, pizza6quantity)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

        return render_template('checkout.html', order = order, phone = phone, name = name)
    else:
        return redirect(url_for('about'))

@app.route("/login", methods = ['POST', 'GET']) 
def login(): 
    if request.method == 'POST': 
        user = request.form['username']
        phone = request.form['phone'] 
        if user == "Admin" and phone == "22222222": 
            return redirect(url_for('admin_login', name = user))
        else:
            return redirect(url_for('customer', guest = user, phone = phone))
    else:
        user = request.args.get('username') 
        return redirect(url_for('about'))

@app.route("/admin/<name>") 
def admin_login(name): 
    cursor.execute("SELECT * FROM Orders")
    data = cursor.fetchall()
    return render_template('staff.html', data=data)

@app.route("/menu/<guest>/<phone>") 
def customer(guest, phone):
    return render_template('menu.html', guest = guest, phone = phone)

@app.route('/')
def log():
    return render_template('login.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8000)