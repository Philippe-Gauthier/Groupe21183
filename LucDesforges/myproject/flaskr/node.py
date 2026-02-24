"""
Auteur : Luc Desforges
Date : 23 fevrier 2026
Description : Fichier contenant toutes les fonctionalités concernant les node et edge.
"""

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("node", __name__)

# Queries pour utiliser la BD sqlite
INDEX_QUERY = "SELECT n.id, title, body, created, author_id, username FROM node n JOIN user u ON n.author_id = u.id ORDER BY created DESC"
GET_QUERY = "SELECT n.id, title, body, created, author_id, username FROM node n JOIN user u ON n.author_id = u.id WHERE n.id = ?"
READ_QUERY = "SELECT node WHERE id = ?"
LISTOF_CHILD_QUERY = "SELECT n.title, e.child_title, parent_id, child_id FROM edge e JOIN node n ON n.id = e.child_id WHERE parent_id = :parent_id"
LISTOF_PARENT_QUERY = "SELECT n.title, e.child_title, parent_id, child_id FROM edge e JOIN node n ON n.id = e.parent_id WHERE child_id = :parent_id"

CREATE_QUERY = "INSERT INTO node (title, body, author_id) VALUES (?, ?, ?)"
UPDATE_QUERY = "UPDATE node SET title = ?, body = ? WHERE id = ?"
ADD_OPTION_QUERY = (
    "INSERT INTO edge (parent_id, child_id, child_title) VALUES (?, ?, ?)"
)

DELETE_QUERY = "DELETE FROM node WHERE id = ?"

# Erreurs de form
TITLE_FORMERROR = "Title is required."

# render_template strings (RTS)
INDEX_RTS = "node/index.html"
CREATE_RTS = "node/create.html"
UPDATE_RTS = "node/update.html"
READ_RTS = "node/read.html"

# route strings
INDEX_ROUTESTRING = "/"
CREATE_ROUTESTRING = "/create"
UPDATE_ROUTESTRING = "/<int:id>/update"
READ_ROUTESTRING = "/<int:id>/read"
ADD_OPTION_ROUTESTRING = "/<int:id>/add_option"
DELETE_ROUTESTRING = "/<int:id>/delete"

# urlFor strings (UFS)
INDEX_UFS = "node.index"
CREATE_UFS = "node.create"
UPDATE_UFS = "node.update"
READ_UFS = "node.read"

"""
Entrées: -Aucune-
Sortie: string équivalent à un string html
Description : Va chercher tous les noeuds qui existe
"""
@bp.route(INDEX_ROUTESTRING)
def index() -> str:
    listof_node = get_listof_node()
    return render_template(INDEX_RTS, listof_node = listof_node)

"""
Entrées: -Aucune-
Sortie: string équivalent à un string html
Description : Fonctionalité por créer un noeud
"""
@bp.route(CREATE_ROUTESTRING, methods = ("GET", "POST"))
@login_required
def create() -> str:
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = TITLE_FORMERROR

        if error is None:
            db = get_db()
            db.execute(CREATE_QUERY, (title, body, g.user["id"]))
            db.commit()
            return redirect(url_for(INDEX_UFS))

        flash(error)

    return render_template(CREATE_RTS)

"""
Entrées: id (identifiant du noeud)
Sortie: string équivalent à un string html
Description : Fonctionalité pour mettre à jour un noeud par id
"""
@bp.route(UPDATE_ROUTESTRING, methods = ("GET", "POST"))
@login_required
def update(id) -> str:
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = TITLE_FORMERROR

        if error is None:
            db = get_db()
            db.execute(UPDATE_QUERY, (title, body, id))
            db.commit()
            return redirect(url_for(UPDATE_UFS, id = id))

        flash(error)

    db = get_db()
    node = get_node(id, True, db)
    listof_node = get_listof_node(db)
    param = {"parent_id": id}
    listof_child = db.execute(LISTOF_CHILD_QUERY, (param)).fetchall()
    listof_parent = db.execute(LISTOF_PARENT_QUERY, (param)).fetchall()
    return render_template(
        UPDATE_RTS,
        node = node,
        listof_node = listof_node,
        listof_child = listof_child,
        parent = listof_parent[0] if listof_parent else None)


"""
Entrées: id (identifiant du noeud)
Sortie: string équivalent à un string html
Description : Fonctionalité pour afficher un noeud par id, et montrer les détails
"""
@bp.route(READ_ROUTESTRING, methods = ("GET", "POST"))
def read(id) -> str:
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = TITLE_FORMERROR

        if error is None:
            db = get_db()
            db.execute(READ_QUERY, (title, body, id))
            db.commit()
            return redirect(url_for(READ_UFS, id = id))

        flash(error)

    db = get_db()
    node = get_node(id, False, db)
    param = {"parent_id": id}
    listof_child = db.execute(LISTOF_CHILD_QUERY, (param)).fetchall()
    return render_template(READ_RTS, node = node, listof_child = listof_child)


"""
Entrées: id (identifiant du noeud)
Sortie: string équivalent à un string html
Description : Fonctionalité pour ajouter un noeud enfant par id
"""
@bp.route(ADD_OPTION_ROUTESTRING, methods = ("POST",))
@login_required
def add_option(id) -> str:
    if request.method == "POST":
        error = None

        if error is None:
            child_id = request.form.get("child_id")
            child_title = request.form["child_title"]

            db = get_db()
            db.execute(ADD_OPTION_QUERY, (id, child_id, child_title))
            db.commit()
            return redirect(url_for(UPDATE_UFS, id = id))

        flash(error)

    db = get_db()
    node_parent = get_node(id, True, db)
    listof_node = get_listof_node(db)
    return render_template(UPDATE_RTS, node = node_parent, listof_node = listof_node)


"""
Entrées: id (identifiant du noeud)
Sortie: string équivalent à un string html
Description : Fonctionalité pour supprimer un noeud par id
"""
@bp.route(DELETE_ROUTESTRING, methods = ("POST",))
@login_required
def delete(id) -> str:
    db = get_db()
    get_node(id, True, db)
    db.execute(DELETE_QUERY, (id,))
    db.commit()
    return redirect(url_for(INDEX_UFS))


"""
Entrées: -Aucune-
Sortie: Liste de noeuds
Description : Fonctionalité pour chercher tous les noeud
"""
def get_listof_node(db = None) -> list[Any]:
    if db is None:
        db = get_db()

    return db.execute(INDEX_QUERY).fetchall()


"""
Entrées: id (identifiant du noeud), optionnels: check_author (Un boolean si on veut que seulement l'auteur puisse accéder), db (Connection à la base de donnée)
Sortie: un noeud
Description : Fonctionalité pour chercher un noeud par id
"""
def get_node(id, check_author = True, db = None):
    if db is None:
        db = get_db()

    node = db.execute(GET_QUERY, (id,)).fetchone()

    if node is None:
        abort(404, f"Node id {id} doesn't exist.")

    if check_author and node["author_id"] != g.user["id"]:
        abort(403)

    return node