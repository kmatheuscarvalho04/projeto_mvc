from flask import Blueprint, render_template, request, send_file
from projeto_mvc.models import relatorios
from projeto_mvc.models.exportar import gerar_excel_sintetico  # <- crie esse arquivo se ainda não tiver

bp_relat = Blueprint('relatorios', __name__)

@bp_relat.route('/gerar_relatorio', methods=['GET','POST'])
def gerar_relatorio():
    return render_template('relatorio/gerar_relatorio.html')

@bp_relat.route('/relatorio', methods=['POST'])
def relatorio():
    mes_relatorio = request.form.get('mes_relatorio').replace('-', '')
    tipo = request.form.get('tipo_relatorio')
    acao = request.form.get('acao')

    if tipo == 'SINTÉTICO':
        dados = relatorios.relatorio_sintetico(mes_relatorio)

        if acao == 'excel':
            caminho = gerar_excel_sintetico(dados, mes_relatorio)
            return send_file(caminho, as_attachment=True)
        else:
            return render_template('relatorio/vis_sintetico.html', dados=dados, mes_relatorio=mes_relatorio)
    else:
        dados, total = relatorios.relatorio_analitico(mes_relatorio)
        return render_template('relatorio/vis_analitico.html', dados=dados, dados_totalconsult=total)


@bp_relat.route('/exportar_sintetico', methods=['GET'])
def exportar_sintetico():
    mes_relatorio = request.args.get('mes_relatorio')
    dados = relatorios.relatorio_sintetico(mes_relatorio)
    caminho = gerar_excel_sintetico(dados, mes_relatorio)
    return render_template('relatorio/vis_sintetico.html')
