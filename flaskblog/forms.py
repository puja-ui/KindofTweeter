from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken, please choose a different username.')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken, please choose a different email')

class LoginForm(FlaskForm):
    email = StringField('Email', validators= [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('LogIn')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators= [DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators= [DataRequired(), Email()])
    picture = FileField('Update profile picture', validators= [FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken, please choose a different username.')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken, please choose a different email')
#jobdae...
class jobpostingform(FlaskForm):
    companyname = StringField('Companyname', validators=[DataRequired()])
    jobtitle = StringField('Jobtitle', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    #country = SelectField('Country', 
                        #choices=[(Antarctica),(Argentina),(Australia),(Austria),(Brahrain),(Belgium),(Brazil),(Canada),(Chile),(China),(Cholombia),(Costa Rica),(Czech Republic),(Denmark),(Ecuador),(Egypt),(Finland),(France),(Germany),(Greece),(Homg Kong),(Hungary),(India),(Indonesia),(Ireland),(Israel),(Italy),(Japan),(Kuwait),(Luxembourg),(Malaysia),(Mexico),(Morocco),(netherlans),(New Zealand),(Nigeria),(Norway),(Oman),(Pakistan),(Panama),(Peru),(Philippines),(Poland),(Portugal),(Qatar),(Romania),(Russia),(Saudi Arabia),(Singapore),(South Africa),(South Korea),(Spain),(Sweden),(Switzerland),(Taiwan),(Thailand),(Turkey),(Ukraine),(United Arab Emirates),(United Kingdom),(United States),(Uruguay),(Venezuela),(Vietnam)])
    
    submit = SubmitField('submit')
    #...jobdae