from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from projeto_mvc.models import membro
# from models import dizimista

bp = Blueprint('dizimista', __name__)

@bp.route('/')
def inicio():
    session.setdefault('menu_expandido', False)
    return render_template('base/index.html', menu_expandido=session['menu_expandido'])

@bp.route('/menu')
def menu():
    session.setdefault('menu_expandido', False)
    return render_template('base/menu.html', menu_expandido=session['menu_expandido'])

@bp.route('/vis_dizimista', methods=['GET','POST'])
def vis_dizimista():
    dados = membro.listar_membros()
    return render_template('dizimista/vis_dizimista.html', dados=dados)

@bp.route('/ins_dizimista',methods=['GET','POST'])
def ins_dizimista():
    dados = membro.listar_membros()
    return render_template('dizimista/ins_dizimista.html', dados=dados)

@bp.route('/alt_dizimista',methods=['GET','POST'])
def alt_dizimista():
    dados = membro.listar_membros()
    return render_template('dizimista/alt_dizimista.html', dados=dados)

@bp.route('/inserir', methods=['POST'])
def inserir_dados():
    sucesso, mensagem = membro.inserir_membro(request.form)
    flash(mensagem)
    if sucesso:
        return redirect(url_for('dizimista.vis_dizimista'))
    else:
        return redirect(url_for('dizimista.ins_dizimista'))
    
@bp.route('/alteracao',methods=['POST'])
def alteracao():
    sucesso, mensagem = membro.alterar_membro(request.form)
    flash(mensagem)
    if sucesso:
        return redirect(url_for('dizimista.vis_dizimista'))
    else:
        return redirect(url_for('dizimista.ins_dizimista'))
    