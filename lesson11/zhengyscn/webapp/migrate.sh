
if [ $1 = "" ];then
    exit 0
fi

if [ $1 = "migrate" ];then
    python manage.py makemigrations
    python manage.py migrate
elif [ $1 = "run" ];then
    python manage.py runserver 0.0.0.0:8000
fi
