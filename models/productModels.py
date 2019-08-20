from flask import Flask, jsonify, request
from models.conectionClass import Conexao
products = [
    {'id':'1','product':'Perfume', 'price':'50$'},
    {'id':'2','product':'Camisa', 'price':'150$'},
    {'id':'3','product':'Calça', 'price':'250$'}
]
conexao = Conexao()
cnx = conexao.conect()
cursor = cnx.cursor()
class Products:
    
    def __init__(self, _object):
        self.name = '' 
        self.height = 0
        self.length = 0
        self.width = 0
        self.weight = 0
        self.price = 0
        self.impost = 0
        self.volume = 0
        self.pesoCalculado = 0

    '''def setParam(self, param, value):
        print('set '+ str(param))
        self.param = value
        print(self.param)'''
    def setName(self,value):
        self.name = value
    def setHeight(self,value):
        self.height = value
    def setWidth(self,value):
        self.width = value
    def setPrice(self,value):
        self.price = value
    def setLength(self,value):
        self.length = value
    def setWeight(self,value):
        self.weight = value
    def setImpost(self, value):
        self.impost = value


    def getName(self):
        return self.name
    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width
    def getPrice(self):
        return self.price
    def getLength(self):
        return self.length
    def getWeight(self):
        return self.weight
    def getImpost(self):    
        return "{tax :"+str(self.impost)+"}"
    
    def returnAllAttrs(self):
        return self.__dict__  
    def getAllProducts(self):
        return jsonify(products),200

    def getProduct(self, id):
        for product in products:
            if product['id']==id:
                return jsonify(product),200
    def getVersion(self):
        
        
        cursor.execute("SELECT top 1 * from tb_011_gisinitro") 
        row = cursor.fetchone() 
        while row: 
            print (row) 
            row = cursor.fetchone()
        return row
    def insertInto(self):
        cursor.execute("INSERT product values (?, ?, ?, ?, ?, ?, ? )",self.name,self.height,self.length,self.width,self.weight,self.price,self.impost) 
        cnx.commit()
        return '{id:'+str(Products.returnLastId())+'}'
    def returnLastId():
        cursor.execute("SELECT max(id) from product") 
        row = cursor.fetchone()
        if row:
            linha = row[0]
        return linha
    def getProduct(self, id):
        cursor.execute("SELECT * from product where id = ?",id) 
        row = cursor.fetchone()
        if row:
            self.id = row[0]
            self.name = row[1]
            self.height = row[2]
            self.length = row[3]
            self.width = row[4]
            self.weight = row[5]
            self.price = row[6]
        return self.__dict__
