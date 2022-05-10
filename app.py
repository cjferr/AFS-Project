from flask import Flask, render_template, jsonify
import driver

app = Flask(__name__)


# TODO: remove FLASK_ENV from .env
# todo: return each of the stations individually, and then print them.  Also need to figure out how we're going to make it run on the button click
@app.route("/")
def index():
    # render_template creates a string out of the html file and variables passed in 
    html_str = render_template('index.html', workouts=[])
    print(html_str)
    return html_str


# pure API endpoint
# input: nothing
# output: a JSON list of workouts


def workouts_list():
    while True:
        try:
            return driver.get_workouts()
        except:
            return workouts_list()


# client-side rendering (pure API endpoint / returns JSON)
@app.route("/generate-workouts")
def workouts_JSON():
    return jsonify(workouts_JSON())

# server-side rendering (returns an HTML page)


@app.route("/show-workouts", methods=["GET"])
def show_workouts():
    return render_template('index.html', workouts=workouts_list())
