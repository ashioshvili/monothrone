import random
def generate_answer(sender_name,messaging_text,entity,value):
	response = None
	greeting_list = ["გამარჯობა", "პრივეტ", "სალამი"]
	if entity == 'greeting_keys':
		greet_txt = random.choice(greeting_list)
		response = "{greet} {name}!".format(greet=greet_txt,name=sender_name)
	if response == None:
		response = "ბოდიში {name}, '{answer}' ჯერ არ ვიცი რას ნიშნავს :)".format(name=sender_name,answer=messaging_text)
	return response