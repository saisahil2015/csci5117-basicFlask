from flask import Flask, request, render_template

app = Flask(__name__)
# tells Flask to be used and processed as an import or as the main file

# tells the app to run the below function on going to the following URL


@app.route("/")
def hello_world():
    return "<p> Hello World <p>"


@app.route('/hi', methods=['GET'])
def hi():
    # looking for username in query parameters. the one after "?"
    user_name = request.args.get("userName", "unknown")
    return render_template('main.html', user=user_name)
