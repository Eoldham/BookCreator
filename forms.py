from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField


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
    archetype = TextAreaField("Write your Archetype and Design your plot!")
    submit = SubmitField('Finished Plot')

class Setting(FlaskForm):
    main_location = TextAreaField("Main Location")
    wider_geography = TextAreaField("Wider Geography")
    key_locations = TextAreaField("Key Locations")
    activities_occupations = TextAreaField("Activities and Occupations")
    natural_world = TextAreaField("The Natural World")
    real_place = StringField('Real Place')
    real_place_likes = TextAreaField("Likes")
    real_place_research = TextAreaField("Research")
    atmosphere = StringField("Atmosphere")
    time_of_day = StringField("Time of day")
    weather = TextAreaField("Weather")
    sounds = TextAreaField("Sounds")
    smells = TextAreaField("Smells")
    tastes = TextAreaField("Tastes")
    sights = TextAreaField("Sights")
    feels = TextAreaField("Feels")
    plot = TextAreaField("Plot Addition")
    character = TextAreaField("Reveal Character")
    time_period = StringField("Time Period")
    submit = SubmitField('Done With Setting')


class Write(FlaskForm):
    beginning = TextAreaField("Beginning")
    introduce_conflict = TextAreaField("Introduce Conflict")
    climax = TextAreaField("Climax")
    resolve_conflict = TextAreaField("Resolve Conflict")
    end = TextAreaField("Ending")
    submit = SubmitField("Finished Writing")
