from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def initial():
    return render_template('index.html')

@app.route('/process',methods=["POST"])
def process():
    data = {}
    data["name"] = request.form["input_name"]
    data["location"] = request.form["select_location"]
    data["languaje"] = request.form["select_languaje"]
    data["comment"] = request.form["input_comment"]
    data["sexo"] = request.form["input_sexo"]
    editor_text = ""
    cont = 0;
    for i in request.form.getlist("input_check"):
        if cont == 0:
            editor_text += i
        else:
            editor_text += " , " + i
        cont += 1
    
    data["editor_text"] = editor_text
    session["data"] = data
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)