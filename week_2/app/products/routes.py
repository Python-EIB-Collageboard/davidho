from flask import Blueprint, request
import uuid

_products: list[dict] = []

products_bp = Blueprint(
    'products',
    __name__,
    url_prefix='/products'
)

@products_bp.get('/')
def get_products():
    return { 'products': _products }, 200 

@products_bp.get('/<string:product_id>')
def get_product(product_id):
    if not product_id:
        return {"error": "product_id required"}, 400
    
    for product in _products:
        if product['id'] == product_id:
            return product, 200

    return { "error": f"product with id {product_id} was not found" }, 404

@products_bp.post('/')
def create_product():
    payload = request.get_json(silent=True)

    if not payload:
        return {"error": "JSON body required"}, 400
    
    payload['id'] = str(uuid.uuid4())
    
    product = payload

    _products.append(product)

    return { 'data': product }, 201

@products_bp.put('/<string:product_id>')
def update_product(product_id):
    if not product_id:
        return {"error": "product_id required"}, 400
    
    payload = request.get_json(silent=True)

    if not payload:
        return {"error": "JSON body required"}, 400
    
    payload['id'] = str(uuid.uuid4())
    
    for index, product in enumerate(_products):
        if product['id'] == product_id:
            _products[index] = payload
            return { "data": "success" }, 200

    
    return { "error": f"product with id {product_id} was not found" }, 404

@products_bp.delete('/<string:product_id>')
def delete_product(product_id):
    if not product_id:
        return {"error": "product_id required"}, 400
    
    for index, product in enumerate(_products):
        if product['id'] == product_id:
            del _products[index]
            return '', 204
    
    return { "error": f"product with id {product_id} was not found" }, 404