from flask import Flask,render_template,redirect, url_for,request
from forms import SignUpForm
from forms import CharacterSheet
from forms import Archetype
from forms import Setting
from forms import Write
#import requests
#import urllib.request
#import time
#from bs4 import BeautifulSoup
#import wget
#import spacy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Bubbles'

COMPARE_TO_BOOKS = []
#global list that holds the comparable books
ARCHETYPE = []
#gobal list that holds the archetype variable
CHARACTER_LIST = []
#global list that keeps all character dictionaries created
SETTING= []
#global list that keeps all setting notes
BOOK = []
#global list that holds all books

@app.route('/')
def home():
    """
        This directs the user to the home page, Where you start out.
    """
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    """
        This is the login in page, when you type in admin to both fields it leads you to the secret page, otherwise it gives
        an error message.
    """
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form ['password'] != 'admin':
            error = 'Invalid credentials,. Please try again.'
        else:
            return render_template('Secret.html')
    return render_template('login.html',error = error)

@app.route('/plot_line', methods = ['GET', 'POST'])
def pick_plot():
    """
        This page is where the user decides on their plot, it lists some basic ones then gives them a place
        to write out their plot. It uses the form "archetype" and saves their input to ARCHETYPE
    """
    form = Archetype()
    archetype = request.form
    ARCHETYPE.append(archetype)
    return render_template('plots.html', form = form)

@app.route('/user_archetype')
def archetype():
    """
        This is the page where the users archetype is displayed for them.
    """
    return render_template('user_archetype.html', archetype = ARCHETYPE)

@app.route('/setting', methods = ['GET','POST'])
def pick_setting():
    """
        This is the page where the user can write their setting. It leads them through setting development
        using the form called "setting" and stores their input into SETTING
    """
    form = Setting()
    if form.is_submitted():
        setting = request.form
        SETTING.append(setting)
    return render_template('setting.html', form = form)

@app.route('/user_setting')
def setting():
    """
        This is the page where the users setting is displayed for them.
    """
    return render_template('user_setting.html', Setting = SETTING)

@app.route('/characters', methods = ['GET','POST'])
def characterSheet():
    """
        This is the page where the user is walked through character creation using the form called "character"
        Their input is stored in CHARACTER_LIST
    """
    form = CharacterSheet()
    if form.is_submitted():
        character = request.form
        CHARACTER_LIST.append(character)
    return render_template('characters.html', form = form)

@app.route('/user_character')
def characters():
    """
        This is the page where the users Characters are displayed for them.
    """
    return render_template('user_characters.html', character_list = CHARACTER_LIST)

@app.route('/write', methods = ['GET','POST'])
def writing():
    """
        This is the page where the user writes their story. They use the book form and their book is stored in BOOK
    """
    form = Write()
    if form.is_submitted():
        book = request.form
        BOOK.append(book)
    return render_template('write.html', form = form)

@app.route('/user_books')
def book():
    """
        This is the page where the users book is displayed for them.
    """
    return render_template('user_books.html', Book = BOOK)

"""
This is just something I was working on but stopped. It fits in with the Project_Gutenberg_Books directory.
But it does nothing at the moment. It was just an add on

#Children_url = 'https://www.gutenberg.org/wiki/Children%27s_Fiction_(Bookshelf)'
#children_response = requests.get(Children_url)
#nice_c_response = BeautifulSoup(children_response.text, "html.parser")
#a_tags = nice_c_response.findAll('a', class_="extiw", )
#for a_tag in nice_c_response.findAll('a', class_ = 'extiw'):
    #link = a_tag.get('href')
    #if ("ebooks" in link):
        #book_page_url = link
        #book_page = requests.get(book_page_url)
#The source code said not to scrape the website :(, so I didn't


#def compare_books():
    #nlp = spacy.load("en_core_web_sm")
    #book = BOOK[BOOK.len() - 1]
        #for item in book.items():
            #text = text + item[1]
        #user_book = nlp(text)
        #user_book.similarity(online_book)
"""


if __name__ == '__main__':
    app.run()