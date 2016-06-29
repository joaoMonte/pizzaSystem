#!flask/bin/python


from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

dictPerson = {}

def createTable():
    strHtmlTable = "<head><link rel= \"stylesheet\" type= \"text/css\" href= \"{{ url_for(\'static\',filename=\'styles/table.css\') }}\">"
    strHtmlTable += "</head><table><thead><tr><th>Nome</th><th>Quantidade</th>"
    strHtmlTable += "<th>Refrigerante</th><th>Sugest&atilde;o</th></tr></thead><tbody>"
    tableLines = ""

    for person in dictPerson:
        qtd = dictPerson[person]['qtd']
        refri = dictPerson[person]['refri']
        sabor = dictPerson[person]['sabor']
        tableLines += createTableLine(person, qtd, refri, sabor)


    strHtmlTable += tableLines
    strHtmlTable += "</tbody></table>"
    print (strHtmlTable)
    table = open('templates/table2.html', 'w')
    print("ola")

    table.write(strHtmlTable)
    table.close()

def createTableLine(name, qtd, refri, sabor):
    strHtml = "<tr><td><strong>"
    strHtml += str(name)
    strHtml += "</strong></td><td>"
    strHtml += str(qtd)
    strHtml += "</td><td>"
    strHtml += str(refri)
    strHtml += "</td><td>"
    strHtml += str(sabor)
    strHtml += "</td></tr>"

    return strHtml


def addPerson(name, qtd, refri, sabor):
    global dictPerson
    dictPerson[name] = {'qtd':qtd, 'refri':refri, 'sabor':sabor}

@app.route('/pizza', methods=['GET'])
def my_form():
    return render_template("form.html")

@app.route('/pizza', methods=['POST'])
def my_form_post():
    name = request.form['name']
    qtd = request.form['qtd']
    refri = request.form['refri']
    sabor = request.form['sabor']
    addPerson(name, qtd, refri, sabor)
    createTable()
    return render_template("table2.html")

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
