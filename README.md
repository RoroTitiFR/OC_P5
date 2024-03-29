# NutriChecker by @RoroTiti

![Screenshots](https://i.imgur.com/jU9H4kz.png)

## User manual

### Getting started

To run the application, it's recommended to setup a virtual environment. We will use virtualenv.

- Move to the source root directory
```
cd "/the/app/directory"
```

- Initialize a virtualenv
```
pip install virtualenv # install virtualenv if not already installed
virtualenv venv
```

- Enable the virtual environment (Windows)
```
.\venv\Scripts\activate
```

- Enable the virtual environment (macOS)
```
source venv/bin/
```

- Install NutriChecker dependencies
```
pip install -r requirements.txt
```

### Database setup

NutriChecker requires a MySQL database in order to save its data. 
Follow the steps in order to obtain a working database setup. 

- Execute the ``create_tables.sql`` file on the MySQL database where you want to host the data of the application.

To communicate with the database, NutriChecker uses the Peewee ORM. You have 2 options to configure the connection to the database.

**Option 1 : regenerate the Peewee model file (recommended and reliable)** 

- From the source root directory, run :
````
python -m pwiz -e mysql -H {database host} -p {database port} -u {database user} -P {database name} > models/database.py
````

**Option 2 : update the model template credentials (may be unreliable according to your database setup or encoding)** 

- Modify ``models/database.py`` and update the database connection credentials :
  - ``host`` : the database IP address
  - ``port`` : the database port
  - ``user`` : the user who has access to the database created previously
  - ``password`` the password of the user

### Run NutriChecker and populate the database

- You can now start NutriChecker with the following command
```
python main.py
```

In order to populate the data from the OpenFoodFacts API, NutriChecker contains an user friendly assistant helping you to download the data.
To access it, go to ``Outils``, ``Mise à jour des données...``

- On the window which will open, click on ``Charger la liste``. It will fetch relevant categories from the OpenFoodFacts API.
- Once the list is fetched, select the categories you want to download and click on ``Ajouter``. The items will be added to the selected categories list.
If you want to remove an item from the selected categories list, simply select it and click on ``Supprimer``.
- Once you are done, click on ``Télécharger les produits``. You can watch the progression and eventual issues on your Python console.
Since the tool only download the products with complete details, if a product is not downloaded, the reason will be displayed on the Python console.
- Close the updater tool and click on ``Recharger les données``, to fetch the freshly downloaded data from the MySQL database.

NutriChecker is now ready, you can start exploring the data and find substitutes for any product you search !

### Exploring the data

Navigation is easy. Here is a guide about how to use NutriChecker :

- First of all, select a category. Categories are listed into the list right below the ``Recharger les données`` button.
When you select a category, all known products for this category are displayed on the products list.
- Once you have a list of products with their primary brand and some details, like the NUTRI-SCORE, 
you can view the details of a product by either double-clicking on it on the list or by selecting a product and then pressing Enter.
This will open a details window separated from the main window, so you can open any amount of details window as you want.
This is useful when you want to compare multiple products together.
- When you select a product on the list, you will see some relevant substitutes on the list below.
You can interact with the substitutes list like the products list.
- When you find a great substitute for a given product, you can it in order to access it quickly later.
In order to save a product with its substitute, select a substitute and click the ``Enregistrer le substitut`` button.
- You can find the saved substitute from the ``Mes substituts enregistrés`` tab.
It will display the list of all the saved products with their corresponding substitutes together with some details.
Again, you can interact with it like with the products or the substitutes lists described before.

### Generating the code documentation

The documentation is generated by Sphinx. All the setup files are already present in source code to allow easy documentation generation.
Here is a guide giving you the steps to generate Read The Docs styled HTML documentation based on the configuration files.

- Move to the documentation configuration directory from the source directory
````
cd docs
````
 
- Build the documentation (Windows)
````
make.bat html
````

- Build the documentation (macOS)
````
make html
````

You will now find the generated documentation in ``_build/html`` directory.
Simply open the ``index.html`` in a web browser and you can start exploring the source code documentation. 

You can also generate PDF documentation easily. You must first install ``latexmk``.
See the guide about how to install it here : [Unofficial Latexmk documentation](https://mg.readthedocs.io/latexmk.html).
Then, use the same commands as to generate HTML documentation, but replace ``html`` by ``latexpdf``.
The result PDF will be saved in ``_build/latex``

## Working environment
- Windows 10 or macOS Mojave and upper
- Python 3.7.4
- MySQL 8.0.17 and upper