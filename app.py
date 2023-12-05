from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs 10,000,00'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Mumbai, India',
    'salary': 'Rs 20,000,00'
  },
  {
    'id': 3,
    'title': 'Front-end Engineer',
    'location': 'Chennai, India'
  },
  {
    'id': 4,
    'title': 'Full-stack Developer',
    'location': 'San francisco, USA',
    'salary': '$ 120,000'
  }
]
@app.route("/")
def hello_world():
  return render_template("home.html", 
                         jobs=JOBS, 
                         company_name = "Speed's")

@app.route("/api/jobs")
def job_list():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)