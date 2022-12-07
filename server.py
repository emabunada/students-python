import requests
import json
from flask import Flask, render_template
import jinja2

from student import Student

app = Flask(__name__)

get_students_link = 'http://staging.bldt.ca/api/method/build_it.test.get_students'

students = []


@app.route("/")
def home():
    students.clear()
    response = requests.get(get_students_link)
    json_response = json.loads(response.text)
    for entry in json_response['data']:
        students.append(
            Student(full_name=entry['full_name'], s_id=entry['id'], level=entry['level'], mobile=entry['mobile_number'],
                    age=entry['age']))


    return render_template('index.html', students=students)


app.run(debug=True)
