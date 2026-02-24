mapper = {"HELLO": "ENGLISH", 
          "HOLA": "SPANISH", 
          "HALLO": "GERMAN", 
          "BONJOUR": "FRENCH", 
          "CIAO": "ITALIAN", 
          "ZDRAVSTVUJTE": "RUSSIAN"}

tc = 1
while True:
	target = input()
	if target == "#":
		break
	
	if target in mapper.keys():
		print(f"Case {tc}: {mapper[target]}")
		tc += 1
	
	else: 
		print(f"Case {tc}: UNKNOWN")
		tc += 1
