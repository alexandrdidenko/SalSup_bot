from telebot import types

'''
# Using the ReplyKeyboardMarkup class
# It's constructor can take the following optional arguments:
# - resize_keyboard: True/False (default False)
# - one_time_keyboard: True/False (default False)
# - selective: True/False (default False)
# - row_width: integer (default 3)
# row_width is used in combination with the add() function.
# It defines how many buttons are fit on each row before continuing on the next row.
'''

markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=1)  # , one_time_keyboard=True, )
itembtn1 = types.KeyboardButton(text='/infocheck')
itembtn2 = types.KeyboardButton('/prim_sec_sales')
itembtn3 = types.KeyboardButton('/cube_sales')
itembtn4 = types.KeyboardButton('/DD_chek')
itembtn5 = types.KeyboardButton('/sync')
# itembtn6 = types.KeyboardButton('test')
itembtn7 = types.KeyboardButton('/export')

markup.add(itembtn1,
           itembtn2,
           itembtn3,
           itembtn4,
           itembtn5,
           # itembtn6,
           itembtn7)
