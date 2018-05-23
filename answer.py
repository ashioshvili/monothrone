import random
def generate_answer(entity_name,value_name,sender_name,messaging_text,entity,value):
	response = None
	greeting_list = ["გამარჯობა", "პრივეტ", "სალამი"]
	"""
	abc = {'ა':('a'),'ბ':('b'),'გ':('g'),'დ':('d'),'ე':('e'),'ვ':('v'),'ზ':('z'),'თ':('t'),'ი':('i'),'კ':('k'),'ლ':('l'),'მ':('m'),'ნ':('n'),'ო':('o'),'პ':('p')
			,'ჟ':('j','zh'),'რ':('r'),'ს':('s'),'ტ':('t'),'უ':('u'),'ფ':('f'),'ქ':('q','k'),'ღ':('g'),'ყ':('y','k'),'შ':('sh'),'ჩ':('ch'),'ც':('c','ts'),'ძ':('z','dz'),'წ':('ts','c','w'),'ჭ':('ch')
			,'ხ':('x','kh'),'ჯ':('j'),'ჰ':('h')}
	snm = sender_name.lower()
	name_ge = ''
	name_spell = ''
	skip = 1000
	for n in range(len(snm)):
		got_two_ch = 0
		if n < (len(snm)-1) and n != skip:
			two_ch = snm[n] + snm[n+1]
			for key, val in abc.items():
				for nn in range(len(val)):
					if two_ch == val[nn]:
						got_two_ch = 1
						name_ge += key
						skip = n+1
			if got_two_ch == 0:
				for key, val in abc.items():
					for bn in range(len(val)):
						if snm[n] == val[bn]:
							name_ge += key
				if n+1 == (len(snm)-1):
					for key, val in abc.items():
						for cn in range(len(val)):
							if snm[n+1] == val[cn]:
								name_ge += key
	"""
	if entity_name == 'names_georgian':
		geo_name = value_name
	else:
		geo_name = sender_name
	
	if entity == 'greeting_keys':
		greet_txt = random.choice(greeting_list)
		response = "{greet} {name}!".format(greet=greet_txt,name=geo_name)
	if entity != None:
		response = "Ent: {en}\nVal: {ev}".format(en=entity,ev=value)
	if response == None:
		response = "ბოდიში {name}, '{answer}' ჯერ არ ვიცი რას ნიშნავს :)".format(name=geo_name,answer=messaging_text)
	return response