from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import membro

bp_membro = Blueprint('membro', __name__)


@bp_membro.route('/ins_dizimista', methods=['GET', 'POST'])
def inserir():
    if request.method == 'POST':
        membro.inserir_membro(
            request.form['cargo'],
            request.form['nome'],
            request.form['ri'],
            request.form['telefone']
        )
        flash("Registro inserido com sucesso!")
        return redirect(url_for('membro.visualizar'))
    return render_template('ins_dizimista.html')


@bp_membro.route('/alt_dizimista', methods=['GET', 'POST'])
def alteracao():
    if request.method == 'POST':
        membro.alterar_membro(
            request.form['id_ou_ri'],
            request.form['campo'],
            request.form['conteudo'],
        )
        flash("Registro alterado com sucesso!")
        return redirect(url_for('membro.visualizar'))
    return render_template('vis_dizimista.html')

