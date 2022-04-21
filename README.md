# Softcane software setup guide

Clone the github code to local disk
```
git clone https://github.com/herufi-africa/softcane.git
```
## Django setup
Install django in the system using the line below
```
pip install django
```
You can the navigate to the folder
 ````
 cd \to\folder\having\the\softcane\code
 cd softcane
 ````

##Set up virtual environment
Install virtual environment package
```
#For Ubuntu or Mac
sudo apt-get update
sudo apt-get install python3-venv

#For windows
python -m pip install --user virtualenv 
```
Create a virtual environment for the project

```
#For Ubuntu or Mac
python3 -m venv env

#For Windows
python -m venv env
```
Activate the virtual environment
```
#For Ubuntu or Mac
source env/bin/activate

#For Windows
env\Scripts\activate
```
## Install the dependencies of the project
On the terminal type
```
pip install -r requirements.txt
```

## Run the migrations
Run the migrations as below
```
$python manage.py makemigrations
$python manage.py migrate
```
## Create the superusers
```
$python manage.py createsuperuser
```
## Ultimately, Run the project
```
$python manage.py runserver
```

## Create a tenant
Go to the localhost:8000/admin to register a tenant

Go to the browser and type 'tenant_name'.localhost:8000 to start

"# softcane" 
