from email.policy import default
from flask import Flask, render_template, request, redirect
from PIL import ImageColor
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/snakegame/<string:move>', methods=['GET'])
def snakegame(move):
    print(move)
    return render_template('snakegame.html')
    
ButtonPressed=0
@app.route('/button', methods=["GET", "POST"])
def button():     
    global ButtonPressed
    if request.method == "POST":
        ButtonPressed+=1
        return render_template("button.html", ButtonPressed = ButtonPressed)
    ButtonPressed=0
    return render_template("button.html", ButtonPressed = ButtonPressed)

@app.route('/scroll', methods=["GET", "POST"])
def scroll():     
    if request.method == "POST":
        print(request.form['ptext'])
        return render_template("scroll.html")
    return render_template("scroll.html")

color='#ff0000'
@app.route('/matrix', methods=['GET','POST'])    
def matrix():
    global color
    if request.method == "POST":
        selected=request.form.getlist('LED')
        color=request.form.get('Color')
        print("the value is {}".format(selected))
        print(ImageColor.getrgb(color))
        return render_template('matrix.html', SELECTED=selected, COLOR=color)
    return render_template('matrix.html', COLOR=color)

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=80, debug=True) ## To run across LAN you can acess thought any of the devices by entering your ip followed by port http://192.168.0.###:80
    app.run(debug=True)