from flask import Flask, render_template, session
from config import SECRET_KEY
from controllers.membro_controller import bp_membro
from controllers.contribuicao_controller import bp_contribuicao

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

# Rotas principais
@app.route('/')
def inicio():
    session.setdefault('menu_expandido', False)
    return render_template('base/index.html', menu_expandido=session['menu_expandido'])

@app.route('/menu')
def menu():
    return render_template('base/menu.html')

# @app.route('/toggle_menu', methods=['POST'])
# def toggle_menu():
    # session['menu_expandido'] = not session.get('menu_expandido', False)
    # return '', 204

# Registrar Blueprints
app.register_blueprint(bp_membro)
app.register_blueprint(bp_contribuicao)

if __name__ == '__main__':
    app.run(debug=True)
