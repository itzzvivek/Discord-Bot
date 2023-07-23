import hikari
import lightbulb

bot = lightbulb.BotApp(
    token='***********', 
    default_enabled_guilds=(***********))


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Bot has started!")

@bot.command
@lightbulb.command('ping','Says Pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

bot.run()
