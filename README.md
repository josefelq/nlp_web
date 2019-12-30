### Requirements
* Python 3+
* Virtualenv (Optional)

### Installation (Assuming you have a virtualenv already set up)
1. Clone repository.
2. Inside project go to user_example/views.py and find the 'header' dictionary. Replace APPLICATION_ID and APPLICATION_KEY with AYLIEN ID and Key respectively.
3. Run 'pip install -r requirements.txt' in root of project (where manage.py is located).
4. Run 'python manage.py migrate' in root of project.
5. Run 'python manage.py runserver' in root of project.
6. In any browser go to http://localhost:8000 .
