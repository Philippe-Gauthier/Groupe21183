<p align="center"> 
  <img src="https://cegepsherbrooke.qc.ca/wp-content/themes/cegepsherbrooke.qc.ca/dist/images/logo.svg" alt="cegepsherbrooke Logo" width="80px" height="80px">
</p>
<h1 align="center"> Renaissance Arthropode </h1>
<h3 align="center"> 243-224-SH PROGRAMMATION 1</h3>
<h5 align="center"> Projet 1 - <a href="https://cegepsherbrooke.qc.ca/">Cegep de Sherbrooke</a> (Hivers 2026) </h5>

<!-- TABLE OF CONTENTS -->
<h2 id="table-of-contents">Table des matières</h2>

<details open="open">
  <summary>Table des matières</summary>
  <ol>
    <li><a href="#overview"> ➤ Sommaire</a></li>
    <li><a href="#project-files-description"> ➤ Description de l'hierarchie des fichiers</a></li>
    <li><a href="#getting-started"> ➤ Pour commencer</a></li>
    <li><a href="#references"> ➤ References</a></li>
    <li><a href="#credits"> ➤ Credits</a></li>
  </ol>
</details>



<!-- OVERVIEW -->
<h2 id="overview">Sommaire</h2>

<p align="justify"> 
Ceci est une remise du projet 1 pour le cours 243-224-SH PROGRAMMATION 1.
Ma version du projet est une application web flask et les fonctionalités de noeud sont dirigé par le principe addressage url.
Ainsi je limite la charge de code dédié sur la traversée de l'arbre et j'ai pu me soucier plutot de la structure de celui-ci dans une base de donnée. La structure web me permet aussi d'offrir un visuel web standard plutot que console. Le fait d'avoir une base de données me permet aussi de créer l'histoire et l'arbre directement par l'application et de l'enregistrer selon les besoin.
</p>

<!-- PROJECT FILES DESCRIPTION -->
<h2 id="project-files-description">Description de l'hierarchie des fichiers</h2>

<ul>
  <li><b>.venv</b> - Contient tout l'environnement virtuel, ce qui inclut les librairies et les scripts externes.</li>
  <li><b>flaskr</b> - Contient toutes les fonctionalité du projet.</li>
  <li><b>instance</b> - Contient le/les instance de la base de données liée à l'application.</li>
</ul>

<h3>À l'intérieur de flaskr</h3>
<ul>
<h3>Dossiers</h3>
    <li><b>_pycache__</b> - Contient toutes les données enregistrées en cache.</li>
    <li><b>static</b> - Contient les fichiers statiques, principalement le css général.</li>
    <li><b>template</b> - Contient les fichiers html dynamiques pour l'affichage.</li>
  <h3>Fichiers</h3>
    <li><b>__init__.py</b> - Contient les fonctionalités pour initialiser l'application.</li>
    <li><b>auth.py</b> - Contient les fonctionalités pour l'authentification de base.</li>
    <li><b>db.py</b> - Contient les fonctionalités pour la connection à la base de données.</li>
    <li><b>node.py</b> - Contient les principales fonctionalités pour le projet 1 (Tout ce qui concerne les noeuds).</li>
</ul>

<!-- GETTING STARTED -->
<h2 id="getting-started">Pour commencer</h2>
<h3>Pour tester les fonctionalités du projet, vous devez ouvrir le terminal au niveau du dossier "myproject".
</h3><h3>Entrez ces deux commandes une à la suite de l'autre.</br>Il existe une version windows et une version linux celon votre système d'exploitation</h3>
<details>
  <summary>Windows</summary>
  <pre><code>> py -3 -m venv .venv</code></pre>
  <pre><code>> .venv\Scripts\activate</code></pre>
</details>
</br>
<details>
  <summary>Linux</summary>
  <pre><code>$ python3 -m venv .venv</code></pre>
  <pre><code>$ . .venv/bin/activate</code></pre>
</details>
<h3>Après avoir activé votre environement virtuel, veuillez entrer cette commande afin d'installer Flask.</h3>
<pre><code>$ pip install Flask</code></pre>
<h3>Finalement, veuillez entrer cette commande pour démarrer l'application</h3>
<pre><code>$ flask --app flaskr run --debug</code></pre>
<h3>L'application devrait normalement se trouver sur l'addresse: <a href="http://127.0.0.1:5000/1/read">http://127.0.0.1:5000/1/read</a></h3>
<!-- CREDITS -->
<h2 id="credits">Références</h2>

<h3>https://flask.palletsprojects.com</h3>
<h4><a href="https://flask.palletsprojects.com/en/stable/installation/">Installation flask</a></h4>
<h4><a href="https://flask.palletsprojects.com/en/stable/tutorial/factory/">Modèle suivit pour créer application web flask</a></h4>
