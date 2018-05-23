import random
import time
from datetime import datetime
#
def generate_answer(entity_name,value_name,sender_name,messaging_text,got_entities):
	response = None
	geo_name = ''
	hour = ''
	greet_txt = ''
	greeting_list = ["გამარჯობა", "გაგიმარჯოს", "მოგესალმებით"]
	if entity_name == 'names_georgian':
		geo_name = value_name
	else:
		geo_name = sender_name
	greet_msg = 0
	for key,val in got_entities.items():
		if key == 'greeting_keys':
			day_time = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
			if day_time[-8] != '0' and day_time[-7] != '0':
				hour = day_time[-8] + day_time[-7]
			if day_time[-8] == '0' and day_time[-7] != '0':
				hour = day_time[-7]
			if day_time[-8] == '0' and day_time[-7] == '0':
				hour = '00'
			if hour != '00':
				if int(hour) >= 6 and int(hour) <= 11:
					greet_txt = "დილამშვიდობის"
				if int(hour) >= 12 and int(hour) <= 4:
					greet_txt = "შუადღემშვიდობის"
				if int(hour) >= 5 and int(hour) <= 7:
					greet_txt = "საღამომშვიდობის"
				if int(hour) >= 8 and int(hour) <= 5:
					greet_txt = "ღამემშვიდობის"
			if hour == '00':
				greet_txt = "ღამემშვიდობის"
			#greet_txt = random.choice(greeting_list)
			response = "{greet} {name}!".format(greet=greet_txt,name=geo_name)
			greet_msg = 1
	for key,val in got_entities.items():		
		if key != None and key != 'greeting_keys':
			if greet_msg == 1:
				response += "\nEnt: {en}\nVal: {ev}".format(en=key,ev=val)
			else:
				response += "Ent: {en}\nVal: {ev}\n".format(en=key,ev=val)
	
	if response == None:
		response = "ბოდიში {name}, '{answer}' ჯერ არ ვიცი რას ნიშნავს :)".format(name=geo_name,answer=messaging_text)
	return response
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