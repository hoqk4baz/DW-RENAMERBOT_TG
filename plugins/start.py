import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.progress import humanbytes

from helper.database import  insert ,find_one,used_limit,usertype,uploadlimit,addpredata,total_rename,total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import add_date ,check_expi
CHANNEL = os.environ.get('CHANNEL',"")
import datetime
from datetime import date as date_
STRING = os.environ.get("STRING","")
log_channel = int(os.environ.get("LOG_CHANNEL",""))
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]

#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
	wish = "Günaydın."
elif 12 <= currentTime.hour < 12:
	wish = 'Tünaydın.'
else:
	wish = 'İyi Akşamlar.'

#-------------------------------

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	old = insert(int(message.chat.id))
	try:
	    id = message.text.split(' ')[1]
	except:
	    await message.reply_text(text =f"""
	Selam {wish} {message.from_user.first_name }
	__Ben Dosyaları Yeniden Adlandırmaya Yarayan Botum\n 
	**Belge veya Video** ilet veya gönder\nArdından Yeniden adlandırmak için Dosya ismi girin__
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("BOT SAHİBİ KANAL" ,url="https://t.me/dwstoree") ], 
	[InlineKeyboardButton("YAPIMCI", url="https://t.me/dark_enza") ]  ]))
	    return
	if id:
	    if old == True:
	        try:
	            await client.send_message(id,"Arkadaşınız Zaten Botumuzu Kullanıyor")
	            await message.reply_text(text =f"""
	Selam  {wish} {message.from_user.first_name }
	__Ben Dosyaları Yeniden Adlandırmaya Yarayan Botum\n 
	**Belge veya Video** ilet veya gönder\nArdından Yeniden adlandırmak için Dosya ismi girin__
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("BOT SAHİBİ KANAL" ,url="https://t.me/dwstoree") ], 
	[InlineKeyboardButton("YAPIMCI", url="https://t.me/dark_enza") ]  ]))
	        except:
	             return
	    else:
	         await client.send_message(id,"Tebrikler! 100MB Yükleme sınırı kazandınız")
	         _user_= find_one(int(id))
	         limit = _user_["uploadlimit"]
	         new_limit = limit + 104857600
	         uploadlimit(int(id),new_limit)
	         await message.reply_text(text =f"""
	Selam {wish} {message.from_user.first_name }
	__Ben Dosyaları Yeniden Adlandırmaya Yarayan Botum\n 
	**Belge veya Video** ilet veya gönder\nArdından Yeniden adlandırmak için Dosya ismi girin__
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("BOT SAHİBİ KANAL" ,url="https://t.me/dwstoree") ], 
	[InlineKeyboardButton("YAPIMCI", url="https://t.me/dark_enza") ]  ]))
	         



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("**__kanalıma abone değilsin__** ",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("BOT SAHİBİ KANAL" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       try:
	   bot_data = find_one(int(botid))
           prrename = bot_data['total_rename']
           prsize = bot_data['total_size']
           user_deta = find_one(user_id)
       except:
	    await message.reply_text("Kullanmadan önce Hakkında konusunu okuyun /hakkında")
       try:
       	used_date = user_deta["date"]
       	buy_date= user_deta["prexdate"]
       	daily = user_deta["daily"]
	user_type = user_deta["usertype"]
       except:
           await message.reply_text("veritabanı temizlendi /start'a tıklayın")
           return
           
           
       c_time = time.time()
       
       if buy_date==None:
           LIMIT = 350
       else:
           LIMIT = 50
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"```Üzgünüm Dostum, sadece SENİN için değilim \n Floadwait aktif, bu yüzden lütfen bekleyin {ltime}```",reply_to_message_id = message.id)
       else:
       		# Forward a single message
       		await client.forward_messages(log_channel, message.from_user.id, message.id)
       		await client.send_message(log_channel,f"Kullanıcı Id :- {user_id}")       		
       		media = await client.get_messages(message.chat.id,message.id)
       		file = media.document or media.video or media.audio 
       		dcid = FileId.decode(file.file_id).dc_id
       		filename = file.file_name
       		value = 2147483648
       		used_ = find_one(message.from_user.id)
       		used = used_["used_limit"]
       		limit = used_["uploadlimit"]
       		expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
       		if expi != 0:
       			today = date_.today()
       			pattern = '%Y-%m-%d'
       			epcho = int(time.mktime(time.strptime(str(today), pattern)))
       			daily_(message.from_user.id,epcho)
       			used_limit(message.from_user.id,0)			     		
       		remain = limit- used
       		if remain < int(file.file_size):
       		    await message.reply_text(f"Afedersiniz! Şundan daha büyük dosyaları yükleyemiyorum: {humanbytes(limit)}. Dosya boyutu algılandı {humanbytes(file.file_size)}\nKullanılan Günlük Limit {humanbytes(used)} Büyük Dosyayı Yeniden Adlandırmak İstiyorsanız Planınızı Yükseltin ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("PLAN YÜKSELT 💰💳",callback_data = "upgrade") ]]))
       		    return
       		if value < file.file_size:
       		    if STRING:
       		        if buy_date==None:
       		            await message.reply_text(f" Limitten Daha Fazla Yükleyemezsiniz {humanbytes(limit)} Kullanılan Günlük Limit {humanbytes(used)} ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("PLAN YÜKSELT 💰💳",callback_data = "upgrade") ]]))
       		            return
       		        pre_check = check_expi(buy_date)
       		        if pre_check == True:
       		            await message.reply_text(f"""__Bu dosyayla ne yapmamı istiyorsun?__\n**Dosya ismi** :- {filename}\n**Dosya Boyutu** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Yeniden Adlandır",callback_data = "rename"),InlineKeyboardButton("✖️ Vazgeç",callback_data = "cancel")  ]]))
       		            total_rename(int(botid),prrename)
       		            total_size(int(botid),prsize,file.file_size)
       		        else:
       		            await message.reply_text(f'PLANINIZIN DOLMASINA KALAN {buy_date}',quote=True)
       		            return
       		    else:
       		          	await message.reply_text("2GB'tan büyük dosyalar yüklenemez ")
       		          	return
       		else:
       		    filesize = humanize.naturalsize(file.file_size)
       		    fileid = file.file_id
       		    total_rename(int(botid),prrename)
       		    total_size(int(botid),prsize,file.file_size)
       		    await message.reply_text(f"""__Bu dosyayla ne yapmamı istiyorsun?__\n**Dosya İsmi** :- {filename}\n**Dosya Boyutu** :- {filesize}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 Yeniden Adlandır",callback_data = "rename"),
       		InlineKeyboardButton("✖️ Vazgeç",callback_data = "cancel")  ]]))
       		
