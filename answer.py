import random
def generate_answer(sender_name,messaging_text,entity,value):
	response = None
	greeting_list = ["გამარჯობა", "პრივეტ", "სალამი"]
	abc = {'ა':('a'),'ბ':('b'),'გ':('g'),'დ':('d'),'ე':('e'),'ვ':('v'),'ზ':('z'),'თ':('t'),'ი':('i'),'კ':('k'),'ლ':('l'),'მ':('m'),'ნ':('n'),'ო':('o'),'პ':('p')
			,'ჟ':('j','zh'),'რ':('r'),'ს':('s'),'ტ':('t'),'უ':('u'),'ფ':('f'),'ქ':('q','k'),'ღ':('g'),'ყ':('y','k'),'შ':('sh'),'ჩ':('ch'),'ც':('c','ts'),'ძ':('z','dz'),'წ':('ts','c','w'),'ჭ':('ch')
			,'ხ':('x','kh'),'ჯ':('j'),'ჰ':('h')}
	snm = sender_name.lower()
	name_ge = ''
	name_spell = ''
	for n in range(len(snm)):
		got_two_ch = 0
		two_ch = snm[n] + snm[n+1]
		for key, val in abc.items():
			for nn in range(len(val)):
				if two_ch == val[nn]:
					got_two_ch = 1
					name_ge += key
		if got_two_ch == 0:
			for key, val in abc.items():
				if snm[n] == val[nn]:
					name_ge += key
		
					
		"""
		if (sender_name[n] + sender_name[n+1]) == 'sh':
			name_ge += 'შ'
			
		else:
			if sender_name[0] == 'x':
				name_ge += 'ხ'
			if sender_name[0] == 'x':
				name_ge += 'ხ'
			if len(sender_name)-(n+1) != 0:
				char = sender_name[n]
				for key, val in abc.items():
					for n in range(len(val)):
						if char == val[0]:
							name_ge += key
		"""	
	if entity == 'greeting_keys':
		greet_txt = random.choice(greeting_list)
		response = "{greet} {name}!".format(greet=greet_txt,name=name_ge)
	if response == None:
		response = "ბოდიში {name}, '{answer}' ჯერ არ ვიცი რას ნიშნავს :)".format(name=name_ge,answer=messaging_text)
	return response