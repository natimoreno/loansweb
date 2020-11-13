# Loans app

### Required
* Python 3.8
* SQLite3

### Devel environment

Environment

```
git clone https://github.com/natimoreno/loansweb.git
makevirtualenv --python <version> <name>
pip install -r requeriments.txt
```

En el archivo mysite/.env configurar las credenciales para
la API Rest que retorna el resultado de la solicitud de prestamos.
```
mysite/.env

URL="xxxx"
CREDENTIAL="xxxxx"
```

Django

```
python manage.py migrate
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
