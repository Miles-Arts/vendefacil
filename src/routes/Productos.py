from flask import Blueprint
from flask import jsonify

main=Blueprint('productos_blueprint',__name__)

@main.route('/')
def get_productos():
    return jsonify({'message': "Vende_Productos"})