from vkbottle import *
from vkbottle.bot import *
from simpledemotivators import *
import aiofiles as aiof
import requests




bot = Bot('a258ce79183e84321e497ba133ca1a7e19129308f548cacef46b9fefc88b2a8899410c383ce278c16c3b6')

FILENAME = "image.jpg"

@bot.on.message(text="d <f> <s>")
async def readme_handler(m: Message, f, s):
    urlpic = m.attachments[0].photo.sizes[-5].url
    print(urlpic)
    img_data = requests.get(urlpic).content


    async with aiof.open(FILENAME, mode='wb') as out:

        await out.write(img_data)
    dem = Demotivator(f, s)  # 2 строчки
    dem.create('image.jpg')
    photo = await PhotoMessageUploader(bot.api).upload(
        "demresult.jpg", peer_id=m.peer_id
    )
    await m.answer(attachment=photo)

bot.run_forever()

