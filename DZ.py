summ = 0
comp = 1
# -----------------------------------------------------------------------
def dz1(bot, chat_id):
    dz1_ResponseHandler = lambda message: bot.send_message(chat_id, f"Твое имя в большом регистре! - {(message.text).upper()}! \n Твое имя в малом регистре! - {(message.text).lower()}")
    my_input(bot, chat_id, "Выведу твое имя с разным регистром", dz1_ResponseHandler)
# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    my_inputInt(bot, chat_id, "Выведу сумму и произведение цифр твоего возраста!", dz2_ResponseHandler)

def dz2_ResponseHandler(bot, chat_id, summ_age_int, comp_age_int):
    bot.send_message(chat_id, f"сумма - {summ_age_int}, произведение - {comp_age_int}")
# -----------------------------------------------------------------------
def dz3(bot, chat_id):
    bot.send_message(chat_id, text="ДОДЕЛАТЬ")
# -----------------------------------------------------------------------
def dz4(bot, chat_id):
    bot.send_message(chat_id, text="ДОДЕЛАТЬ")
# -----------------------------------------------------------------------
def dz5(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько вам лет?", dz5_ResponseHandler)

def dz5_ResponseHandler(bot, chat_id, age_int):
    bot.send_message(chat_id, text=f"О! тебе уже {age_int}! \nА через год будет уже {age_int+1}!!!")
# -----------------------------------------------------------------------
def dz6(bot, chat_id):
    dz6_ResponseHandler = lambda message: bot.send_message(chat_id, f"Добро пожаловать {message.text}! У тебя красивое имя, в нём {len(message.text)} букв!")
    my_input(bot, chat_id, "Как тебя зовут?", dz6_ResponseHandler)

# -----------------------------------------------------------------------
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

def summ_and_comp(age_int, summ_age_int, comp_age_int):
    while age_int > 0:
        summ_age_int += age_int % 10
        comp_age_int *= age_int % 10
        age_int //= 10
        return summ_age_int, comp_age_int
# -----------------------------------------------------------------------