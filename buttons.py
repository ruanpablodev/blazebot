from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def linkdouble():
	markup = InlineKeyboardMarkup()

	btn = InlineKeyboardButton("---🎰 JOGUE AQUI 🎰---", url='https://blaze.com/pt/games/double')
	markup.add(btn)

	btn = InlineKeyboardButton("---📊 ESTATISTICAS 📊---", url='https://t.me/estatisticasthunder')

	markup.add(btn)

	return markup