from flask import Flask
from projeto_mvc.routes.dizimista import bp as dizimista_bp
from projeto_mvc.routes.movimento import bp_mov as movimento_bp
from projeto_mvc.routes.contas import bp_contas as contas_bp
from projeto_mvc.routes.relatorios import bp_relat as relatorios_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'TESTE'
    app.register_blueprint(dizimista_bp)
    app.register_blueprint(movimento_bp)
    app.register_blueprint(contas_bp)
    app.register_blueprint(relatorios_bp)
    return app
