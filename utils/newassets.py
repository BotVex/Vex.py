import aiohttp
from io import BytesIO
from typing import Union
from random import randint
from PIL import ImageColor
from colorir import sRGB, HSV
from colorthief import ColorThief



class Icons:
	NOT_IN_GUILD = 'https://i.postimg.cc/KvpGZvz3/9152fdef6eda843249ed83a5606fa745279afbae7681b1b33a8f1b43746cdb99-3.jpg'
	CMD_ON_COOLDOWN = 'https://i.postimg.cc/vHmfqMN7/102-Sem-Titulo-20220604000113.png'
	NOT_OWNER = 'https://i.postimg.cc/QxVSBphr/102-Sem-Titulo-20220604001852.png'
	MISSING_PERMS = 'https://i.postimg.cc/TYGLFxNN/102-Sem-Titulo-20220604114118.png'
	BOT_MISSING_PERMS = 'https://i.postimg.cc/TYGLFxNN/102-Sem-Titulo-20220604114118.png' 
	NO_PRIVATE_MSG = 'https://i.postimg.cc/Twx8JtQS/102-Sem-Titulo-20220604141342.png'
	
	
	def get_oracle(oracle):
		if oracle == 'Ben 10':
			return 'https://i.postimg.cc/g0ctx0jd/Et9-Fc-VDXEAIg88c.jpg'
		elif oracle == 'Finn':
			return 'https://i.postimg.cc/x1qgrwtk/image.jpg'
		elif oracle == 'Vovó Juju':
			return 'https://i.postimg.cc/FsckfmD5/image.jpg'

class Emojis:
	PYTHON = '<:python:1017975869777645639>'
	DISNAKE = '<:disnake:1017292954278309888>'
	SPOTIFY = '<:spotify:1017293041666629735>'
	GITHUB = '<:github:1017292626946441276>' 
	DEV = '<:dev:1017292588656635964>'
	BETA1 = '<:beta1:1017294298275926027>'
	BETA2 = '<:beta2:1017294345612824618>' 
	X_RED = '<:icon_x_red:1017293727556964423>'
	WARN_YELLOW = '<:icon_warn_yellow:1017293540767846421>'
	WARN_RED = '<:icon_warn_red:1017293473231163402>'
	PROFILE = '<:icon_profile:1017295044501327933>'
	ID = '<:icon_id:1017294935654940742>'
	CHECK_GREEN = '<:icon_check_green:1017293768648577067>'
	ARROW_RED_LEFT = '<:icon_arrow_red_left:1017293845882470430>'
	ARROW_GREEN_RIGHT = '<:icon_arrow_green_right:1017293880678416394>'
	BAN = '<:Icon_ban:1017293963406884867>'
	BOT_TAG = '<:bot_tag:1023267356417458266>'
	CLOCK = '<:icon_clock:1017970780979601478>'
	GOOGLE = '<:google:1041029529994547310>'


class Assets(Emojis, Icons):
	pass


class DefaultColors:
	GREEN = 0x71FF51
	YELLOW = 0xFFE251
	RED = 0xFF5151
	BLUE = 0x51A2FF
	BLACK = 0x3D3D3D
	PYTHON_BLUE = 0x4584B6
	PYTHON_YELLOW = 0xffde57


class ColorConverter:
	def __init__(self):
		pass
	
	
	def RGB2HEX(RGB: Union[tuple, list[int]]) -> tuple:
		return ''.join(f'{i:02X}' for i in RGB)

	
	def HEX2RGB(HEX) -> tuple:
		return ImageColor.getcolor(HEX, 'RGB')

	
	def HEX2RGBA(HEX) -> tuple:
		return ImageColor.getcolor(HEX, 'RGBA')


	def RGB2HSVtuple(RGB: Union[tuple, list[int]]) -> tuple:
		r, g, b = RGB
		H, S, V = sRGB(r, g, b).hsv(round_to=1)
		return H, S, V


	def HSV2RGB(HSV_) -> tuple:
		h, s, v = HSV_
		R, G, B = HSV(h, s, v).sRGB()
		return R, G, B


class ColorGen:
	def __init__(self):
		pass
	
	def genRGB():
		return (randint(0, 255), randint(0, 255), randint(0, 255))
	
	
	def genRGBA():
		return (randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))


class GetColor:
	def general_color(img):
		color_thief = ColorThief(BytesIO(img))
		dominant = color_thief.get_color(quality=1)
		color = ''.join(f'{i:02X}' for i in dominant)
		return int(color, 16)
	
	
	async def general_color_url(url):
		async with aiohttp.ClientSession() as session:
			async with session.get(str(url)) as resp:
				img_file = await resp.content.read()
				color_thief = ColorThief(BytesIO(img_file))
				dominant = color_thief.get_color(quality=1)
				color = ''.join(f'{i:02X}' for i in dominant)
				return int(color, 16)


class Colors(DefaultColors, ColorConverter, ColorGen, GetColor):
	pass