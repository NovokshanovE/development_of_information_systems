import os
from typing import Optional, Dict

from flask import (
    Blueprint, request,
    render_template, current_app,
    session, redirect, url_for
)

#from database.operations import select
#from database.sql_provider import SQLProvider


blueprint_auth = Blueprint('blueprint_auth', __name__, template_folder='templates')

@blueprint_auth.route('/', methods=['GET', 'POST'])
def start_auth():
    session['user_id'] = 1
    session['user_group'] = 'manager'
    return render_template('auth.html')

