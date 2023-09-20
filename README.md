Vinventory - Gestion de Cave à Vin
Vinventory Logo

Vinventory est une application web de gestion de cave à vin construite avec Django. Elle vous permet de suivre et de gérer votre collection de vins de manière simple et efficace.

Fonctionnalités
Gestion de la Cave : Suivez les détails de chaque vin de votre collection, y compris le nom, le millésime, le cépage, la région, la quantité en stock, et plus encore.

Recherche et Filtres : Recherchez rapidement un vin spécifique ou utilisez des filtres pour trier et organiser votre collection.

Ajout et Suppression Faciles : Ajoutez de nouveaux vins à votre cave et supprimez-les en cas de besoin.

Notes et Évaluations : Ajoutez des notes et des évaluations personnelles à chaque vin pour garder une trace de vos préférences.

Exportation de Données : Exportez vos données de cave à vin au format CSV pour une utilisation en dehors de l'application.

Configuration
Prérequis
Python 3.x
Django 3.x
Un navigateur web moderne
Installation
Clonez ce dépôt sur votre machine locale :

git clone https://github.com/votre-utilisateur/vinventory.git
Accédez au répertoire du projet :

cd vinventory
Installez les dépendances requises :

pip install -r requirements.txt
Appliquez les migrations Django :

python manage.py migrate
Créez un superutilisateur pour accéder à l'interface d'administration :

python manage.py createsuperuser
Lancez le serveur de développement :

python manage.py runserver
Accédez à l'application dans votre navigateur à l'adresse http://localhost:8000/.

Utilisation
Connectez-vous en utilisant les identifiants du superutilisateur que vous avez créés.

Ajoutez vos vins à la cave via l'interface d'administration ou en utilisant l'interface utilisateur de Vinventory.

Explorez et gérez votre collection de vins, ajoutez des notes et des évaluations.

Contributeurs
Votre nom
Autres contributeurs (le cas échéant)
Licence
Ce projet est sous licence MIT.
