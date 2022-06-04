from io import BytesIO
from PIL import Image, ImageOps, ImageFilter


class Filters:
	
	def autocontrast(imagebytes, cutoff: int=0, ignore: int=None, mask=None, preserve_tone: bool=False):
		img_obj = Image.open(BytesIO(imagebytes)).convert('RGB')
		return ImageOps.autocontrast(img_obj, cutoff=cutoff, ignore=ignore, mask=mask, preserve_tone=preserve_tone)
	
	
	def equalize(imagebytes, mask=None):
		img_obj = Image.open(BytesIO(imagebytes)).convert('RGB')
		
		return ImageOps.equalize(img_obj, mask=mask)
	
	
	def flip(imagebytes):
		img_obj = Image.open(BytesIO(imagebytes))
		return ImageOps.flip(img_obj)
	
	
	def mirror(imagebytes):
		img_obj = Image.open(BytesIO(imagebytes))
		return ImageOps.mirror(img_obj)
	
	
	def invert(imagebytes):
		img_obj = Image.open(BytesIO(imagebytes))
		return ImageOps.invert(img_obj)
	
	
	def posterize(imagebytes, bits):
		img_obj = Image.open(BytesIO(imagebytes))
		return ImageOps.posterize(img_obj, bits)
	
	
	def solarize(imagebytes, threshold=128):
		img_obj = Image.open(BytesIO(imagebytes))
		return ImageOps.solarize(img_obj, threshold=threshold)
	
	
	def grayscale(imagebytes):
		img_obj = Image.open(BytesIO(imagebytes))
		return ImageOps.grayscale(img_obj)
	
	
	def unsharp(imagebytes, radius=2, percent=150, threshold=3):
		img_obj = Image.open(BytesIO(imagebytes))
		return img_obj.filter(ImageFilter.UnsharpMask(radius=radius, percent=percent, threshold=threshold))
	
	
	def gaussianblur(imagebytes, radius=2):
		img_obj = Image.open(BytesIO(imagebytes))
		return img_obj.filter(ImageFilter.GaussianBlur(radius=radius))
	
	
	def pixelize(imagebytes, bits=32, resize=True):
		img_obj = Image.open(BytesIO(imagebytes))
		imgSmall = img_obj.resize((bits, bits),resample=Image.BILINEAR)
		
		if resize is True:
			return imgSmall.resize(img_obj.size, Image.NEAREST)
		else:
			return imgSmall
	
	
	def image2ascii(imagebytes, ascii_chars):
		
		image = Image.open(BytesIO(imagebytes))
		
		ASCII_CHARS = []
		for i in ascii_chars:
			ASCII_CHARS.append(i.replace(' ', ''))
		new_width = 100
		
		width, height = image.size
		ratio = height/width
		new_height = int(new_width * ratio)
		resized_image = image.resize((new_width, new_height))
		
		
		grayscale_image = resized_image.convert("L")
		
		pixels = grayscale_image.getdata()
		characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
		
		pixel_count = len(characters)  
		ascii_image = "\n".join([characters[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
		
		return ascii_image