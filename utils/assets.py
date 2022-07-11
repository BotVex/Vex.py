from random import randint
from PIL import ImageColor
from colorir import sRGB, HSV


class Colors:
	success = 0x38c48c
	error   = 0xff045c
	general = 0xfad4fb
	
	
	def RGB2HEX(RGB):
		return ''.join(f'{i:02X}' for i in RGB)
	
	
	def HEX2RGBtuple(HEX):
		return ImageColor.getcolor(HEX, 'RGB')
	
	
	def RGB2HSVtuple(RGB):
		r, g, b = RGB
		H, S, V = sRGB(r, g, b).hsv(round_to=1)
		return H, S, V
	
	
	def HSV2RGBtuple(HSV_):
		h, s, v = HSV_
		R, G, B = HSV(h, s, v).sRGB()
		return R, G, B
	
	
	def genRGBtuple():
		return (randint(0, 255), randint(0, 255), randint(0, 255))


class Emojis:
	success = '<:Y_:987924991557374002> | '
	neutral = '<:nan:987925016823889920> | '
	error = '<:X_:987925044623704085> | '
	unknown_file = '<:unknown_f:987924931629182986> | '
	unavailable_filter = '<:u_filter:987924962390196234> | '
	disnake_icon = '<:disnake:987925228397146182> | '
	python_icon = '<:py:987925080191402064> | '
	botTag = '<:bot_tag:987925288384102450>'
	github = '<:github:990768354216267848>'
	tools = '🛠️ | '
	entertainment = '🪀 | '
	image = '🖼️ | '
	owner = '🐺 | '
	administration = '⚙️ | '


class MediaUrl:
	noguildicon = 'https://i.postimg.cc/KvpGZvz3/9152fdef6eda843249ed83a5606fa745279afbae7681b1b33a8f1b43746cdb99-3.jpg'
	commandoncooldownbanner = 'https://i.postimg.cc/vHmfqMN7/102-Sem-Titulo-20220604000113.png'
	notownerbanner = 'https://i.postimg.cc/QxVSBphr/102-Sem-Titulo-20220604001852.png'
	missingpermissionsbanner = 'https://i.postimg.cc/TYGLFxNN/102-Sem-Titulo-20220604114118.png'
	botmissingpermissionsbanner = 'https://i.postimg.cc/TYGLFxNN/102-Sem-Titulo-20220604114118.png'
	noprivatemessagebanner = 'https://i.postimg.cc/Twx8JtQS/102-Sem-Titulo-20220604141342.png'
	ben10icon = 'https://i.postimg.cc/g0ctx0jd/Et9-Fc-VDXEAIg88c.jpg'
