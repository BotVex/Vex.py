import aiohttp
from io import BytesIO
from typing import Union
from random import randint
from PIL import ImageColor
from colorir import sRGB, HSV
from colorthief import ColorThief


class Colors:
    GREEN = 0x71FF51
    YELLOW = 0xFFE251
    RED = 0xFF5151
    BLUE = 0x51A2FF
    BLACK = 0x3D3D3D
    PYTHON_BLUE = 0x4584B6
    PYTHON_YELLOW = 0xFFDE57


class ColorConverter:
    def __init__(self):
        pass

    def RGB2HEX(RGB: Union[tuple, list[int]]) -> tuple:
        return "".join(f"{i:02X}" for i in RGB)

    def HEX2RGB(HEX) -> tuple:
        return ImageColor.getcolor(HEX, "RGB")

    def HEX2RGBA(HEX) -> tuple:
        return ImageColor.getcolor(HEX, "RGBA")

    def RGB2HSVtuple(RGB: Union[tuple, list[int]]) -> tuple:
        r, g, b = RGB
        H, S, V = sRGB(r, g, b).hsv(round_to=1)
        return H, S, V

    def HSV2RGB(HSV_) -> tuple:
        h, s, v = HSV_
        R, G, B = HSV(h, s, v).sRGB()
        return R, G, B

    def DECIMAL2HEX(decimal: int) -> str:
        return hex(decimal)


class ColorGenerate:
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

        color = "".join(f"{i:02X}" for i in dominant)
        return int(color, 16)

    async def general_color_url(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(str(url)) as resp:
                img_file = await resp.content.read()

                color_thief = ColorThief(BytesIO(img_file))

                dominant = color_thief.get_color(quality=1)

                color = "".join(f"{i:02X}" for i in dominant)
                return int(color, 16)
