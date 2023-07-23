import hikari

bot = hikari.GatewayBot(token='MTEzMTg1NTc5ODU4MzE4NTQ5MA.GzwCdF.98XV-duElUrd-AFVn0SXTDj36tMLYimqlaH1YU')

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print("Bot has started")

bot.run()
