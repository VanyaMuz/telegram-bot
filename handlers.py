
from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode
import asyncio


import database.requests as  rq
from database.requests import get_all_chats_names
import keyboards as kb

router = Router()

Chat_id_list = {5:'Запчасти Мари', 25: 'Пингвины', 32:'ЗАПЧАСТИ  УПР', 142: 'test' }

@router.message(CommandStart())
async def start(message: Message):

      
    await message.answer(f"Hello, {message.from_user.full_name}", reply_markup=kb.main)
    
@router.message(F.text == "Start parsing")
async def catalog(message: Message):
    global ccID_new
    global ccID_old
    ccID_new = 0
    
    while True:
        
        category = await rq.get_categories_by_id()
        
        # sys.stderr.write(f"{category.EventId} ccid {ccID_new}\r") #print(category.EventId)
        # sys.stderr.write(f"ccid start {ccID_new}\r")
        # print('ccid start', ccID_new)
        if ccID_new == 0:
            ccID_new = int(category.EventId)
            ccID_old = ccID_new
        elif ccID_new != category.EventId:
            
            while ccID_new != category.EventId+1:
                event = await rq.get_events(ccID_new)
                print(event.ClientFlag)
                print(event.ChatID)
                if event.ChatID in Chat_id_list:
                    if ccID_new != ccID_old:
                        try:
                            contact = await rq.get_contact_name(event.ContactID)
                            await message.answer(f"Чат: <b>{Chat_id_list[event.ChatID]}</b>\n{contact.Name if contact.Name != None else contact.ClientName}:\n{event.Body}", parse_mode = ParseMode.HTML)
                            ccID_old = ccID_new
                        except:
                            print('error', 'contact name:', contact.ClientName, 'ccidnew:', ccID_new, 'ccidold:', ccID_old)
                            pass
                elif event.ClientFlag in (0, 256):
                    if ccID_new != ccID_old:
                        try:
                            contact = await rq.get_contact_name(event.ContactID)
                            await message.answer(f"{'Личное сообщение от:' if event.ClientFlag == 0 else 'Изменено:'}  <b>{contact.Name if contact.Name != None else contact.ClientName}</b>\n {event.Body}", parse_mode = ParseMode.HTML)
                            ccID_old = ccID_new
                        except:
                            pass    
                ccID_new +=1
            ccID_new = int(category.EventId)
        await asyncio.sleep(5)
        
# @router.callback_query(F.data.startswith('category_'))
# async def category(callback: CallbackQuery):
#     category_data = await rq.get_categories_by_id(callback.data.split('_')[1])
    
#     # await callback.answer(f'Вы выбрали категорию, {category_data.name}')
#     # await callback.message.answer("Выберите товар по категории", 
#     #                               reply_markup= await kb.items(callback.data.split('_')[1]))
    
# @router.callback_query(F.data.startswith('item_'))
# async def item(callback: CallbackQuery):
#     item_data = await rq.get_item(callback.data.split('_')[1])
#     # print('callback.data= ', callback.data)
#     await callback.answer(f'Вы выбрали товар, {item_data.name}')
#     await callback.message.answer(f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price} рублей',
#                                   reply_markup= await kb.basket())
    

@router.message(F.text == "Chat list")
async def chat_list(callback: CallbackQuery):
    chat_list_db = await get_all_chats_names()
    all_chats_list = {}
    for chat in chat_list_db:
        
        all_chats_list[chat.ChatID] = chat.Name
    
    await callback.answer(f'Chat: {all_chats_list}')
    