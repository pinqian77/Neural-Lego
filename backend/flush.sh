rm -rf db.sqlite3
rm -rf lego/migrations
rm -rf media/*
python3 manage.py makemigrations lego 
python3 manage.py migrate
python3 manage.py createsuperuser
