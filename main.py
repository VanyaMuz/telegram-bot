import asyncio
from aiogram import Bot, Dispatcher
import logging
import threading, time
from aiogram.types import Message

from config_reader import config
from handlers import router
from database.models import async_main


# def async_function():
    
    
   
#         time.sleep(2)
#         # catalog(message: Message)

# t1 = threading.Thread(target=async_function)

async def main():
    
    await async_main()
    
    
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_router(router)
    logging.basicConfig(level=logging.INFO, filename="bot.log", filemode='w',
                                                format="%(asctime)s %(levelname)s %(message)s")
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    # t1.start()
    await dp.start_polling(bot)

async def on_startup(bot: Bot):
    await bot.send_message( config.admin_id.get_secret_value(), text = "▶️Bot is running")
    
async def on_shutdown(bot: Bot):
    await bot.send_message( config.admin_id.get_secret_value(), text = "🛑Bot is OFF")
    

if __name__ == '__main__':
    
    try:
        
        asyncio.run(main())
        
    except:
        print('Bot stopped')

