#Useful commands for the Project Learnt:

pipenv --python 3.10.9
pipenv shell  
pipenv install Flask
pipenv run pip freeze > requirements.txt or pipenv lock -r > requirements.txt
flask --app server.py --debug run

#escape helps in adding security such that it stringifies the commands so that they don't execute and affect the website and is default

#http://127.0.0.1:5000/hi?userName=Random to test with query with username

#Figure out how to make JS work with this

#References:

https://flask.palletsprojects.com/en/2.2.x/

https://jinja.palletsprojects.com/en/3.1.x/

https://render.com/docs/deploy-flask

#Questions to Consider:

- How are HTTP requests and responses represented?
- How do I handle routing
- How do I host static files?
- How do I host templates, where can I find examples of if statements, loops, and interpolation. What are the “Escape” rules?
- How are “interceptors” / “filters” / “middleware” handeled?
- Can I see an example of processing:
- HTTP query parameters
- HTTP request body in standard form encoding
- HTTP request body in json
- returning json instead of HTML From there – I normally want examples for query parameters, and http request body parsing in standard form-encoding and json encoding.
