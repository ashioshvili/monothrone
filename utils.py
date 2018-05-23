from wit import Wit
#
access_token = "NKQBRYAM5AXIJ4AKMEJIOMA6RXSXTYVZ"

client = Wit(access_token = access_token)

def wit_response(message_text):
	resp = client.message(message_text)
	categories = {}
	entities = list(resp['entities'])
	for entity in entities:
		categories[entity] = resp['entities'][entity][0]['value']
	return categories

def wit_sname(message_text):
	resp = client.message(message_text)
	entity = None
	value = None
	try:
		entity = list(resp['entities'])[0]
		value = resp['entities'][entity][0]['value']
	except:
		pass
	return (entity, value)