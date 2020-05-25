print("Jai Ma Jagdambe!!\n-----------------\n")

#dependency_Dict = {} # dict with Set as value. Sample: {comp1: depSet1, comp2: depSet2, ..}
installed_Set = set() # set constructor. set containing components. Sample: {comp1, comp2, ..}
dependencyOn_Dict = {} # dict with component dependent on it.
numberOfDependency_Dict = {} # dict with component and number of other components which are dependent on it.
allowedCommandSet = {"DEPEND", "INSTALL", "LIST", "REMOVE", "END"}

def DEPEND(commandLine):
	print("DEPEND Called")
	commandLineWords = commandLine.split(" ") #list type
	dep_size = len(commandLineWords)
	#print(dep_size)
	#print(type(dep_size))
	for i in range(2, dep_size):
		#print(commandLineWords[i])
		if commandLineWords[1] in dependencyOn_Dict:
			print(commandLineWords[1] + " Present")
			dependencyOn_Dict[commandLineWords[1]].add(commandLineWords[i])
			
			if commandLineWords[i] in numberOfDependency_Dict:
				numberOfDependency_Dict[commandLineWords[i]] = numberOfDependency_Dict[commandLineWords[i]] + 1
			else:
				numberOfDependency_Dict[commandLineWords[i]] = 1
		else: 
			print(commandLineWords[1] + " Not Present")
			dependencyOn_Dict[commandLineWords[1]] = {commandLineWords[i]}
			#print(type(dependencyOn_Dict[commandLineWords[1]])) #set type
			print(dependencyOn_Dict[commandLineWords[1]])
			
			if commandLineWords[i] in numberOfDependency_Dict:
				numberOfDependency_Dict[commandLineWords[i]] = numberOfDependency_Dict[commandLineWords[i]] + 1
			else:
				numberOfDependency_Dict[commandLineWords[i]] = 1
				
			
		
	print(dependencyOn_Dict)
	print(numberOfDependency_Dict)

def INSTALL(commandLine):
	print("INSTALL Called")
	commandLineWords = commandLine.split(" ") #list type
	install_size = len(commandLineWords)
	for i in range(1, install_size):
		if commandLineWords[i] not in dependencyOn_Dict: #INSTALL component rightaway.
			installed_Set.add(commandLineWords[i])
		else:											#INSTALL components and then it's dependencies too
			installed_Set.add(commandLineWords[i]) 
			for deps in dependencyOn_Dict[commandLineWords[i]]:
				installed_Set.add(deps)
		
	
	print(installed_Set)

def REMOVE(commandLine):
	print("REMOVE Called")
	commandLineWords = commandLine.split(" ") #list type
	remove_size = len(commandLineWords)
	for i in range(1, remove_size):
		#if commandLineWords[i] not in dependencyOn_Dict: #components is never installed. 
		#	#installed_Set.add(commandLineWords[i])
		#	print(commandLineWords[i] + " not installed.")
		if commandLineWords[i] not in numberOfDependency_Dict or numberOfDependency_Dict[commandLineWords[i]] == 1:  #REMOVE component right away.
			print("Removing " + commandLineWords[i])
		elif numberOfDependency_Dict[commandLineWords[i]] > 1: #There are dependencies
			print(commandLineWords[i] + " is still needed.")
		
	
	print(numberOfDependency_Dict)

def LIST():
	for comp in installed_Set:
		print(comp)


f = open("inputCommands.txt", "r")
for commandLine in f:
	print("\n>>>" + commandLine) #str type

	commandLine = " ".join(commandLine.split()) #First split by whitespace, to remove multi-spaces, join back.
	#print(len(commandLine))
	if len(commandLine) <= 2:
		print("Empty Command")
	elif commandLine.split()[0] not in allowedCommandSet:
		print("Invalid Command")
	elif commandLine.split()[0] == "DEPEND": #takes whitespace as delimiter
		#commandLineWords = commandLine.split(" ") #list type
		#for s in commandLineWords:
		#	print(s)
		DEPEND(commandLine)
	elif commandLine.split()[0] == "INSTALL": #takes whitespace as delimiter
		#commandLineWords = commandLine.split(" ") #list type
		#for s in commandLineWords:
		#	print(s)
		INSTALL(commandLine)
	elif commandLine.split()[0] == "REMOVE": #takes whitespace as delimiter
		#commandLineWords = commandLine.split(" ") #list type
		#for s in commandLineWords:
		#	print(s)
		REMOVE(commandLine)
	elif commandLine.split()[0] == "LIST": #takes whitespace as delimiter
		#commandLineWords = commandLine.split(" ") #list type
		#for s in commandLineWords:
		#	print(s)
		LIST()
	elif commandLine.split()[0] == "END": #takes whitespace as delimiter
		#commandLineWords = commandLine.split(" ") #list type
		#for s in commandLineWords:
		#	print(s)
		print("END")
		break
		
print("Finish Fast!!")
		
	
	
