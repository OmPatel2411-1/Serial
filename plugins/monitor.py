import asyncio
import time
import requests
from bs4 import BeautifulSoup
from pyrogram import Client
from pyrogram.errors import FloodWait

from config import Config
from database.db import is_video_processed, add_processed_video 

FIRST_RUN_COMPLETED = False 

# =========================================================
# 🚨 3. ZEE5.COM CONTENT SCRAPING LOGIC
# =========================================================

def scrape_new_zee5_links(user_cookies: str) -> list:
    """
    zee5.com se latest video links ki list nikalta hai.
    """
    
    # Zaroor Badlein - URL ko apne hisaab se set karein
    LATEST_CONTENT_URL = "https://www.zee5.com/tv-shows/genre/drama/hindi" 
    
    headers = {
        'Cookie': user_cookies,
        'User-Agent': 'Mozilla/5.0 (CustomBot/1.0)'
    }
    
    latest_links = []
    
    try:
        response = requests.get(LATEST_CONTENT_URL, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # --------------------------------------------------------------------------
        # 🚨 ZAROOR BADLEIN - 4: HTML TAGS AUR CLASSES
        # Yahaan aapki website ke structure ke hisaab se badlav zaruri hai
        # --------------------------------------------------------------------------
        
        # 1. Main List Container Dhoondhein
        main_list_wrapper = soup.find('div', class_='movieTrayWrapper') 
        if not main_list_wrapper: return []
            
        # 2. Container ke andar har video item ko dhoondhein (Finalized selector)
        video_containers = main_list_wrapper.find_all('div', class_='slick-slide') 
        
        for container in video_containers:
            # <a> tag ko dhoondhein
            a_tag = container.find('a', href=True) 
            
            if a_tag:
                href = a_tag.get('href')
                if href and 'video/' in href: 
                    if not href.startswith('http'):
                        full_url = f"https://www.zee5.com{href}"  
                    else:
                        full_url = href
                    latest_links.append(full_url)
        # --------------------------------------------------------------------------
        
        return list(set(latest_links))
    
    except requests.exceptions.RequestException as e:
        print(f"Scraping Error: {e}")
        return []
    except Exception as e:
        print(f"Parsing Error: {e}")
        return []

# ---------------------------------------------------------------------

async def zee5_monitor_task(client: Client):
    global FIRST_RUN_COMPLETED
    latest_links = scrape_new_zee5_links(Config.ZEE5_COOKIES)
    
    if not FIRST_RUN_COMPLETED and latest_links:
        print("FIRST RUN: Recording old videos for sync...")
        for link in latest_links:
            await add_processed_video(link) 
        FIRST_RUN_COMPLETED = True 
        return
    
    if not latest_links: return
        
    for link in latest_links:
        if not await is_video_processed(link):
            print(f"🎉 NEW VIDEO FOUND: {link} - Starting Telegram upload.")
            try:
                # Bot ko seedha link bhej diya
                await client.send_message(chat_id=Config.UPDATE_CHANNEL, text=link)
                await add_processed_video(link) 
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except Exception as e:
                print(f"Error processing link {link}: {e}")

async def start_monitor_scheduler(client: Client):
    """Monitoring task ko niyamit roop se chalata hai."""
    interval = Config.MONITOR_INTERVAL_MINUTES
    
    await client.send_message(
        chat_id=Config.UPDATE_CHANNEL,
        text=f"✅ Automation Started: ZEE5 Monitor checking every {interval} minutes."
    )
    
    while True:
        await zee5_monitor_task(client)
        await asyncio.sleep(interval * 60)
