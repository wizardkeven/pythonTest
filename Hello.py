# This is a sample python class
class Hello(object):
	name = ""
	age = 0
	size = 10.0
	def _init__(self,n,a,s):
		self.name = n
		self.age = a
		self.size = s

	def speak(self):
		print("%s is speaking: I am %d years old and penis is of size: %d"%(self.name,self.age,self.size))


	def set(self,name,age,size):
		self.name = name
		self.age = age
		self.size = size
		pass
#print("Hello guokai")
	#if(name=="guok" or name =="Nick"):
	# print("Alert: Alice Mode")
 	#	name = name +"???" 
	#else:
	# print("Else")
	#	name = mame+"!!!!"
	# print("Hello" , name)

# h = Hello()
# h._init__("Rama", 20, 10.5)
# h.speak()
