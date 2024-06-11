from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Rota para realizar o cálculo
@app.route("/calculate", methods=["POST"])
def calculate():
    expression = request.form["expression"]
    try:
        # Avalia a expressão matemática
        result = eval(expression)
        return render_template("index.html", result=result)
    except Exception as e:
        error_message = f"Erro: {str(e)}"
        return render_template("index.html", error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
