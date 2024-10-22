from aiogram import types, executor,Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext
from buttons import main_menu
from datas import add_to_db,show_admin

api = '7910620601:AAE_VoSxCcONSk6EaA8KRL0klGijtB8vjyQ'
bot = Bot(api)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)

class MenuState(StatesGroup):
    awqat = State()
    baxasi = State()
    photo = State()




@dp.message_handler(commands=['start'])
async def send_hi(sms:types.Message):
    await sms.answer('Assalamu aleykum',
                     reply_markup=main_menu)
    
@dp.message_handler(text='Awqat menu')
async def send_menu(sms:types.Message):
    await sms.answer('awqatlar')
    await sms.answer('awqattin atin jaz:')
    await MenuState.awqat.set()

@dp.message_handler(state=MenuState.awqat)
async def send_food(sms:types.Message,state:FSMContext):
    async with state.proxy() as food:
        food['awqat']=sms.text
    await sms.answer('Baxasin jazin:')
    await MenuState.baxasi.set()

@dp.message_handler(state=MenuState.baxasi)
async def send_food(sms:types.Message,state:FSMContext):
    async with state.proxy() as food:
        food['baxasi']=sms.text
    await sms.answer('foto jiber:')
    await MenuState.photo.set()

@dp.message_handler(state=MenuState.photo,content_types='photo')
async def send_food(sms:types.Message,state:FSMContext):
    async with state.proxy() as food:
        food['photo']=sms.photo[0]['file_id']
    await sms.answer('Awqat qosildi:')
    await sms.answer_photo(
        photo=food['photo'],
        caption=f'''
ati:{food['awqat']},
baxasi:{food['baxasi']}'''
    )
    await add_to_db(awqat=food['awqat'],
                    baxasi=food['baxasi'],
                    photo=food['photo'])

    await state.finish()

@dp.message_handler(text='Suw menu')
async def send_food(sms:types.Message):
    foods = await show_admin()
    for i in foods:
        await sms.answer_photo(
            photo=i[-1],
            caption=f'''{i[0]},
{i[1]}
''')

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)