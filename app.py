from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Database configuration
db_config = {
    'host': 'db',  # Replace with your database VM's IP
    'user': 'ecommerce_user',  # Replace with your database username
    'password': 'DancingCheetah821&',  # Replace with your database password
    'database': 'ecommerce_db'  # Replace with your database name
}

# Function to get a database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# View Products
@app.route('/products')
def view_products():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('products.html', products=products)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# Add Product
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        manufacturer = request.form['manufacturer']
        price = float(request.form['price'])
        inventory = int(request.form['inventory'])

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO products (name, description, manufacturer_name, price, inventory_count) VALUES (%s, %s, %s, %s, %s)",
                (name, description, manufacturer, price, inventory)
            )
            conn.commit()
            flash('Product added successfully!', 'success')
        except mysql.connector.Error as err:
            flash(f'Error: {err}', 'error')
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('view_products'))

    return render_template('add_product.html')

# View Users
@app.route('/users')
def view_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('view_user.html', users=users)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# Add User
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        preferences = request.form['preferences']

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, password, email, preferences) VALUES (%s, %s, %s, %s)",
                (username, password, email, preferences)
            )
            conn.commit()
            flash('User added successfully!', 'success')
        except mysql.connector.Error as err:
            flash(f'Error: {err}', 'error')
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('index'))

    return render_template('add_user.html')

# View Purchases
@app.route('/purchases')
def view_purchases():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products_bought")
        purchases = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('view_purchases.html', purchases=purchases)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
# Add Purchase
@app.route('/add_purchase', methods=['GET', 'POST'])
def add_purchase():
    if request.method == 'POST':
        user_id = int(request.form['user_id'])
        product_id = int(request.form['product_id'])
        username = request.form['username']
        product_name = request.form['product_name']
        quantity = int(request.form['quantity'])
        date_of_purchase = request.form['date_of_purchase']

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO products_bought (user_id, product_id, username, product_name, quantity, date_of_purchase) VALUES (%s, %s, %s, %s, %s, %s)",
                (user_id, product_id, username, product_name, quantity, date_of_purchase)
            )
            conn.commit()
            flash('Purchase added successfully!', 'success')
        except mysql.connector.Error as err:
            flash(f'Error: {err}', 'error')
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('index'))

    return render_template('add_purchase.html')
# Delete User by User ID
@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            conn.commit()
            flash('User deleted successfully!', 'success')
        except mysql.connector.Error as err:
            flash(f'Error: {err}', 'error')
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('view_users'))

    return render_template('confirm_delete.html', id=user_id, type='user')

# Delete Product by Product ID
@app.route('/delete_product/<int:product_id>', methods=['GET', 'POST'])
def delete_product(product_id):
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
            conn.commit()
            flash('Product deleted successfully!', 'success')
        except mysql.connector.Error as err:
            flash(f'Error: {err}', 'error')
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('view_products'))

    return render_template('confirm_delete.html', id=product_id, type='product')
# Delete Purchase by Purchase ID
@app.route('/delete_purchase/<int:purchase_id>', methods=['GET', 'POST'])
def delete_purchase(purchase_id):
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM products_bought WHERE purchase_id = %s", (purchase_id,))
            conn.commit()
            flash('Purchase deleted successfully!', 'success')
        except mysql.connector.Error as err:
            flash(f'Error: {err}', 'error')
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('view_purchases'))

    return render_template('confirm_delete.html', id=purchase_id, type='purchase')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

