import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["hakkında"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Toplam kullanıcılar:  {total_user()}\nBot : @dwrenamer_bot\nYapımcı : @dark_enza\nKodlama Dili : Python3\nKütüphane :  Pyrogram 2.0\nSunucu :  Heroku\nYeniden Adlandırılan Toplam Dosya Sayısı: {total_rename}\nToplam Dosya boyutu :- {humanbytes(int(total_size))} ",quote=True)
