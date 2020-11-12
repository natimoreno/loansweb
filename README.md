# Loans app

### Required
* Python 3.8
* SQLite3

### Devel environment

Environment

```
git clone <url>
makevirtualenv --python <version> <name>
pip install -r requeriments.txt
```

Django

```
python manage.py migrate loans
python manage.py createsuperuser 
python manage.py runserver
```

```
Como funciona ?

Cualquier usuario puede solicitar un prestamo desde "Get Now"
La seccion "Manage Loans" requiere login. Para esto hay que 
registrar un usuario en la seccion de Administración de Django.

Create group: ManageLoans
Create user: asignar al grupo ManageLoans 
```
