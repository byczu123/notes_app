from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('search',__name__)

@bp.route('/search', methods=('POST','GET'))
def search_post():
    if request.method=='POST':
        postName = request.form['postName']
        error = None

        if not postName:
            error = 'Title of the post required.'

        if error is not None:
            flash(error)
        
        else:
            db = get_db()
            posts = db.execute('SELECT p.id, title, body, created, author_id, username'
            ' FROM post p JOIN user u ON p.author_id = u.id'
            ' ORDER BY created DESC'
                ).fetchall()
        return redirect(url_for('search.search_post'))
  

    return render_template('searched_posts.html', posts=posts)