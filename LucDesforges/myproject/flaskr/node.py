"""
Auteur : Luc Desforges
Date : 23 fevrier 2026
Description : Fichier contenant toutes les fonctionalités concernant les node et edge.
""" 
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('node', __name__)

#Queries pour utiliser la BD sqlite
indexQuery = 'SELECT n.id, title, body, created, author_id, username FROM node n JOIN user u ON n.author_id = u.id ORDER BY created DESC'
getQuery = 'SELECT n.id, title, body, created, author_id, username FROM node n JOIN user u ON n.author_id = u.id WHERE n.id = ?'
readQuery = 'SELECT node WHERE id = ?'
listOfChildQuery = 'SELECT n.title, e.child_title, parent_id, child_id FROM edge e JOIN node n ON n.id = e.child_id WHERE parent_id = :parent_id'
listOfParentQuery = 'SELECT n.title, e.child_title, parent_id, child_id FROM edge e JOIN node n ON n.id = e.parent_id WHERE child_id = :parent_id'

createQuery = 'INSERT INTO node (title, body, author_id) VALUES (?, ?, ?)'
updateQuery = 'UPDATE node SET title = ?, body = ? WHERE id = ?'
addOptionQuery = 'INSERT INTO edge (parent_id, child_id, child_title) VALUES (?, ?, ?)'

deleteQuery = 'DELETE FROM node WHERE id = ?'

#Erreurs de form
titleFormError = 'Title is required.'

#render_template strings (RTS)
indexRTS= 'node/index.html'
createRTS = 'node/create.html'
updateRTS = 'node/update.html'
readRTS = 'node/read.html'

#route strings
indexRouteString = '/'
createRouteString = '/create'
updateRouteString = '/<int:id>/update'
readRouteString = '/<int:id>/read'
addOptionRouteString = '/<int:id>/add_option'
deleteRouteString = '/<int:id>/delete'

#urlFor strings (UFS)
indexUFS= 'node.index'
createUFS = 'node.create'
updateUFS = 'node.update'
readUFS = 'node.read'

"""
Entrées: -Aucune-
Sortie: string équivalent à un string html
Description : Va chercher tous les noeuds qui existe
""" 
@bp.route(indexRouteString)
def index() -> str:
    listOfNode = get_listOfNode()
    return render_template(indexRTS, listOfNode=listOfNode)

"""
Entrées: -Aucune-
Sortie: string équivalent à un string html
Description : Fonctionalité por créer un noeud
"""
@bp.route(createRouteString, methods=('GET', 'POST'))
@login_required
def create() -> str:
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = titleFormError

        if error is None:
            db = get_db()
            db.execute(createQuery, (title, body, g.user['id']))
            db.commit()
            return redirect(url_for(indexUFS))
        
        flash(error)
            
    return render_template(createRTS)

"""
Entrées: id (identifiant du noeud)
Sortie: string équivalent à un string html
Description : Fonctionalité pour mettre à jour un noeud par id
"""
@bp.route(updateRouteString, methods=('GET', 'POST'))
@login_required
def update(id) -> str:
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = titleFormError

        if error is None:
            db = get_db()
            db.execute(updateQuery, (title, body, id))
            db.commit()
            return redirect(url_for(updateUFS, id=id))
        
        flash(error)

    db = get_db()
    node = get_node(id, True, db)
    listOfNode = get_listOfNode(db)
    param = {'parent_id': id}
    listOfChild = db.execute(listOfChildQuery, (param)).fetchall()
    listOfParent = db.execute(listOfParentQuery, (param)).fetchall()
    return render_template(updateRTS, node=node, listOfNode=listOfNode, listOfChild=listOfChild, parent=listOfParent[0] if listOfParent else None )

"""
Entrées: id (identifiant du noeud)
Sortie: string équivalent à un string html
Description : Fonctionalité pour afficher un noeud par id, et montrer les détails
"""
@bp.route(readRouteString, methods=('GET', 'POST'))
@login_required
def read(id) -> str:
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = titleFormError

        if error is None:
            db = get_db()
            db.execute(readQuery, (title, body, id))
            db.commit()
            return redirect(url_for(readUFS, id=id))
        
        flash(error)
        
    db = get_db()
    node = get_node(id, False, db)
    param = {'parent_id': id}
    listOfChild = db.execute(listOfChildQuery, (param)).fetchall()
    return render_template(readRTS, node=node, listOfChild=listOfChild)

"""
Entrées: id (identifiant du noeud)
Sortie: string équivalent à un string html
Description : Fonctionalité pour ajouter un noeud enfant par id
"""
@bp.route(addOptionRouteString, methods=('POST',))
@login_required
def add_option(id) -> str:
    if request.method == 'POST':
        error = None

        if error is None:
            child_id = request.form.get('child_id')
            child_title = request.form['child_title']

            db = get_db()
            db.execute(addOptionQuery, (id, child_id, child_title))
            db.commit()
            return redirect(url_for(updateUFS, id=id))
        
        flash(error)

    db = get_db()
    node_parent = get_node(id, True, db)
    listOfNode = get_listOfNode(db)
    return render_template(updateRTS, node=node_parent, listOfNode=listOfNode, addOptionQuery=addOptionQuery)

"""
Entrées: id (identifiant du noeud)
Sortie: string équivalent à un string html
Description : Fonctionalité pour supprimer un noeud par id
"""
@bp.route(deleteRouteString, methods=('POST',))
@login_required
def delete(id) -> str:
    db = get_db()
    get_node(id, True, db)
    db.execute(deleteQuery, (id,))
    db.commit()
    return redirect(url_for(indexUFS))

"""
Entrées: -Aucune-
Sortie: Liste de noeuds
Description : Fonctionalité pour chercher tous les noeud
"""
def get_listOfNode(db=None) -> list[Any]:
    if(db is None):
        db = get_db()

    return db.execute(indexQuery).fetchall()

"""
Entrées: id (identifiant du noeud), optionnels: check_author (Un boolean si on veut que seulement l'auteur puisse accéder), db (Connection à la base de donnée)
Sortie: un noeud
Description : Fonctionalité pour chercher un noeud par id
"""
def get_node(id, check_author = True, db = None):
    if(db is None):
        db = get_db()

    node = db.execute(getQuery, (id,)).fetchone()

    if node is None:
        abort(404, f"Node id {id} doesn't exist.")

    if check_author and node['author_id'] != g.user['id']:
        abort(403)

    return node