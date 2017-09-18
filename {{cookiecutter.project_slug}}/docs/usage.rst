=====
Usage
=====

{% if cookiecutter.type_of_project == 'pypi' %}
To use {{ cookiecutter.project_name }} in a project::

    import {{ cookiecutter.project_slug }}
{% endif %}

{% if cookiecutter.type_of_project == 'flask' %}
To run the application (from the root of your application) : 

.. code-block:: console

    python run.py 

Then go to your browser at the indicated URL
{% endif %}