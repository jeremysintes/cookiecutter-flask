import config
from {{ cookiecutter.project_slug }}_devsite import app

if __name__ == '__main__':
    app.run(port=8081, debug=True)