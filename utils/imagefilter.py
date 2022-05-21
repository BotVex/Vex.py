from io import BytesIO
from PIL import Image, ImageOps, ImageFilter


class Filters():
	def autocontrast(imagebytes, cutoff=0, ignore=None, mask=None, preserve_tone=False):
		pass