from flask import Flask,render_template,redirect, url_for,request
from forms import SignUpForm
from forms import CharacterSheet
from forms import Archetype
from forms import Setting
from forms import Write
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

ARCHETYPE = ''
#gobal string that holds the archetype variable
CHARACTER_LIST = []
#global list that keeps all character dictionaries created
SETTING= []
#global list that keeps all setting notes
BOOK = []
#global list that holds all books
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form ['password'] != 'admin':
            error = 'Invalid credentials,. Please try again.'
        else:
            return redirect(url_for('/user_home'))
    return render_template('login.html',error = error)

@app.route('/plot_line')
def pick_plot():
    form = Archetype
    archetype = request.form
    ARCHETYPE = archetype
    return render_template('plots.html', form = form)

@app.route('/setting', methods = ['GET','POST'])
def pick_setting():
    form = Setting()
    if form.is_submitted():
        setting = request.form
        SETTING.append(setting)
    return render_template('setting.html', form = form)

@app.route('/user_setting')
def setting():
    return render_template('user_setting.html', Setting = SETTING)

@app.route('/characters', methods = ['GET','POST'])
def characterSheet():
    form = CharacterSheet()
    if form.is_submitted():
        character = request.form
        print(character)
        CHARACTER_LIST.append(character)
        print(CHARACTER_LIST)
    return render_template('characters.html', form = form)

@app.route('/user_character')
def characters():
    return render_template('user_characters.html', character_list = CHARACTER_LIST)

@app.route('/write', methods = ['GET','POST'])
def writing():
    form = Write()
    if form.is_submitted():
        book = request.form
        BOOK.append(book)
    return render_template('write.html', form = form)

@app.route('/user_books')
def book():
    return render_template('user_books.html', Book = BOOK)

@app.route('/signup',methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result = result)
    return render_template('signup.html', form = form)

if __name__ == '__main__':
    app.run()
