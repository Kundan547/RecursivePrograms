import streamlit as st
import sqlite3
import hashlib

# Initialize connection to SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')

# Create products table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY, name TEXT, price REAL, description TEXT)''')

# Insert some sample products if the table is empty
c.execute('SELECT COUNT(*) FROM products')
if c.fetchone()[0] == 0:
    sample_products = [
        ('Laptop', 999.99, 'High-performance laptop'),
        ('Smartphone', 499.99, 'Latest model smartphone'),
        ('Headphones', 99.99, 'Noise-cancelling headphones'),
    ]
    c.executemany('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', sample_products)
    conn.commit()

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def add_user(username, password):
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, make_hashes(password)))
    conn.commit()

def login_user(username, password):
    c.execute('SELECT * FROM users WHERE username =?', (username,))
    data = c.fetchone()
    if data:
        return check_hashes(password, data[1])
    return False

def get_products():
    c.execute('SELECT * FROM products')
    return c.fetchall()

def main():
    st.title("Simple E-commerce App")

    menu = ["Home", "Login", "SignUp", "Shop"]
    choice = st.sidebar.selectbox("Menu", menu)

    if 'user' not in st.session_state:
        st.session_state.user = None

    if 'cart' not in st.session_state:
        st.session_state.cart = {}

    if choice == "Home":
        st.subheader("Welcome to our E-commerce Store")
        st.write("Please login to start shopping!")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')

        if st.button("Login"):
            if login_user(username, password):
                st.success("Logged In as {}".format(username))
                st.session_state.user = username
            else:
                st.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.subheader("Create New Account")

        new_user = st.text_input("Username")
        new_password = st.text_input("Password", type='password')

        if st.button("SignUp"):
            add_user(new_user, new_password)
            st.success("You have successfully created an account")
            st.info("Go to Login Menu to login")

    elif choice == "Shop":
        if st.session_state.user is None:
            st.warning("Please login to access the shop")
        else:
            st.subheader(f"Welcome to the Shop, {st.session_state.user}!")
            
            products = get_products()
            for product in products:
                col1, col2, col3 = st.columns([2,1,1])
                with col1:
                    st.write(f"**{product[1]}**")
                    st.write(product[3])
                with col2:
                    st.write(f"${product[2]:.2f}")
                with col3:
                    if st.button("Add to Cart", key=product[0]):
                        if product[0] in st.session_state.cart:
                            st.session_state.cart[product[0]] += 1
                        else:
                            st.session_state.cart[product[0]] = 1
                        st.success(f"Added {product[1]} to cart!")
            
            st.subheader("Your Cart")
            total = 0
            for product_id, quantity in st.session_state.cart.items():
                product = next((p for p in products if p[0] == product_id), None)
                if product:
                    st.write(f"{product[1]} - Quantity: {quantity} - ${product[2] * quantity:.2f}")
                    total += product[2] * quantity
            st.write(f"**Total: ${total:.2f}**")

if __name__ == '__main__':
    main()