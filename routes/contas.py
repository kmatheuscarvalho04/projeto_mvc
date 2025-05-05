from flask import Blueprint, render_template, request, redirect, url_for, flash
from projeto_mvc.models import contas_a_pagar

bp_contas = Blueprint('contas', __name__)

@bp_contas.route('/contas_a_pagar')
def contas_a_pagar_view():
    return render_template('contas_a_pagar.html')

@bp_contas.route('/inserir_ctas_pagar', methods=['POST'])
def inserir_ctas_pagar():
    sucesso, mensagem = contas_a_pagar.inserir_conta(request.form)
    flash(mensagem)
    return redirect(url_for('contas.contas_a_pagar_view'))
