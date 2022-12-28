from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *

@Client.on_message(filters.private & filters.command('aciklama_ekle'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**Ayarlamam için bana bir açıklama ver.\n\nÖrnek:- `/aciklama_ekle DW Store`**")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**Dosya açıklaması başarıyla düzenlendi ✅**")

@Client.on_message(filters.private & filters.command('aciklama_sil'))
async def delete_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("**Herhangi bir özel açıklama yok**")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("**Dosya açıklaması başarı ile silindi ✅**")
                                       
@Client.on_message(filters.private & filters.command('aciklamayi_gör'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>Eklenen açıklama:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("**Herhangi bir özel açıklama yok**")
          
