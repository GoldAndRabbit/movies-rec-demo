> ## Django install

执行
``` commandline 
pip install Django -i https://pypi.tuna.tsinghua.edu.cn/simple 
cd repos
django-admin.py startproject recdemo
cd recdemo
python manage.py runserver
```

提示
``` commandline
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
```

执行
``` commandline
cd recdemo
python manage.py migrate
python manage.py runserver
```

修改settings.py
``` python
ALLOWED_HOSTS = ['0.0.0.0', 'adminserver', 'localhost']

STATIC_URL = '/static/'
# must add follow dir
STATICFILES_DIRS = (
     os.path.join(BASE_DIR, 'static').replace('\\', '/'),
     os.path.join(BASE_DIR,).replace('\\', '/'),
)
```

执行
``` commandline
python manage.py runserver 127.0.0.1:8000
```