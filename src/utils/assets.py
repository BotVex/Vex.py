from random import randint
from PIL import ImageColor
from colorir import sRGB, HSV


class Colors:
	success = 0x38c48c
	error = 0xff045c
	general = 0xfad4fb
	warning = 0xecfc03
	
	
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
	success = '<:Y_:987924991557374002>'
	neutral = '<:nan:987925016823889920>'
	error = '<:X_:987925044623704085>'
	disnake_icon = '<:disnake:987925228397146182>'
	python_icon = '<:py:987925080191402064>'
	bot_tag = '<:bot_tag:1023267356417458266>'

	icon_ban = '<:Icon_ban:1017293963406884867>'
	beta1 = '<:beta1:1017294298275926027>' 
	beta2 = '<:beta2:1017294345612824618>' 
	dev = '<:dev:1017292588656635964>' 
	disnake = '<:disnake:1017292954278309888>' 
	github = '<:github:1017292626946441276>' 
	icon_arrow_green_right = '<:icon_arrow_green_right:1017293880678416394>' 
	icon_arrow_red_left = '<:icon_arrow_red_left:1017293845882470430>'
	icon_check_green = '<:icon_check_green:1017293768648577067>' 
	icon_id = '<:icon_id:1017294935654940742>'
	icon_profile = '<:icon_profile:1017295044501327933>'
	icon_warn_red = '<:icon_warn_red:1017293473231163402>'
	icon_warn_yellow = '<:icon_warn_yellow:1017293540767846421>'
	icon_x_red = '<:icon_x_red:1017293727556964423>'
	spotify = '<:spotify:1017293041666629735>'
	trash = '<:trash:1066030051411361873>'
	dot = '<:dot:1019072815233765396>'
	dance = '<a:dance:1066043138491306134>'
	reverse = '<:reverse:1066045215795843212>'
	block = '<:block:1066046626671628418>'
	monoculo = '<:monoculo:1066057929247179005>'
	boost = '<a:boost:1066061313874329740>'


class MediaUrl:
	noguildicon = 'https://i.postimg.cc/KvpGZvz3/9152fdef6eda843249ed83a5606fa745279afbae7681b1b33a8f1b43746cdb99-3.jpg'
	commandoncooldownbanner = 'https://i.postimg.cc/vHmfqMN7/102-Sem-Titulo-20220604000113.png'
	notownerbanner = 'https://i.postimg.cc/QxVSBphr/102-Sem-Titulo-20220604001852.png'
	missingpermissionsbanner = 'https://i.postimg.cc/TYGLFxNN/102-Sem-Titulo-20220604114118.png'
	botmissingpermissionsbanner = 'https://i.postimg.cc/TYGLFxNN/102-Sem-Titulo-20220604114118.png'
	noprivatemessagebanner = 'https://i.postimg.cc/Twx8JtQS/102-Sem-Titulo-20220604141342.png'
	
	def get_oracle(oracle):
		if oracle == 'Ben 10':
			return 'https://i.postimg.cc/g0ctx0jd/Et9-Fc-VDXEAIg88c.jpg'
		elif oracle == 'Finn':
			return 'https://i.postimg.cc/x1qgrwtk/image.jpg'
		elif oracle == 'Vovó Juju':
			return 'https://i.postimg.cc/FsckfmD5/image.jpg'
