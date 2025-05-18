from flask import Flask, render_template, request

app = Flask(__name__)
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

@app.route("/", methods=["GET", "POST"])
def caesar_cipher():
    result = ""
    message = ""
    shift =0 
    if request.method == "POST":
        message = request.form["message"]
        shift = int(request.form["shift"])
        for char in message:
            if char.upper() in alpha:
                loc = alpha.find(char.upper())
                new_char = alpha[(loc + shift) % 26]
                result += new_char
            else:
                result += char
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
