from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.command('start'))
async def command(b, m:Message):
    await m.reply_text(
        text="""👋 Hello {},
        
🤖 My Name is Hagadmansa Mega Bot, I can stream Telegram Files over HTTP.

🧐 Don't know how to do? No worries, just press the help button.

👨‍💻 My Creator is <a href=https://t.me/hagadmansa>Hagadmansa</a>.""".format(m.from_user.mention),
        reply_markup=InlineKeyboardMarkup
        ([[
            InlineKeyboardButton('🌐 Website', url='https://hagadmansa.com'),
            InlineKeyboardButton('📣 Updates', url='https://t.me/hagadmansa')
            ],[
            InlineKeyboardButton('ℹ️ Help', callback_data='help'),
            InlineKeyboardButton('😊 About', callback_data='about')
        ]]),
        disable_web_page_preview=True,
    )
     
@StreamBot.on_message(filters.command('help'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>ℹ️ HELP</b>
        
Here is the list of my commands, please read carefully everything. if anything happened to you then we are not responsible.""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('❓ How to use me', callback_data='howtouseme')
            ],[
            InlineKeyboardButton('⚙️ Instructions', callback_data='instructions'),
            InlineKeyboardButton('🕹 Tutorials', callback_data='tutorials'),
            ],[
            InlineKeyboardButton('🔙 Back', callback_data='home'),
            InlineKeyboardButton('📣 Channel', url='https://t.me/hagadmansa')
        ]]
    ),
        disable_web_page_preview=True,
    )
    
@StreamBot.on_message(filters.command('howtouseme'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>ℹ️ Help</b> > How To Use Me
        
My name is Hagadmansa Mega Bot, I am a member of Hagadmansa family. I can provide you direct download link of any telegram file/media. If you send me any file/media I will give an external download link, you can use that link to download any file outside telegram. My link is supported in any browser.

• Send me any file/media from Telegram.
• I Will provide an external download link for you.
• All links will be permanent and have the fastest speed.

<b>🔞 Warning:</b>

• 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this.""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='help'),
            InlineKeyboardButton('🏠 Home', callback_data='home')
            ]]
    ),
        disable_web_page_preview=True,
    )
    
@StreamBot.on_message(filters.command('instructions'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>ℹ️ Help</b> > Instructions
        
1. Don't send photos to the bot, send them as a file.
2. Don't send multiple files at a time, send them one by one.

<b>🔞 Warning:</b>

• 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this.""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='help'),
            InlineKeyboardButton('🏠 Home', callback_data='home')
            ]]
    ),
        disable_web_page_preview=True,
    )

@StreamBot.on_message(filters.command('instructions'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>ℹ️ Help</b> > Tutorials
        
All tutorials related to Bots, Website, Movies and etc, will be updated here. Till then you can visit my movie website <b>www.hagadmansa.com</b> to watch movies. Don't forget to subscribe my updates channel <b>@hagadmansa</b>.

<b>🔞 Warning:</b>

• 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this.""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='help'),
            InlineKeyboardButton('🏠 Home', callback_data='home')
            ]]
    ),
        disable_web_page_preview=True,
    )
