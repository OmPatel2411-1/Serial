import asyncio
from pyrogram import Client, idle
# ... [Aapke pehle ke imports] ...

# 🚨 Zaroori Imports Jodein:
from database.db import init_db_pool 
from plugins.monitor import start_monitor_scheduler 
from config import Config

# ... [Aapke handlers yahan rahenge] ...

async def main():
    # Database Pool Initialize Karein
    await init_db_pool() 
    
    client = Client(
        "bot_session", 
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="plugins")
    )

    await client.start()

    # Monitoring scheduler ko background task mein shuru karein
    asyncio.create_task(start_monitor_scheduler(client)) 

    await idle() 
    
    await client.stop()

if __name__ == "__main__":
    asyncio.run(main())
