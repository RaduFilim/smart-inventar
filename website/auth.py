from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if (len(username) < 4) or (0 == username.count('.')):
            flash('Username invalid', category='error')
        elif len(password) < 1:
            flash('Parola invalida', category='error')
        else:
            flash('S-ar putea sa fie bine🤔', category='success')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('/sign-up')
def sign_op():
    return render_template("sign-up.html")