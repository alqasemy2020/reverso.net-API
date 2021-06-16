from flask import Flask, request, jsonify, render_template_string
from utl import get_translation


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/translate/')
def main():
    source = request.args.get('source')
    lang = request.args.get('lang')
    word = request.args.get('word')
    
    data = get_translation(source, lang, word)

    return jsonify(data=data)

@app.route('/')
@app.route('/home')
def home():
    return render_template_string("""<script>
    document.addEventListener("DOMContentLoaded", function(event) {     
    var div = document.createElement('a');
    var b = document.createElement('b');
    b.innerText = 'Usage Example: '
    div.href = 'https://' + window.location.host + '/translate/' + '?source=en&lang=ar&word=hello'
    div.innerText = 'https://' + window.location.host + '/translate/' + '?source=en&lang=ar&word=hello'
    document.body.append(b);
    document.body.append(div);
   });</script>""")

if __name__ == '__main__':
    app.run(host='0.0.0.0')


