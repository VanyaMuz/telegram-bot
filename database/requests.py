from database.models import async_session
from database.models import Category
from database.models import Contact, ChatInfo

from sqlalchemy import select, desc, and_

# async def set_user(tg_id: int) -> None:
#     async with async_session() as session:
#         user = await session.scalar(select(User).where(User.tg_id == tg_id))
#         if not user:
#             userq = User(tg_id = tg_id)
#             session.add(userq)
#             await session.commit()

# async def get_categories():
#     async with async_session() as session:
#         return await session.scalars(select(Category))
    
async def get_contact_name(conid):
    async with async_session() as session:
        return await session.scalar(select(Contact).where(Contact.ContactID == conid))

async def get_all_chats_names():
    async with async_session() as session:
        return await session.scalars(select(ChatInfo).where(ChatInfo.Name != None))


# async def get_categories_items(category_id):
#     async with async_session() as session:
#         return await session.scalars(select(Item).where(Item.category == category_id))

async def get_categories_by_id():
    async with async_session() as session:
        return await session.scalar(select(Category).order_by(desc(Category.EventId)))
    
async def get_events(ev_id):
    async with async_session() as session:
        return await session.scalar(select(Category).where(Category.EventId == ev_id))
    
# async def get_item(item_id):
#     async with async_session() as session:
#         return await session.scalar(select(Item).where(Item.id == item_id))