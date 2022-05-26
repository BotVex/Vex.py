from random import randint


class Colors:
	success = 0x38c48c
	error   = 0xff045c
	general = 0xfad4fb
	
	
	def RGB2HEX(RGB):
		return ''.join(f'{i:02X}' for i in RGB)
	
	
	def genRGBtuple():
		return (randint(0, 255), randint(0, 255), randint(0, 255))
	

class Emojis:
	success = '<:svTick_sim:975225579479646258>'
	neutral = '<:svTick_Neutro:975225608697159830>'
	error = '<:svTick_Nao:975225649029578782>'
	interrogation = '<:help:975225718822809650>'
	unknown_file = '<:unknown_file:975886833181421661>'
	unavailable_filter = '<:unavailable_filter:975888355051044874>'
	architecture = '<:arquitetura:975501599633977404>'
	disnake_icon = '<:disnake:975495299067965471>'
	python_icon = '<:python:975497682149863444>'
	tools = '🛠️'
	entertainment = '🪀'
	image = '🖼️'