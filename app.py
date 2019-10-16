from flask import Flask,render_template,redirect, url_for,request
import Character_class
from forms import SignUpForm
from forms import Character_sheet
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

character_list = []
#global list that keeps all character dictionaries created
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
    return render_template('plots.html')

@app.route('/setting')
def pick_setting():
    error = None
    if request.method == 'POST':
        name = request.form['name']

    return render_template('setting.html')

@app.route('/characters', methods = ['GET','POST'])
def characters():
    form = Character_sheet()
    if form.is_submitted():
        character = request.form
        character_list.append(character)
    return render_template('characters.html', form = form)

@app.route('/user_character')
def characters():
    return render_template('user_characters.html', character_list = character_list)

@app.route('/write')
def writing():
    return render_template('write.html')

@app.route('/signup',methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result = result)
    return render_template('signup.html', form = form)

if __name__ == '__main__':
    app.run()
