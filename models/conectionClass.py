import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
class Conexao:

    
    @staticmethod 
    def conect():
        server = 'cpro40229.publiccloud.com.br' 
        database = 'GISINISTRO' 
        username = 'sa' 
        password = 'Nova@1885673'
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        return cnxn