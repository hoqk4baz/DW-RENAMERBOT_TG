from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *

@Client.on_message(filters.private & filters.command('isim_ekle'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Ayarlamam için bana bir başlık ver.\n\nÖrnek:- `/dosya_ismi DW Store`**")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**Dosya ismi başarıyla düzenlendi ✅**")

@Client.on_message(filters.private & filters.command('isim_sil'))
async def delete_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("**Herhangi bir özel başlığınız yok**")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("**Dosya ismi başarı ile silindi ✅**")
                                       
@Client.on_message(filters.private & filters.command('ismi_gör'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>Eklenen isim:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("**Herhangi bir özel başlığınız yok**")
          
