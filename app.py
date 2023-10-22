# Import necessary modules and classes from Flask
from flask import Flask, jsonify, request, render_template, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS

# Import forms, helper functions, and data storage modules
from forms import RegistrationForm, LoginForm
from helpers import hash_password, check_password
from data_storage import load_users, save_users

# Initialize the Flask app
app = Flask(__name__, template_folder="")
app.secret_key = "ishanoshada"

# Enable Cross-Origin Resource Sharing (CORS) for API requests
CORS(app)

# Enable Cross-Site Request Forgery (CSRF) protection
csrf = CSRFProtect(app)

# Load user data from storage
users = load_users()

# Configure Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# Define a User class for Flask-Login
class User(UserMixin):
    pass


# Callback function to load user by ID
@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.get('user_id') == user_id:
            return user
    return None


# Route for user registration
@app.route('/signup', methods=['POST'])
def signup():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Hash the password before saving it
        hashed_password = hash_password(password)

        # Append user data to the list and save it
        users.append({'id': len(users) + 1, 'username': username, 'password': hashed_password})
        save_users(users)

        return jsonify({'message': 'User created successfully'}), 201

    return jsonify({'message': 'Invalid input data'}), 400


# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data.get('username')
    password = data.get('password')

    for user in users:
        if user['username'] == username and check_password(user['password'], password):
            user_obj = User()
            user_obj.id = user['id']
            login_user(user_obj)
            return jsonify({'message': 'Login successful'})

    return jsonify({'message': 'Invalid credentials'}), 401


# Route for user logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})


# Route for the home page
@app.route('/')
def index():
    # Initialize registration and login forms
    rform = RegistrationForm()
    lform = LoginForm()

    # Render the index.html template with the forms
    return render_template('index.html', registration_form=rform, login_form=lform, template_folder="templates")


# Initialize CSRF protection
csrf.init_app(app)

# Start the Flask application
app.run()
