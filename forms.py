from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

# Registration Form
class RegistrationForm(FlaskForm):
    # Username field, with validators for data presence and length constraints
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    
    # Password field, with validators for data presence and length constraints
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    
    # Confirm Password field, with validators for data presence and equality to 'password'
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    
    # Submit button for form submission
    submit = SubmitField('Sign Up')

# Login Form
class LoginForm(FlaskForm):
    # Username field, with validators for data presence and length constraints
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    
    # Password field, with validator for data presence
    password = PasswordField('Password', validators=[DataRequired()])
    
    # Submit button for form submission
    submit = SubmitField('Login')
  
