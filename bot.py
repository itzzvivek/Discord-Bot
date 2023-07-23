import hikari

bot = hikari.GatewayBot(token='*********')

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print("Bot has started")

bot.run()
