from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print("Received:", data)

    with open("SCHOOL.txt", 'a') as z:
        z.write('NAME  :  ' + data['name'] + '\n\n')
        z.write('CLASS : ' + data['student_class'] + '\n\n')
        z.write('SECTION : ' + data['section'] + '\n\n')
        z.write('ADMISSION NO. : ' + data['admission'] + '\n\n')
        z.write('MOBILE NO. : ' + data['mobile'] + '\n\n')
        z.write('ADDRESS : ' + data['address'] + '\n\n')
        z.write("===================================================\n\n")

    return jsonify({"message": "Student data saved successfully!"})

if __name__ == "__main__":
    app.run(debug=True)