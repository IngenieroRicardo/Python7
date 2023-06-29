#------------------------classe aritmetica----------------------------#
class aritmetica:
	#variablepublica = 'editable' <- esta es la forma de crear variables publicas
	#inicializamos variables#
	def __init__(self):
		self.n1 = 0.0
		self.n2 = 0.0
	#metodos set#
	def setn1(self, n1):
		self.n1 = n1
	def setn2(self, n2):
		self.n2 = n2
	#metodos get#
	def getn1(self): 
		return str(self.n1)
	def getn2(self): 
		return str(self.n2)
	def getsuma(self):
		return str(self.n1+self.n2)
  

#------------------------ejecucion principal----------------------------#
clase = aritmetica()
#usamos funciones set de la clase aritmetica#
clase.setn1( float("2.3") )
clase.setn2( float("2.2") )
#usamos funciones get de la clase aritmetica#
print(clase.getsuma())
