Mandelbrot
==========

Setup

```
virtualenv virt
source virt/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
make -C css
make -C coffee
```

Importing data

```
./manage.py migrate
./manage.py loadsalesforce ~/staff.csv
./manage.py loadbios ../bios/
./manage.py loadpriorities
./manage.py loadmappings ~/mandelbrot-mappings/
./manage.py loadgithub
./manage.py loadpriorities
./manage.py dedupe
./manage.py runserver
```
