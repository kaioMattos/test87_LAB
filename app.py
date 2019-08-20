from flask import Flask, jsonify, request
from controllers.productController import  ProductController
app = Flask(__name__)
productController = ProductController()

@app.route('/devs',methods=['GET'])
def home():
    return productController.showProducts()


@app.route('/POST/tax' ,methods=['POST'])
def validationImpost():
    data = request.get_json();
    productController.popObject(data)
    productController.setImpost()
    return jsonify(productController.showImpost())


@app.route('/POST/testCalcImpost' ,methods=['POST'])
def test():
    data = request.get_json();
    
    return jsonify(productController.testCalcImpost(data))


@app.route('/POST/track', methods=['POST'])
def saveProduct():
    data = request.get_json();
    productController.popObject(data)
    productController.setImpost()
    return jsonify(productController.saveProduct())

@app.route('/POST/track/<string:id>', methods=['GET'])
def showOnlyProduct(id):  
    return jsonify(productController.getProductPerId(id))
   
if __name__ == "__main__":
    app.run(debug=True) 