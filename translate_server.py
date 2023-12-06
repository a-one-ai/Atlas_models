from flask import Flask, render_template, request,jsonify,json
from translate_model import translate

app = Flask(__name__)

supported_languages = {"arabic":"ar","english":"en","french":"fr"}

@app.route('/atlas/translation', methods=['POST'])
def index():
    try:
        if request.method == 'POST':
            user_input = request.form.get('user_input')
            script_lang = request.form.get('script_lang')
            script_lang= script_lang.lower()
            if script_lang in supported_languages.values():
                translated_result = translate(user_input, script_lang)
            elif script_lang in supported_languages.keys():
                translated_result = translate(user_input, supported_languages[script_lang])
                
            response={
                'user_input': user_input,
                'translated': translated_result
            }
            return jsonify(response)
    except KeyError as e:
        print(e)
        return "please reupload again"

if __name__ == '__main__':
    app.run(debug=True)
