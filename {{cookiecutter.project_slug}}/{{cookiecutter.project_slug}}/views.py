from {{cookiecutter.project_slug}} import app
from flask import render_template

#--------------------------------------------------------------------------------------------------------------------
#   ACCUEIL:
#   Tous les templates liés à l'accueil de l'utilisateur
#
#--------------------------------------------------------------------------------------------------------------------

# Page d'accueil
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='page not found'), 404