# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "13379820")

API_HASH = os.environ.get("API_HASH", "77fdc5ce1fdcdccf2823978dfb533894")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7629462203:AAGdFwLXgT6EuJr07-TciEQl4PjHAwbzXiM") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Eagle_Movies1") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://rxrx1850:2MbPCsM06EHTiyew@cluster0.kuhr4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1002758303').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
