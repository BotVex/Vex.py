import disnake


class Confirm(disnake.ui.View):
		def __init__(self):
				super().__init__()
				self.value = None


		@disnake.ui.button(label='sim', style=disnake.ButtonStyle.green)
		async def confirm(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
				self.value = True
				self.stop()

	
		@disnake.ui.button(label='não', style=disnake.ButtonStyle.red)
		async def cancel(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
				self.value = False
				self.stop()
