from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
  if(request.method == "GET"):
    return render_template("index.html")
  else:
    num1 = request.form["num1"]
    num2 = request.form["num2"]
    opc = request.form["opc"]
    if (num1 != "" and num2 != ""):
      if(opc == "soma"):
        soma = int(num1) + int(num2)
        return str(soma)
      elif(opc == "subi"):
        subi = int(num1) - int(num2)
        return str(subi)
      elif(opc == "multi"):
        multi = int(num1) * int(num2)
        return str(multi)
      elif(opc == "divi"):
        divi = int(num1) // int(num2)
        return str(divi)
      
    else:
      return "Informe um valor válido"

# @app.route("/<int:id>")
# def home_id(id):
#   return str(id + 1)

@app.errorhandler(404)
def not_found(error):
  return render_template("error.html")

@app.errorhandler(405)
def not_found2(error):
  return "O verbo não existe"

app.run(port=8080, debug=True)