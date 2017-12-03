from flask import Flask, render_template, request
app = Flask(__name__)

import sys
import json
from os.path import join, dirname
from watson_developer_cloud import ToneAnalyzerV3

tone_analyzer = ToneAnalyzerV3(
    version='2017-11-21',
    username='put your own username',
    password='put your own password'
)


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return toneAnalyze(request.form['text'])
    elif request.method == 'GET':
        return render_template('index.html')


@app.route("/result", methods=['GET', 'POST'])
def result():
    return render_template('result.html')


def toneAnalyze(textInput):
    tone = tone_analyzer.tone(textInput, tones=None, content_type='text/plain')
    data = json.dumps(tone, indent=2)
    return output(data)


def output(jsonInput):
    data = json.loads(jsonInput)
    scoreList = []
    toneList = []
    mergeList = []
    for x in data["document_tone"]["tones"]:
        scoreList.append(x["score"])
        toneList.append(x["tone_name"])
    # If there's only one sentence, then there will not have sentences tone exist
    try:
        for y in data["sentences_tone"]:
            sentList = []
            for z in y["tones"]:
                sentList.append(y["text"])
                sentList.append(z["tone_name"])
                sentList.append(z["score"])
                mergeList.append(sentList)
                sentList = []
    except:
        pass
    finalList = [scoreList, toneList, mergeList]
    return render_template('result.html', resultList=finalList)


if __name__ == '__main__':
    app.run(debug=True)
