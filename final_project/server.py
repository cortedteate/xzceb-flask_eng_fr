from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    frentext = machinetranslation.eng_2_fre(textToTranslate)
    return frentext

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    engtext = machinetranslation.fre_2_eng(textToTranslate)
    return engtext

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    def hello():
    return render_template('index.html') #"Hello Traductor!"    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
