from flask import Flask, render_template, request
import model

app=Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        buying=request.form['buying']
        maintainence=request.form['maint']
        doors=request.form['doors']
        persons=request.form['persons']
        lug_boot=request.form['lug_boot']
        safety=request.form['safety']
        message=model.predict(buying, maintainence, doors, persons, lug_boot, safety)

        return render_template('index.html', message=message)

if __name__=='__main__':
    app.run(port=2000, debug=True)
