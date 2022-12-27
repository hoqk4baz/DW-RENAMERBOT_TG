from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Bağlantınızı Paylaşın" ,url=f"https://t.me/share/url?url=https://t.me/dwrenamer_bot?start={message.from_user.id}") ]   ])
    await message.reply_text(f"Tavsiye Edin Kazanın 100MB Yükleme Limiti Alın\nReferans başına 100 MB\n Your Link :- https://t.me/dwrenamer_bot?start={message.from_user.id} ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    
