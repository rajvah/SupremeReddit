# Team SUPREME Reddit Wrapper DEMO User Guide

### Initial Dependencies Download
1. Python 3 (we used 3.8 for our project): https://www.python.org/downloads/
2. Cassandra: https://pypi.org/project/cassandra-driver/
    1. Install on Linux: https://cassandra.apache.org/doc/latest/cassandra/getting_started/installing.html 
    2. Install on MacOS: https://medium.com/@manishyadavv/how-to-install-cassandra-on-mac-os-d9338fcfcba4
    3. In a new terminal window, you have to set up a simple `reddit` table for `cassandra`:
```
cassandra -f
cqlsh
CREATE KEYSPACE reddit WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor':1};
exit
```
3. Django: https://pypi.org/project/Django/
    1. Install: https://docs.djangoproject.com/en/4.0/topics/install/ 

### Once the Dependencies are Set
1. Open terminal or command line in your machine
2. Clone the repository from the `main` branch to your local machine: `git clone git@github.com:rajvah/SupremeReddit.git`
3. Then run the following commands to install Django, migrate the models for the local databases, sync the databases with the migrations, and get the local server up and running:

```
cd r2
pip install django
pip install cassandra-driver
cassandra -f (if not running already from dependencies set up)
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate --run-syncdb
python3 manage.py runserver
```

### Once the Server is Running
1. In a web browser of your choice on the same machine, go to localhost address: `http://127.0.0.1:8000/r2app/`
2. Click around the differently labeled buttons
3. Compare and contrast the output messages in the terminal/server logging
4. See that the performance is consistent with and without the `db_wrapper.py`
