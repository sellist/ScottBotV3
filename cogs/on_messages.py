from discord.ext import commands

from services.NameService import NameService


class NameCommands(commands.Cog):
    """
    Organization of events that will trigger using ! commands
    """

    def __init__(self, bot):
        self.nameService = NameService()

    @commands.command()
    async def test(self, ctx):
        await ctx.send(f'I saw someone say {ctx.message.content} from {ctx.message.author.id}')

    @commands.command()
    async def addname(self, ctx):

        """
        :param ctx: message
        :return: none
        """
        count = 0
        print(ctx.message.content.split())
        x: str
        for x in ctx.message.content.split()[1:]:
            try:
                self.nameService.add_name(str(x.title()))
                count+=1
            except Exception as e:
                print(e)
                print(f"{x} isn't valid")

        if count >= 1:
            await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
        else:
            await ctx.message.add_reaction('\N{THUMBS DOWN SIGN}')

    @commands.command()
    async def name(self, ctx):
        await ctx.message.channel.send(self.nameService.get_name())

    @commands.command()
    async def couple(self,ctx):
        first = self.nameService.get_name()
        second = self.nameService.get_name()
        await ctx.send(
            f"{first} and {second}"
        )

    @commands.command()
    async def namehelp(self, ctx):
        await ctx.send(
            """Use !name to generate a name \nUse !addname to add a name to the list of names to be generated from""")


def setup(bot):
    bot.add_cog(NameCommands(bot))


if __name__ == '__main__':
    print("This is the on_messages module in the on_events package")
