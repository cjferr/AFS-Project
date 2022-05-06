from flask import Flask, render_template
import driver

app = Flask(__name__)


# TODO: remove FLASK_ENV from .env
# todo: return each of the stations individually, and then print them.  Also need to figure out how we're going to make it run on the button click
@app.route("/")
def index():
    return render_template('index.html', workouts=[])


@app.route("/workouts")
def show_workouts():
    while True:
        try:
            workouts = driver.get_workouts()
            print(len(workouts))
            print(workouts)
            print("\n\n\n\n\n\n\n\n\n\n")
            break
        except:
            return show_workouts()

    return render_template('index.html', workouts=workouts)
