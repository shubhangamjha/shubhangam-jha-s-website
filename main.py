from flask import Flask, render_template

app = Flask(__name__)


JOBS = [
  {
    'id': '1',
    'title': 'Data Analysist',
    'location': 'Bengaluru, India',
    'salary': '₹10,00,000'
    
  },

  {
    'id': '2',
    'title': 'Data Scientist',
    'location': 'Greater, India',
    'salary': '₹15,00,000'
    
  },

  {
    'id': '3',
    'title': 'Data Engineer',
    'location': 'California, USA',
    
    
  }
]

@app.route("/")

def hello_world():
  return render_template('home.html', 
                         jobs=JOBS,
                        company_name= 'Terminal Stacks')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True) 