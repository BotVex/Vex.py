from io import BytesIO
from colorthief import ColorThief


def dominant_color(img):
	color_thief = ColorThief(BytesIO(img))
	dominant = color_thief.get_color(quality=1)
	color = ''.join(f'{i:02X}' for i in dominant)
	return int(color, 16)

