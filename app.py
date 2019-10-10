from flask import Flask,render_template,redirect, url_for,request


app = Flask(__name__)

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
    return render_template('setting.html')

@app.route('/characters')
def characters():
    return render_template('characters.html')

@app.route('/write')
def writing():
    return render_template('write.html')



if __name__ == '__main__':
    app.run()
