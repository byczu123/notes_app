import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

from flaskr.blog import login_required

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/<int:id>',methods=('GET','POST'))
@login_required
def index(id):
    db = get_db()
    posts = db.execute('SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE author_id = ?'
        ' ORDER BY created DESC',(id,)
        ).fetchall()

    return render_template('user.html', posts=posts)

