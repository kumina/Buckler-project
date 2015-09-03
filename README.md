Kibanana - kibanana sample project
==================================

Kibanana adds multi user support (with authentication and per-user indexes)
to Kibana4

To install:

Git clone this repository

    git clone git@bitbucket.org:kibanana/kibanana Kibanana

Make it a virtualenv

    virtualenv --system-site-packages Kibanana

cd into it, install zc.buildout and run buildout

    cd Kibanana && bin/pip install zc.buildout && bin/buildout -c development.cfg

Customize settings:

    cd Kibanana/settings
    cp config.py-in config.py
    vi config.py

Make sure you set the correct UPSTREAM url's for Kibana and ElasticSearch, and that they're accessible from the host

Start Django:

    cd ..
    bin/django runserver

Go to http://localhost:8000/ and use the credentials you've set in config.py
