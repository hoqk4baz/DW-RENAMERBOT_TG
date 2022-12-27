"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**ÜCRETSİZ KULLANICI PLANI**
	Günlük Yükleme Limiti 2GB
	FİYAT 0
	
	**VIP 1 ** 
	Günlük YÜkleme Limiti 10GB
	Fiyat 20 TL/AY
	
	**VIP 2 **
	Günlük Yükleme Limiti 50GB
	Fiyat 50 TL/AY
	
	**VIP3**
	Günlük Yükleme Limiti 100GB
	Fiyat 100TL/AY
	
        Satın Almak için Aşağıdan iletişime Geç"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN",url = "https://t.me/dark_enza")],[InlineKeyboardButton("Vazgeç",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**ÜCRETSİZ KULLANICI PLANI**
	Günlük Yükleme Limiti 2GB
	FİYAT 0
	
	**VIP 1 ** 
	Günlük YÜkleme Limiti 10GB
	Fiyat 20 TL/AY
	
	**VIP 2 **
	Günlük Yükleme Limiti 50GB
	Fiyat 50 TL/AY
	
	**VIP3**
	Günlük Yükleme Limiti 100GB
	Fiyat 100TL/AY
	
        Satın Almak için Aşağıdan iletişime Geç"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mrlokaman")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
