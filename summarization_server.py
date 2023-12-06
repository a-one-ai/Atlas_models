from flask import Flask, render_template, request
from summarization_model import get_summary

app = Flask(__name__)

@app.route('/Atlas/summarization', methods=['GET', 'POST'])
def index():
    summary = None
    user_input = ""

    if request.method == 'POST':
        user_input = request.form['user_input']
        summary = get_summary(user_input)

    return render_template('summarization.html', user_input=user_input, summary=summary)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
