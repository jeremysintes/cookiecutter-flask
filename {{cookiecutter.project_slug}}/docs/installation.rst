.. highlight:: shell

============
Installation
============

{% if cookiecutter.type_of_project == 'flask' %}

1. Clone the git

.. code-block:: console

    git clone gh://{{ cookiecutter.git_username }}/{{ cookiecutter.project_slug }}

2. It is recommended to create a developpement environment (exemple below with Anaconda):

.. code-block:: console

	conda create –n {{ cookiecutter.project_slug }}

3. Activate the developpement environment :

.. code-block:: console

   activate {{ cookiecutter.project_slug }}

4. Install the required librairies :

.. code-block:: console

    pip install -r requirements

5. Run the application : 

.. code-block:: console

    python run.py 

6. Go to your browser at the indicated URL
{% endif %}


{% if cookiecutter.type_of_project == 'pypi' %}

Stable release
--------------

To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release. 

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.project_name }} can be downloaded from the `Git repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone https://{{ cookiecutter.git_source }}/{{ cookiecutter.git_username }}/{{ cookiecutter.project_slug }}

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://{{ cookiecutter.git_source }}/{{ cookiecutter.git_username }}/{{ cookiecutter.project_slug }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Git repo: https://{{ cookiecutter.git_source }}/{{ cookiecutter.git_username }}/{{ cookiecutter.project_slug }}
.. _tarball: https://{{ cookiecutter.git_source }}/{{ cookiecutter.git_username }}/{{ cookiecutter.project_slug }}/tarball/master
{% endif %}