from Hello import Hello

class mama(Hello):
	"""docstring for mama"""
	def __init__(self,arg):
		super(mama, self).__init__()
		Hello._init__(self,"",0,0)
		if arg == "OK":

			self.name = "Sarah"
			self.age = 20
			self.size = 0
			# Hello.__init__(self,self.name,self.age,self.size)
			mama.set(self,self.name,self.age,self.size)
			mama.get(self)

	def get(self):
		Hello._init__(self,self.name,self.age,self.size)
		mama.speak(self)
		