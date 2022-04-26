from typing import Any, Dict, Optional, List, Union
import asyncio

import disnake
from disnake import ApplicationCommandInteraction, MessageInteraction

# https://github.com/Kraots/ViHillCorner/blob/master/utils/paginator.py#L367-L448


class EmbedPaginator(disnake.ui.View):
    def __init__(
        self,
        ctx,
        embeds: List[disnake.Embed],
        *,
        timeout: float = 30.0
    ):
        super().__init__(timeout=timeout)
        self.ctx = ctx
        self.embeds = embeds
        self.current_page = 0

    async def interaction_check(self, interaction: MessageInteraction) -> bool:
        if interaction.user and interaction.user.id in (self.ctx.bot.user.id, self.ctx.author.id):
            return True
        await interaction.response.send_message('hmmmmmmmm\nparece que você não pode controlar esse menu...', ephemeral=True)
        return False

    async def on_timeout(self) -> None:
        if self.message:
            await self.message.edit(view=None)

    async def show_page(self, inter: MessageInteraction, page_number: int):
        if (
            (page_number < 0) or
            (page_number > len(self.embeds) - 1)
        ):
            if not inter.response.is_done():
                await inter.response.defer()
            return
        self.current_page = page_number
        embed = self.embeds[page_number]
        embed.set_footer(text=f'Página {self.current_page + 1}/{len(self.embeds)}')
        if inter.response.is_done():
            await self.message.edit(embed=embed)
        else:
            await inter.response.edit_message(embed=embed)

    @disnake.ui.button(label='≪', style=disnake.ButtonStyle.grey)
    async def go_to_first_page(self, button: disnake.ui.Button, interaction: MessageInteraction):
        """Go to the first page."""

        await self.show_page(interaction, 0)

    @disnake.ui.button(label='anterior', style=disnake.ButtonStyle.blurple)
    async def go_to_previous_page(self, button: disnake.ui.Button, interaction: MessageInteraction):
        """Go to the previous page."""

        await self.show_page(interaction, self.current_page - 1)

    @disnake.ui.button(label='próximo', style=disnake.ButtonStyle.blurple)
    async def go_to_next_page(self, button: disnake.ui.Button, interaction: MessageInteraction):
        """Go to the next page."""

        await self.show_page(interaction, self.current_page + 1)

    @disnake.ui.button(label='≫', style=disnake.ButtonStyle.grey)
    async def go_to_last_page(self, button: disnake.ui.Button, interaction: MessageInteraction):
        """Go to the last page."""

        await self.show_page(interaction, len(self.embeds) - 1)

    @disnake.ui.button(label='sair', style=disnake.ButtonStyle.red)
    async def stop_pages(self, button: disnake.ui.Button, interaction: MessageInteraction):
        """Stops the pagination session."""

        await interaction.response.defer()
        await interaction.delete_original_message()
        self.stop()

    async def start(self):
        """Start paginating over the embeds."""
        embed = self.embeds[0]
        embed.set_footer(text=f'Página 1/{len(self.embeds)}')
        if isinstance(self.ctx, ApplicationCommandInteraction):
            if not self.ctx.response.is_done():
                self.message = await self.ctx.response.send_message(embed=embed, view=self)
            else:
                self.message = await self.ctx.followup.send(embed=embed, view=self)
            return
        self.message = await self.ctx.send(embed=embed, view=self)