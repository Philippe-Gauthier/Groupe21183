from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    #originpost = [post_item for post_item in posts if post_item['id'] == id]

    #print('test'+originpost[0]['title'])

    for post_item in posts:
            print(post_item['title'])

    param = {'origin_id': id}
    choices = db.execute(
        'SELECT p.title, origin_id, destination_id'
        ' FROM choice c JOIN post p ON p.id = c.destination_id'
        ' WHERE origin_id = :origin_id',
        (param)
    ).fetchall()

    for choice_item in choices:
        print(choice_item['title'])

    fathers = db.execute(
        'SELECT p.title, origin_id, destination_id'
        ' FROM choice c JOIN post p ON p.id = c.origin_id'
        ' WHERE origin_id = :origin_id',
        (param)
    ).fetchall()

    for father_item in fathers:
        print(father_item['title'])

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.update', id=id))

    return render_template('blog/update.html', post=post, posts=posts, choices=choices, fathers=fathers)

@bp.route('/<int:id>/read', methods=('GET', 'POST'))
@login_required
def read(id):
    post = get_post(id, False)
    db = get_db()

    param = {'origin_id': id}

    choices = db.execute(
        'SELECT p.title, origin_id, destination_id'
        ' FROM choice c JOIN post p ON p.id = c.destination_id'
        ' WHERE origin_id = :origin_id',
        (param)
    ).fetchall()

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'SELECT post'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.read', id=id))

    return render_template('blog/read.html', post=post, choices=choices)

@bp.route('/<int:id>/add_option', methods=('POST',))
@login_required
def add_option(id):
    destination_id = request.form.get('destination_id')
    print("destination_id" + str(destination_id))
    post_origin = get_post(id)
    post_destination = get_post(destination_id)

    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    if request.method == 'POST':
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO choice (origin_id, destination_id)'
                ' VALUES (?, ?)',
                (id, destination_id)
            )
            db.commit()
            return redirect(url_for('blog.update', id=id))

    return render_template('blog/update.html', post=post_origin, posts=posts)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))

