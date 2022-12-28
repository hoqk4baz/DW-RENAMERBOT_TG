import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit , usertype,addpre
ADMIN = str(os.environ.get("ADMIN"))
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["uyar"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("Kullanıcı Başarıyla Bildirildi")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("Kullanıcı Başarıyla Bildirilemedi 😔") 


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["premiumekle"]))
async def buypremium(bot, message):
	await message.reply_text("PLAN SEÇ.........",quote=True,reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("VIP 1",callback_data = "vip1"), 
        			InlineKeyboardButton("VIP 2",callback_data = "vip2") ]]))
        			

@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/premiumekle")
	user_id = id[1].replace(" ", "")
	inlimit  = 10737418240
	uploadlimit(int(user_id),10737418240)
	usertype(int(user_id),"VIP1")
	addpre(int(user_id))
	await update.message.edit("10 GB Premium Yükleme sınırın başarıyla eklendi")
	await bot.send_message(user_id,"Selam Dostum VIP 1'e Yükseltildin planını buradan kontrol et /planım")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/premiumekle")
	user_id = id[1].replace(" ", "")
	inlimit  = 53687091200
	uploadlimit(int(user_id),53687091200)
	usertype(int(user_id),"VIP2")
	addpre(int(user_id))
	await update.message.edit("50 GB Premium Yükleme sınırın başarıyla eklendi")
	await bot.send_message(user_id,"Selam Dostum VIP 2'ye Yükseltildin planını buradan kontrol et /planım")
