import random

def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)

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

def game(bot, chat_id):
   bot.register_next_step_handler(game_register, bot)


def game_register(message, bot):
    @bot.message_handler(commands=['start'])
    def welcome(message, where_call=None):
        if where_call is None:
            global number
            number = random.randint(1, 30)
            msg = bot.send_message(message.chat.id, 'Сможешь угадать число между 1 и 30?')
            attempt = 1
            bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))

        elif where_call == 'not_digit':
            msg = bot.send_message(message.chat.id, 'только числа')
            attempt = 1
            bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))


    def random_number(message, attempt):
        if message.text.isdigit():
            n = int(message.text)
            if attempt < 6:
                attempt += 1
                if n < number:
                    msg = bot.send_message(message.chat.id, 'мало\nещё')
                    bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))

                elif n > number:
                    msg = bot.send_message(message.chat.id, 'много\nещё')
                    bot.register_next_step_handler(msg, lambda message: random_number(message, attempt))
                else:
                    bot.send_message(message.chat.id, 'угадал, с {} попытки!'.format(attempt - 1))
            else:
                bot.send_message(message.chat.id, 'попытки исчерпаны\nзагаданное число {0}'.format(number))
        else:
            welcome(message, where_call='not_digit')