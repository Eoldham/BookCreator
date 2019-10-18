from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField


class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')


class CharacterSheet(FlaskForm):
    name = StringField('Name')
    nickname = StringField('Nickname')
    birthday = StringField('Birthday')
    birth_place = StringField('Birth Place')
    height = StringField('Height')
    weight = StringField('Weight')
    body = StringField('Body Shape')
    eye_color = StringField('Eye Color')
    glasses = StringField('Glasses?')
    contacts = StringField('Contacts?')
    skin_tone = StringField('Skin Tone')
    freckles = StringField('Freckles?')
    moles = StringField('Moles?')
    mole_placement = StringField('Mole Placement')
    scars = StringField('Scars?')
    scar_placement = StringField('Scar Placement')
    tattoos = StringField('Tattoos')
    tattoo_placement = StringField('Tattoo Placement')
    health = StringField('Health')
    outfit = StringField('Outfit')
    hair_color = StringField('Hair Color')
    hair_texture = StringField('Hair Texture')
    hair_length = StringField('Hair Length')
    submit = SubmitField('Create Character')


class Archetype(FlaskForm):
    archetype = SelectField('Which Archetype?', choices=['A', 'B'])

class Setting(FlaskForm)
