# hello, world!
1. start project hello, world
    1. python -m pip install django~=3.2 
    2. django-admin startproject hello world
    3. python manage.py runserver
2. startapp
   1. python manage.py startapp playground
   2. ssettimgs.py > INSTALLED_APPS 'playground', 추가     
3. playground/views
   1. say_Hello()
4. urls
   1. playground/hello/ => say_Hello()
5. urls, playground/urls 
   1. playground/ -> hello. -> say_hello()
6. templates/playground/hello.html
   1. playground/ -> hello_html/ -> say_hello_html() -> html
