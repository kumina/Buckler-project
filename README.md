Buckler - buckler sample project
==================================

Buckler adds multi user support (with authentication and per-user indexes)
to Kibana4

To install:

Git clone this repository

    git clone git@git.kumina.nl:kibanana/buckler-project.git

Make it a virtualenv

    virtualenv --system-site-packages buckler-project

cd into it, install zc.buildout and run buildout

    cd buckler-project && bin/pip install zc.buildout && bin/buildout -c development.cfg

Customize settings:

    cd Buckler/settings
    cp config.py-in config.py
    vi config.py

Make sure you set the correct UPSTREAM url's for Kibana and ElasticSearch, and that they're accessible from the host

Start Django:

    cd ../..
    bin/django runserver

Go to http://localhost:8000/ and use the credentials you've set in config.py
