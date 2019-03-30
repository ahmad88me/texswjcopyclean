from flask import Flask
from flask import render_template, request
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def main():
    result = ""
    raw = ""
    if 'raw' in request.form:
        raw = request.form['raw']
        result = clean(raw)
    return render_template('main.html', raw=raw, results=result)


def clean(t):
    newt = ""
    for line in t.split('\n'):
        tokens = line.strip().split(' ')
        start = 0
        if tokens[0].strip().isdigit():
            start = 1
        #     print "digit: "+tokens[0]
        # else:
        #     print("not: "+tokens[0])
        end = len(tokens)
        if tokens[-1].strip().isdigit():
            end = -1
        #     print("digit: "+tokens[-1])
        # else:
        #     print("not: "+tokens[-1])
        # newt += ' '.join(tokens[1:-1])+"\n"
        newt += ' '.join(tokens[start:end])+"\n"
    return newt


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
