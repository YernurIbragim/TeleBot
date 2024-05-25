import telebot
from telebot import types
import io
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

bot = telebot.TeleBot("xxx")            #Instead of xxx write Bot's Token
toChat = "xxx"          #Instead of xxx write Telegram Chat's Id

#Statistics is still work in progress!

def check(message):
    if message.text == "Anonymous submission" or message.text == "Non-anonymous submission" or "/stats1376":
            return True
    else:
        bot.send_message(message.chat.id, "I do not understand command/text that you sent to me. Please, choose commands from the pop-up keyboard.")

def reviewAN(message):
    if message.content_type == "text":
        message_to_forward = f"Received feedback, anonymous: \n \n \n \n{message.text}"
        if message.text == "Anonymous submission":
            kb = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text = "Yes", callback_data = "Yes")
            btn2 = types.InlineKeyboardButton(text = "No", callback_data = "No")
            kb.add(btn1, btn2)
            bot.send_message(message.chat.id, "You wrote \"Anonymous submission\" two times, are you sure that you want to send it?", reply_markup=kb)
            @bot.callback_query_handler(func=lambda callback: callback.data)
            def check1(callback):
                if callback.data == "Yes":
                    bot.send_message(toChat, message_to_forward)
                else:
                    bot.send_message(message.chat.id, "Send another message!")
                    return
        else:
            bot.send_message(toChat, message_to_forward)
            kb = types.InlineKeyboardMarkup(row_width = 1)
            btn1 = types.InlineKeyboardButton(text = "Out telegram channel", url="xxx")
            kb.add(btn1)
            bot.send_message(message.chat.id, "Your request has been sent. Thank you!\n\n\n<b>Be advised that we will not contact you since we don't have your info. But, we will look into your request.</b>", reply_markup=kb, parse_mode= "HTML")
    elif message.content_type == 'photo':
        bot.send_message(toChat, "Received anonymous feedback:")
        bot.send_photo(toChat, message.photo[-1].file_id)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Out telegram channel", url="xxx")
        kb.add(btn1)
        bot.send_message(message.chat.id, "Your request has been sent. Thank you!\n\n\n<b>Be advised that we will not contact you since we don't have your info. But, we will look into your request.</b>", reply_markup=kb, parse_mode= "HTML")
    elif message.content_type == "document":
        bot.send_message(toChat, "Received anonymous feedback:")
        bot.send_document(toChat, message.document.file_id)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Out telegram channel", url="xxx")
        kb.add(btn1)
        bot.send_message(message.chat.id, "Your request has been sent. Thank you!\n\n\n<b>Be advised that we will not contact you since we don't have your info. But, we will look into your request.</b>", reply_markup=kb, parse_mode= "HTML")
    elif message.content_type == "audio":
        bot.send_message(toChat, "Received anonymous feedback:")
        bot.send_audio(toChat, message.audio.file_id)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Out telegram channel", url="xxx")
        kb.add(btn1)
        bot.send_message(message.chat.id, "Your request has been sent. Thank you!\n\n\n<b>Be advised that we will not contact you since we don't have your info. But, we will look into your request.</b>", reply_markup=kb, parse_mode= "HTML")
    elif message.content_type == "video":
        bot.send_message(toChat, "Received anonymous feedback:")
        bot.send_video(toChat, message.video.file_id)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Out telegram channel", url="xxx")
        kb.add(btn1)
        bot.send_message(message.chat.id, "Your request has been sent. Thank you!\n\n\n<b>Be advised that we will not contact you since we don't have your info. But, we will look into your request.</b>", reply_markup=kb, parse_mode= "HTML")
    elif message.content_type == "voice":
        bot.send_message(toChat, f"Received feedback, anonymous.")
        bot.send_voice(toChat, message.voice.file_id)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Out telegram channel", url="xxx")
        kb.add(btn1)
        bot.send_message(message.chat.id, "Your request has been sent. Thank you!\n\n\n<b>Be advised that we will not contact you since we don't have your info. But, we will look into your request.</b>", reply_markup=kb, parse_mode= "HTML")

def reviewNAN(message):
    if message.content_type == "text":
        message_to_forward = f"Received feedback\nFrom @{message.from_user.username}\n \n \n{message.text}"
        if message.text == "Non-anonymous submission":
            kb = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text="Yes", callback_data="Yes")
            btn2 = types.InlineKeyboardButton(text="No", callback_data="No")
            kb.add(btn1, btn2)
            bot.send_message(message.chat.id,
                             "You wrote \"Non-anonymous submission\" two times, are you sure that you want to send it?",
                             reply_markup=kb)
            @bot.callback_query_handler(func=lambda callback: callback.data)
            def check2(callback):
                if callback.data == "Yes":
                    bot.send_message(toChat, message_to_forward)
                else:
                    bot.send_message(message.chat.id, "Send another message!")
                    return
        else:
            bot.send_message(toChat, message_to_forward)
            kb = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton(text="Out telegram channel", url="xxx")
            kb.add(btn1)
            bot.send_message(message.chat.id, "Your request has been sent. We will contact you shortly through your telegram username. Thank you!", reply_markup=kb)
    elif message.content_type == 'photo':
        bot.send_message(toChat, f"Received feedback\nFrom @{message.from_user.username}")
        bot.send_photo(toChat, message.photo[-1].file_id)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Out telegram channel", url="xxx")
        kb.add(btn1)
        bot.send_message(message.chat.id,
                         "Your request has been sent. We will contact you shortly through your telegram username. Thank you!",
                         reply_markup=kb)
    elif message.content_type == "document":
        bot.send_message(toChat, f"Received feedback\nFrom @{message.from_user.username}")
        bot.send_document(toChat, message.document.file_id)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Out telegram channel", url="xxx")
        kb.add(btn1)
        bot.send_message(message.chat.id,
                         "Your request has been sent. We will contact you shortly through your telegram username. Thank you!",
                         reply_markup=kb)
    elif message.content_type == "audio":
        bot.send_message(toChat, f"Received feedback\nFrom @{message.from_user.username}")
        bot.send_audio(toChat, message.audio.file_id)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Out telegram channel", url="xxx")
        kb.add(btn1)
        bot.send_message(message.chat.id,
                         "Your request has been sent. We will contact you shortly through your telegram username. Thank you!",
                         reply_markup=kb)
    elif message.content_type == "video":
        bot.send_message(toChat, f"Received feedback\nFrom @{message.from_user.username}")
        bot.send_video(toChat, message.video.file_id)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Out telegram channel", url="xxx")
        kb.add(btn1)
        bot.send_message(message.chat.id,
                         "Your request has been sent. We will contact you shortly through your telegram username. Thank you!",
                         reply_markup=kb)
    elif message.content_type == "voice":
        bot.send_message(toChat, f"Received feedback\nFrom @{message.from_user.username}")
        bot.send_voice(toChat, message.voice.file_id)
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text="Out telegram channel", url="xxx")
        kb.add(btn1)
        bot.send_message(message.chat.id,
                         "Your request has been sent. We will contact you shortly through your telegram username. Thank you!",
                         reply_markup=kb)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.type != 'private':
        bot.send_message(message.chat.id, "Please, send your message through my DMs")
        return
    kb = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton(text="Anonymous submission")
    btn2 = types.KeyboardButton(text="Non-anonymous submission")
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id, "Dear student, \n"
                          "What type of submission would you like to make? \n"
                          "Use keyboard to choose type of submission \n", reply_markup=kb)

caseCounter = 0
df = pd.DataFrame(columns=['Date', 'Case Count'])

@bot.message_handler(func=lambda message: check(message))
def handle_All(message):
    global caseCounter
    global df
    if message.chat.type != 'private':
        bot.send_message(message.chat.id, "Please, send your message through my DMs")
        return
    if message.text == "Anonymous submission":
        bot.send_message(message.chat.id, "<b>NOTE!!!!! \n \nIf you are sending any type of media through this chat and need to send text with it, send photo and text in separate submissions. \nOtherwise, we won't get them</b>", parse_mode = "HTML")
        sent = bot.reply_to(message, "You chose anonymous submission. \n"
                                     "Please, enter your request:")
        bot.register_next_step_handler(sent, reviewAN)
        caseCounter+=1
    if message.text == "Non-anonymous submission":
        bot.send_message(message.chat.id, "<b>NOTE!!!!! \n \nIf you are sending any type of media through this chat and need to send text with it, send photo and text in separate submissions. \nOtherwise, we won't get them</b>", parse_mode="HTML")
        sent = bot.reply_to(message, "You chose non-anonymous submission. \n"
                                 "Please, enter your request:")
        bot.register_next_step_handler(sent, reviewNAN)
        caseCounter=+1
    if message.text == "/stats1376":
        if (message.from_user.id == 5063012645): #5 in the end removed
            bot.send_message(message.chat.id, "Loading statistics...")
            buf = io.BytesIO()
            plt.figure(figsize=(12, 6))
            plt.plot('Date', 'caseCounter', data=df, marker='o', markerfacecolor='blue', markersize=12, color='skyblue',
                     linewidth=4)
            plt.ylabel = "Cases"
            plt.xlabel = "Date"
            plt.savefig(buf, format='png')
            buf.seek(0)
            bot.send_photo(message.chat.id, buf)
        else:
            bot.send_message(message.chat.id,
                             "How do you know about this function? Never use it again.\n\n\n<b>NOTE: Accesing any data from Student Government or University Authorities is punishable.</b>",
                             parse_mode="HTML")
            bot.send_message(message.chat.id, f"This user id is: {message.from_user.id}")


df = pd.concat([df, pd.DataFrame({'Date': [datetime.now()], 'caseCounter': [caseCounter]})], ignore_index=True)


bot.infinity_polling()