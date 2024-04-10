from flask import Flask, render_template
from raspador import atualizar_planilha

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/infos")
def infos():
    return render_template('infos.html')

@app.route("/projetos")
def projetos():
    return render_template('projetos.html')

@app.route("/publicacoes")
def publicacoes():
    return render_template('publicacoes.html')

@app.route("/leissp")
def leissp():
    arquivo_credenciais = os.path.join(os.getcwd(), "insperaa-f16b8130bed9.json")

    # Chamando a função atualizar_planilha() para obter o HTML das tabelas
    tabela1_html, tabela2_html = atualizar_planilha(arquivo_credenciais=arquivo_credenciais)


    # Passando o HTML das tabelas para o template leissp.html
    return render_template('leissp.html', tabela1_html=tabela1_html, tabela2_html=tabela2_html)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
