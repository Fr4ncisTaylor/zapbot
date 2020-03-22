import whatsapp

bot     = whatsapp.bot()
bot.initialize()

def handle(msg):
	if msg == '/start':
		bot.sendMessage('Hello!')

bot.loop(handle)