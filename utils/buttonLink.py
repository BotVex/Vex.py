import disnake

class ButtonLink(disnake.ui.View):
	def __init__(self, label, url):
		super().__init__()
		self.button_label = label
		self.button_url = url
		self.add_item(
			disnake.ui.Button(
				style=disnake.ButtonStyle.link,
				label=self.button_label,
				url=self.button_url
			)
		)