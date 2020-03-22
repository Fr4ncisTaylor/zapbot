"""
change only the [contact] and [path] fields, 
change the others only if you are absolutely 
sure of what you are doing!!!
"""

contact         = "MY CONTACT"
path            = "/path/to/chromedriver"

#____________________________________________#
## DO NOT MODIFY ##
webWhatsapp     = "https://web.whatsapp.com/"
classes = dict(
	msg_text    = "-N6Gq",
	msg_box     = "_13mgZ",
	send_button = "_3M-N-",
	search_box  = "_3u328",
	)

css = dict(
	left_msg     = "span.selectable-text",
	media_button = "span[data-icon='clip']",
	media_input  = "input[type='file']",
	send_button  = "//div[contains(@class, 'yavlE')]",

	)
