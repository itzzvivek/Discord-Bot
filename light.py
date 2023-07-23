import hikari
import lightbulb

bot = lightbulb.BotApp(
    token='MTEzMTg1NTc5ODU4MzE4NTQ5MA.Gres6b.H0XRvIDxhdXIiQ6jkMSuRo8d9c9C4BLpSEcZ7c', 
    default_enabled_guilds=(1131855540633489528))


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Bot has started!")

@bot.command
@lightbulb.command('ping','Says Pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

bot.run()
