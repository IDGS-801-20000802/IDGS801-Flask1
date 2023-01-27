from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo Flask cambios nuevos"

@app.route("/Hola")
def hola():
    return "Hola desde hola"

@app.route("/Nueva")
def nueva():
    return "Hola desde holaaa"

if __name__=="__main__":
    app.run(debug=True, port=3000)