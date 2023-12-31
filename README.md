# 🌟 Flask Authentication App 🌟


![GitHub contributors](https://img.shields.io/github/contributors/Ishanoshada/flask-auth-app)
![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)
![Flask Version](https://img.shields.io/badge/flask-orange.svg)

Welcome to the Flask Authentication App! This app empowers users to register and log in with ease. It incorporates advanced features like password hashing and CSRF protection for enhanced security.

## 🚀 Get Started!

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python app.py
```

## 📁 File Structure

```bash
.
├── app.py
├── data_storage.py
├── forms.py
├── helpers.py
├── static
│   └── style.css
├── templates
│   └── index.html
└── users.json
```

## 🧐 Code Breakdown

- `app.py`: Contains the main Flask application code, including routes for registration, login, and logout.

- `data_storage.py`: Manages the storage of user data. Supports both JSON and MongoDB as data storage methods.

- `forms.py`: Defines WTForms for user registration and login.

- `helpers.py`: Provides functions for hashing and checking passwords.

- `static/style.css`: Contains the CSS styling for the application.

- `templates/index.html`: The HTML file for the user interface.

- `users.json`: JSON file used to store user data when using JSON as the data storage method.

## 🔮 Future Plans

We have exciting plans for the future! Expect features like email verification and account recovery to be added soon.

## 💽 Database Choices

1. **JSON**: Quick and easy setup, perfect for smaller applications. Data is stored in a JSON file (`users.json`).

2. **MongoDB**: Offers scalability and robust querying capabilities. Requires a MongoDB instance to be running.



**Repository Views** ![Views](https://profile-counter.glitch.me/flaskaluthappish/count.svg)

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Acknowledgments

- Thanks to the Flask and MongoDB communities for providing excellent resources and documentation.
- Inspiration for this project came from the need for a simple and secure real-time chat application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---

🎉 Bravo! You're now ready to showcase your Flask Authentication App on GitHub. Feel free to explore and contribute to this exciting project! 🚀
