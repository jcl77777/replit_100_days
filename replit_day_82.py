from flask import Flask, request

app = Flask(__name__)

languages = {
    "jp": "Konnichiwa",
    "fr": "Bonjour",
    "de": "Hallo Guten Tag",
    "es": "Hola",
    "ch": "你好",
    "en": "Hello"
}

@app.route('/language', methods=['GET'])
def get_language():
    lang_code = request.args.get("lang")
    #check if lang in the dictionary
    if lang_code:
        return languages.get(lang_code, "Language not found")
    #provide valid parameter
    else:
        return "Please provide a 'lang' parameter."

@app.route('/')
def index():
    return "Hello World!"

app.run(host='0.0.0.0', port=81)