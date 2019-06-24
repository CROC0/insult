from flask import Flask, render_template, request
import os
from random import randint
app = Flask(__name__)

sk = os.environ.get('SECRET_KEY')
URL = os.environ.get('HEROKU_URL', 'http://127.0.0.1:5000/')

app_settings = {
    'SECRET_KEY': sk,
    "TEMPLATES_AUTO_RELOAD": True,
    'SQLALCHEMY_DATABASE_URI': os.environ.get(
                                            'DATABASE_URL',
                                            'sqlite:///data.db'
                                            ),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SESSION_TYPE': 'filesystem',
    'PERMANENT_SESSION_LIFETIME': (1 * 60 * 60)
}

app.config.update(app_settings)

@app.route("/", methods=["GET","POST"])
def insult():
    if request.method == "GET":
        A = [line.rstrip('\n') for line in open('a.txt')]
        B = [line.rstrip('\n') for line in open('b.txt')]
        C = [line.rstrip('\n') for line in open('c.txt')]

        string = "{} {} {}".format(
                                    A[randint(0, len(A)-1)],
                                    B[randint(0, len(B)-1)],
                                    C[randint(0, len(C)-1)]
                                    )

      #  return render_template('index.html', top="Thou", bottom=string)
    else:
        string = request.form.get('insult')
    return render_template('index.html', top="Thou", bottom=string)

if __name__ == "__main__":
    app.run()