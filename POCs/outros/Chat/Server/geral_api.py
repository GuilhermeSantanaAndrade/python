from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from services.geral_service import logon as service_logon

geral_app = Blueprint('geral_app', __name__, template_folder='templates')

campos = ["usuario", "ip", "port"]
tipos = [dict, str, int]

@geral_app.route('/logon/', methods=['POST'])
def logon():
    dados = request.get_json()
    print(dados)
    
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        result = service_logon(dados['usuario']['nome'], dados['usuario']['segredo'])
        return jsonify(to_dict(result))
    except Exception as err:
        return 'Erro em logon:' + err, 409