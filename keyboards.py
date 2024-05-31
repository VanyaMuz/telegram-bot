from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                           InlineKeyboardButton, InlineKeyboardMarkup)
from database.requests import get_contact_name
from aiogram.utils.keyboard import InlineKeyboardBuilder
from unicodedata import category

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Start parsing'), KeyboardButton(text='Chat list')],
                                     ],
                                     resize_keyboard=True,
                                     input_field_placeholder='Выберите действие'
                                    )


# async def categories():
#     all_categories = get_categories()
#     names = get_contact_name()
#     keyboard = InlineKeyboardBuilder()
#     # for category in all_categories:
#     #     keyboard.add(InlineKeyboardButton(text=category.Duration, callback_data=f"category_{category.Body}"), )
#     keyboard.add(InlineKeyboardButton(text='На главную', callback_data= 'to_main'))
#     return keyboard.adjust(2).as_markup()

# async def items(category_id):
#     all_items = await get_categories_items(category_id)
#     keyboard = InlineKeyboardBuilder()
#     for item in all_items:
#         keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f"item_{item.id}"), )
#     keyboard.add(InlineKeyboardButton(text='На главную', callback_data= 'to_main'))
#     return keyboard.adjust(2).as_markup()

# async def basket():
#     keyboard = InlineKeyboardBuilder()
#     keyboard.add(InlineKeyboardButton(text='В корзину', callback_data= 'to_main'))
#     keyboard.add(InlineKeyboardButton(text='На главную', callback_data= 'to_main'))
#     return keyboard.adjust(2).as_markup()