import whatsapp

bot     = whatsapp.bot()
bot.initialize()

def handle(msg):
	if msg == '/start':
		bot.sendMessage('Hello!')
	if msg == '/media':
		bot.sendMedia('/path/to/imagem.jpg')
		
bot.loop(handle)
