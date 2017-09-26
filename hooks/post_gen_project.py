#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def remove_directory(dirpath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))

def rename(filepath, newname):
    os.rename(os.path.join(PROJECT_DIRECTORY, filepath), os.path.join(PROJECT_DIRECTORY, newname), )   





if __name__ == '__main__':
    if '{{ cookiecutter.use_pypi_deployment_with_travis }}' != 'y':
        remove_file('travis_pypi_setup.py')

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE.rst')
    
    if 'pypi' == '{{ cookiecutter.type_of_project }}':
        template_file = os.path.join('{{ cookiecutter.project_slug }}', 'templates.zip')
        views_file = os.path.join('{{ cookiecutter.project_slug }}', 'views.py')
        static_file = os.path.join('{{ cookiecutter.project_slug }}', 'static')
        init_flask_file = os.path.join('{{ cookiecutter.project_slug }}', '__init__flask.py')
        init_pypi_file = os.path.join('{{ cookiecutter.project_slug }}', '__init__pypi.py')
        init_file = os.path.join('{{ cookiecutter.project_slug }}', '__init__.py')

        remove_file(template_file)    
        remove_file(views_file)    
        remove_directory(static_file)    
        remove_file(init_flask_file)    
        remove_file('app.yaml')
        rename(init_pypi_file, init_file )

    
    if 'flask' == '{{ cookiecutter.type_of_project }}':
        #delete the pypi elements from the {{ cookiecutter.project_slug }} folder
        #unzip('{{ cookiecutter.project_slug }}/templates.zip')
        init_pypi_file = os.path.join('{{ cookiecutter.project_slug }}', '__init__pypi.py')
        init_flask_file = os.path.join('{{ cookiecutter.project_slug }}', '__init__flask.py')
        init_file = os.path.join('{{ cookiecutter.project_slug }}', '__init__.py')
        #template_file = os.path.join('{{ cookiecutter.project_slug }}', 'templates.zip')
        APP_DIRECTORY = os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}')

        #shutil.unpack_archive(template_file, APP_DIRECTORY)
        #remove_file(template_file)        
        remove_file('{{ cookiecutter.project_slug }}/__init__pypi.py')
        rename(init_flask_file, init_file )
        remove_file('setup.py')


    if 'n' == '{{ cookiecutter.create_devsite }}':
        remove_file('run_devsite.py')  
        remove_directory('{{ cookiecutter.project_slug }}_devsite')

    if 'y' == '{{ cookiecutter.create_devsite }}':
        DEVSITE_DIRECTORY = os.path.join(PROJECT_DIRECTORY, '{{ cookiecutter.project_slug }}_devsite')
 



