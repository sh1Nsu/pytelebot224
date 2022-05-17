
# -----------------------------------------------------------------------
def dz1(bot, chat_id):
    dz1_ResponseHandler = lambda message: bot.send_message(chat_id, f"Добро пожаловать {message.text}! У тебя красивое имя, в нём {len(message.text)} букв!")
    my_input(bot, chat_id, "Как тебя зовут?", dz1_ResponseHandler)
# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    dz2_ResponseHandler = lambda message: bot.send_message \
        (chat_id, f"От 2 до последнего символа - {((message.text)[1:-1])}. \n Задом наперед - {((message.text)[::-1])}. "
                  f"\n Последние три символа - {((message.text)[-3:])}. \n Первые 5 символов - {((message.text)[0:5])}")
    my_input(bot, chat_id, "Давай я изменю твоё имя, просто напиши его", dz2_ResponseHandler)
# -----------------------------------------------------------------------
def dz3(bot, chat_id):
    dz3_ResponseHandler = lambda message: \
        bot.send_message(chat_id, f"Твое имя в большом регистре! - {(message.text).upper()}! "
                                  f"\n Твое имя в малом регистре! - {(message.text).lower()}")
    my_input(bot, chat_id, "Выведу твое имя с разным регистром", dz3_ResponseHandler)
# -----------------------------------------------------------------------
def dz4(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько вам лет?", dz4_ResponseHandler)

def dz4_ResponseHandler(bot, chat_id, age_int):
    bot.send_message(chat_id, text=f"О! тебе уже {age_int}! \nА через год будет уже {age_int+1}!!!")
# -----------------------------------------------------------------------
def dz5(bot, chat_id):
    dz5_ResponseHandler = lambda message: bot.send_message(chat_id, f"Получай!{(message.text)*5}")
    my_input(bot, chat_id, "Давай я выведу твоё имя 5 раз!", dz5_ResponseHandler)
# -----------------------------------------------------------------------
def dz6(bot, chat_id):
    message = bot.send_message(chat_id, "Сколько будет 2+2*2?")
    bot.register_next_step_handler(message, dz6_register, bot)
# -----------------------------------------------------------------------
def dz7(bot, chat_id):
    message = bot.send_message(chat_id, "Давай вычислим сумму и произведение цифр твоего возраста!")
    bot.register_next_step_handler(message, dz7_register, bot)
# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)
# -----------------------------------------------------------------------
def my_inputInt(bot, chat_id, txt, ResponseHandler):

    # bot.send_message(chat_id, text=botGames.GameRPS_Multiplayer.name, reply_markup=types.ReplyKeyboardRemove())

    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt, ResponseHandler=ResponseHandler)
    # bot.register_next_step_handler(message, my_inputInt_return, bot, txt, ResponseHandler)  # то-же самое, но короче

def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        if message.content_type != "text":
            raise ValueError
        var_int = int(message.text)
        # данные корректно преобразовались в int, можно вызвать обработчик ответа, и передать туда наше число
        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                         text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)
# -----------------------------------------------------------------------
def dz6_register(message, bot):
    while True:
        answer = int(message.text)
        if answer != 6:
            bot.send_message(message.chat.id, "Неправильно!")
            break
        else:
            bot.send_message(message.chat.id, "Ответ верный, молодец!")
            break
# -----------------------------------------------------------------------
def dz7_register(message, bot):
    summ = 0
    composition = 1
    message_int = int(message.text)
    while message_int > 0:
        summ += message_int % 10
        composition *= message_int % 10
        message_int //= 10
    bot.send_message(message.chat.id, f"Сумма цифр в твоем возрасте - {(summ)}")
    bot.send_message(message.chat.id, f"Произведение цифр в твоем возрасте - {(composition)}")
# -----------------------------------------------------------------------