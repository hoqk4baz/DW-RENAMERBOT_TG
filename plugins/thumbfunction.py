from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

@Client.on_message(filters.private & filters.command(['arkaplanı_gor']))
async def viewthumb(client,message):
		print(message.chat.id)
		thumb = find(int(message.chat.id))[0]
		if thumb :
			await client.send_photo(message.chat.id,photo =f"{thumb}")
		else:
			await message.reply_text("**Herhangi bir özel küçük resminiz yok**")
	
	
@Client.on_message(filters.private & filters.command(['arkaplanı_sil']))
async def removethumb(client,message):
	delthumb(int(message.chat.id))
	await message.reply_text("**Özel küçük resim başarıyla silindi**")

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
	file_id = str(message.photo.file_id)
	addthumb(message.chat.id , file_id)
	await message.reply_text("**Özel küçük resim başarıyla kaydedildi** ✅")
	
