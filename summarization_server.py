from flask import Flask, jsonify, request
from summarization_model import get_summary

app = Flask(__name__)

@app.route('/atlas/summarization', methods=['POST'])
def summarization():
    try:
        if request.method == 'POST':
            user_input = request.form['user_input']
            summary = get_summary(user_input)
            response_data = {
                'user_input': user_input,
                'summary': summary
            }
        return jsonify(response_data)
    except:
        return "please enter valid text"
if __name__ == '__main__':
    app.run(debug=True, port=8000)
