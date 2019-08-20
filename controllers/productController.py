from flask import Flask, jsonify, request

from models.productModels import Products
_objetc = {}
product = Products(_objetc)
class ProductController:
  

    def popObject(self, data):
        print(data)
        for key, value in data.items():   
            if key == 'name':
                product.setName(value)
            if key == 'height':
                product.setHeight(float(value))
            if key == 'width':
                product.setWidth(float(value))
            if key == 'price':
                product.setPrice(float(value))
            if key == 'length':
                product.setLength(float(value))
            if key == 'weight':
                product.setWeight(float(value))

    def getParamsCalcImpost():
        height = product.getHeight()
        width = product.getWidth()
        length = product.getLength()
        price = product.getPrice()
        weight = product.getWeight()
        return ProductController.calcImpost(height,width,length,price,weight)

    def calcImpost(height,width,length,price,weight):
        
        volume = float(height) * float(width) * float(length)
        pesoCalculado = float(volume) * 300
        if pesoCalculado <= 100:
            impost = (float(price)/100) * 5
        else:
            impost = pesoCalculado * (float(weight)/1000)
        return impost

    def showProducts(self):
        return product.getAllProducts()

    def setImpost(self):
        impost = ProductController.getParamsCalcImpost()
        product.setImpost(float(impost))
    def showImpost(self):
        return product.getImpost()
    def getVers(self):
        return product.getVersion()
    def saveProduct(self):
        return product.insertInto()
    def getProductPerId(self, id):
        return product.getProduct(id)

    def testCalcImpost(self, data):
        for key, value in data.items():   
            if key == 'height':
                height = (float(value))
            if key == 'width':
                width = (float(value))
            if key == 'price':
                price = (float(value))
            if key == 'length':
                length = (float(value))
            if key == 'weight':
               weight = (float(value))
        return ProductController.calcImpost(height,width,length,price,weight) 




