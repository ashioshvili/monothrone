import random
def generate_answer(sender_name,messaging_text,entity,value):
	response = None
	greeting_list = ["გამარჯობა", "პრივეტ", "სალამი"]
	abc = {'ა':('a'),'ბ':('b'),'გ':('g'),'დ':('d'),'ე':('e'),'ვ':('v'),'ზ':('z'),'თ':('t'),'ი':('i'),'კ':('k'),'ლ':('l'),'მ':('m'),'ნ':('n'),'ო':('o'),'პ':('p')
			,'ჟ':('j','zh'),'რ':('r'),'ს':('s'),'ტ':('t'),'უ':('u'),'ფ':('f'),'ქ':('q','k'),'ღ':('g'),'ყ':('y','k'),'შ':('sh'),'ჩ':('ch'),'ც':('c','ts'),'ძ':('z','dz'),'წ':('ts','c','w'),'ჭ':('ch')
			,'ხ':('x','kh'),'ჯ':('j'),'ჰ':('h')}
	
	name_ge = ''
	for char in range(len(sender_name)):
		for key, val in abc.items():
			for n in range(len(val)):
				if char == val[0]:
					name_ge += key
			
	if entity == 'greeting_keys':
		greet_txt = random.choice(greeting_list)
		response = "{greet} {name}!".format(greet=greet_txt,name=name_ge)
	if response == None:
		response = "ბოდიში {name}, '{answer}' ჯერ არ ვიცი რას ნიშნავს :)".format(name=name_ge,answer=messaging_text)
	return response