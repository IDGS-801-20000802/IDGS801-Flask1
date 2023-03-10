from flask import Flask, render_template

app= Flask(__name__)

@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/resultado", methodts=["POST"])
def resultado():
    n1=request.form.get("txtNum1")
    n2=request.form.get("txtNum2")
    res=int(n1)*int(n2)
    return render_template("usuarios.html", res, n1, n2)

if __name__=="__main__":
    app.run(debug=True, port=3000)