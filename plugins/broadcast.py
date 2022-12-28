import os
from pyrogram.errors import FloodWait
import asyncio
from pyrogram import Client ,filters
from helper.database import getid ,delete
import time
ADMIN = int(os.environ.get("ADMIN"))
 

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["duyur"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Tüm kimlikler veritabanından alçekiliyor ...........")
   ids = getid()
   tot = len(ids)
   success = 0 
   failed = 0 
   await ms.edit(f"Duyuru başlatıldı .... \n Toplam Duyurulacak kişi sayısı : {tot}")
   for id in ids:
     try:
     	time.sleep(1)
     	await message.reply_to_message.copy(id)
     	success += 1 
     except:
     	failed += 1
     	delete({"_id":id})     	 
     	pass
     try:
     	await ms.edit( f"Mesa başarı ile {success} kişiye iletildi. {failed} 'kişiye iletilemedi (Bot'u bıraktılar). \nToplam - {tot}" )
     except FloodWait as e:
     	await asyncio.sleep(t.x)
