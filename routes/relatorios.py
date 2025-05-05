from flask import Blueprint, render_template, request, flash
from projeto_mvc.models import relatorios

bp_relat = Blueprint('relatorios', __name__)

@bp_relat.route('/gerar_relatorio')
def gerar_relatorio():
    return render_template('gerar_relatorio.html')

@bp_relat.route('/relatorio', methods=['POST'])
def relatorio():
    de_data = request.form.get('de_data').replace('-', '')
    para_data = request.form.get('para_data').replace('-', '')
    tipo = request.form.get('tipo_relatorio')

    if tipo == 'SINTÉTICO':
        dados = relatorios.relatorio_sintetico(de_data, para_data)
        return render_template('vis_sintetico.html', dados=dados)
    else:
        dados, total = relatorios.relatorio_analitico(de_data, para_data)
        return render_template('vis_analitico.html', dados=dados, dados_totalconsult=total)
