from flask import Blueprint, render_template, request, redirect, url_for, flash,session
from projeto_mvc.models import admin

bp_adm = Blueprint('administrador', __name__)

@bp_adm.route('/admin')
def menu():
    session.setdefault('menu_expandido', False)
    return render_template('admin/admin.html', menu_expandido=session['menu_expandido'])