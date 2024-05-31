from typing import Any, Dict
from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


engine = create_async_engine('sqlite+aiosqlite:///c:\\Users\\Viber\\AppData\\Roaming\\ViberPC\\375445103496\\viber.db')

async_session = async_sessionmaker(engine)

class Base(AsyncSession, DeclarativeBase):
    pass

class User(Base):
    
    def __init__(self, tg_id):
        self.tg_id = tg_id
    
    __tablename__ = 'users'
  

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)

    def __repr__(self):
        return f'<User {self.username}>'

class Category(Base):

    def __init__(self, name):
        self.name = name
    
    
    __tablename__ = 'EventInfo'

    EventId: Mapped[int] = mapped_column(primary_key=True)
    Body: Mapped[str] = mapped_column(String(50))
    IsRead: Mapped[int] = mapped_column()
    ChatID: Mapped[str] = mapped_column()
    Timestamp: Mapped[int] = mapped_column()
    ClientFlag: Mapped[int] = mapped_column()
    ContactID: Mapped[int] = mapped_column()

    def __repr__(self):
        return f'<category {self.name}>'
    
class Contact(Base):

    def __init__(self, name):
        
        self.name = name

    __tablename__ = 'Contact'

    ContactID: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(50))
    ClientName: Mapped[str] = mapped_column(String(50))
    
    def __repr__(self):
        return f'<contact {self.name}>'

class ChatInfo(Base):

    def __init__(self, name, chatid):
        
        self.name = name
        self.chatid = chatid
        

    __tablename__ = 'ChatInfo'

    ChatID: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(String(50))
    
    def __repr__(self):
        return f'<chat {self.name}>'


class Item(Base):

    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category


    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(500))
    price: Mapped[int] = mapped_column()
    category: Mapped[int] = mapped_column(ForeignKey('categories.id'))

    def __repr__(self):
        return f'<Item {self.name}>'
    
async def async_main():
    async with engine.begin() as conn:
         await conn.run_sync(Base.metadata.create_all)