import json

from flask import Flask, render_template, session
from auth.route import blueprint_auth
from report.route import blueprint_report
from access import login_required


app = Flask(__name__)
app.secret_key = 'You will never guess'

app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(blueprint_report, url_prefix='/report')
#
# app.config['db_config'] = json.load(open('configs/db.json'))
# app.config['access_config'] = json.load(open('configs/access.json'))
#

@app.route('/')
@login_required
def main_menu():
    return render_template('main_menu.html')


@app.route('/exit')
def exit_func():
    if 'user_id' in session:
        session.clear()
    return render_template('exit.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
