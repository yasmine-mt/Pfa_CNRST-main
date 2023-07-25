# Installation
Après avoir clôné le repo :

    # Requirements
    python 3.6
    pip3
    virtualenv
    # Recommandé : créez un environnement virtuel
    $ virtualenv venv
    $ venv\Scripts\activate
    
    # Initialisez la DB
    $ python manage.py makemigrations
    $ python manage.py migrate
    
    # Lancez le serveur de dev
    $ python manage.py runserver

Le site sera accessible à l'adresse http://localhost:8000/.
# Technologies utilisées:
Python
Django
Bootstrap
JavaScript
HTML
CSS
# Database
SQLite
# Modules Python supplémentaires requis :
Django , Django-filter ,Django-auditlog

# Pour effectuer le TEST E2E  :
installer le pilote du navigateur (chromedriver.exe) :

1 -> Téléchargez le pilote ChromeDriver correspondant à la version de Google Chrome installée sur votre machine depuis le site officiel de Chromium: https://sites.google.com/a/chromium.org/chromedriver/downloads
Une fois téléchargé, extrayez le fichier chromedriver.exe dans un emplacement de votre choix.

2 -> Installer la bibliothèque Selenium :

    pip install selenium

    pip install --upgrade selenium


3 -> Exécutez le script de test E2E :
    
    python test.py




