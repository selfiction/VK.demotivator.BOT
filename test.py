from vkbottle import *
from vkbottle.bot import *
from simpledemotivators import *
import aiofiles as aiof
import requests




bot = Bot('***')

FILENAMED = "image.jpg"
FILENAMEQ = "image.jpg"



@bot.on.message(text="d <f> <s>")
async def readme_handler(m: Message, f, s):
    urlpic = m.attachments[0].photo.sizes[-5].url
    print(urlpic)
    img_data = requests.get(urlpic).content


    async with aiof.open(FILENAMED, mode='wb') as out:

        await out.write(img_data)
    dem = Demotivator(f, s)  # 2 строчки
    dem.create('image.jpg')
    photo = await PhotoMessageUploader(bot.api).upload(
        "demresult.jpg", peer_id=m.peer_id
    )
    await m.answer(attachment=photo)

@bot.on.message(text="q <f>")
async def readme_handler(m: Message, f):
    users_info = await bot.api.users.get(m.from_id)
    urlpic = m.attachments[0].photo.sizes[-5].url
    print(urlpic)
    img_data = requests.get(urlpic).content


    async with aiof.open(FILENAMEQ, mode='wb') as out:
        await out.write(img_data)
    quot = Quote(f, author_name=users_info[0].first_name)  # 2 строчки
    quot.create('image.jpg')
    photo = await PhotoMessageUploader(bot.api).upload(
        "qresult.png", peer_id=m.peer_id
    )
    await m.answer(attachment=photo)

bot.run_forever()

