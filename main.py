import random
import time
import requests
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "مرحباً بك في تشغيل البروجك لمدة 24 ساعة!"

    app.run(host='0.0.0.0', port=8080)
import asyncio
from typing import Literal

from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata,  GetMessagesRequest, User ,Item, Position, CurrencyItem, Reaction
from typing import Any, Dict, Union
import random
import time
from highrise import BaseBot, __main__, CurrencyItem, Item, Position, AnchorPosition, SessionMetadata, User
from highrise.__main__ import BotDefinition
from asyncio import run as arun
from json import load, dump
import asyncio
import os
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from typing import Union
import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from typing import Any, Dict, Union
import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re

from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from highrise import BaseBot, Position
from highrise import __main__
from highrise.models import Item
from asyncio import run as arun
from highrise.models import AnchorPosition
import requests
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import BaseBot
from collections import UserDict
from highrise.models import SessionMetadata, User
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
import random
from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task
from typing import Union
import asyncio
import contextlib
import random
from typing import Any, Dict, Union
from importlib.machinery import ModuleSpec
from click.decorators import pass_context
from highrise import BaseBot
from typing import Any, Dict, Union
from highrise import *
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *



dance_group = set()
moderators = ["Jollyjojo65","_haIey","UntraceableDJ","Just.Joke","iRoose","Willyodasno","McSquishems","nicciswaving","1_on_1:64ce5151f395c5380a451768:66ad7a2ff79957b0678e53a9"]
         #this private converstion id you can sa to bot join and will find yours in fans.json


class BotDefinition:
    
      
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token
        self.following_username = None

class Counter:
    bot_id = ""
    static_ctr = 0
    usernames = ['UntraceableDJ' ,'Jollyjojo65' ,'_haIey']

class Bot(BaseBot):
    continuous_emote_tasks: Dict[int, asyncio.Task[Any]] = {}  
    user_data: Dict[int, Dict[str, Any]] = {}
    EMOTE_DICT = {
      "angry"           : "emoji-angry",
      "bow"             : "emote-bow",
      "casual"          : "idle-dance-casual",
      "charging"        : "emote-charging",
      "confusion"       : "emote-confused",
      "cursing"         : "emoji-cursing",
      "curtsy"          : "emote-curtsy",
      "cutey"           : "emote-cutey",
      "dont"            : "dance-tiktok2",
      "emotecute"       : "emote-cute",
      "energyball"      : "emote-energyball",
      "enthused"        : "idle-enthusiastic",
      "fashionista"     : "emote-fashionista",
      "flex"            : "emoji-flex",
      "flirtywave"      : "emote-lust",
      "float"           : "emote-float",
      "frog"            : "emote-frog",
      "gravedance"      : "dance-weird",
      "gravity"         : "emote-gravity",
      "greedy"          : "emote-greedy",
      "hello"           : "emote-hello",
      "hot"             : "emote-hot",
      "icecream"        : "dance-icecream",
      "kiss"            : "emote-kiss",
      "kpop"            : "dance-blackpink",
      "lambi"           : "emote-superpose",
      "laugh"           : "emote-laughing",
      "letsgo"          : "dance-shoppingcart",
      "maniac"          : "emote-maniac",
      "model"           : "emote-model",
      "no"              : "emote-no",
      "ogdance"         : "dance-macarena",
      "pennydance"      : "dance-pennywise",      
      "pose1"           : "emote-pose1",
      "pose2"           : "emote-pose3",
      "pose3"           : "emote-pose5",
      "pose4"           : "emote-pose7",
      "pose5"           : "emote-pose8",
      "punkguitar"      : "emote-punkguitar",
      "raisetheroof"    : "emoji-celebrate",
      "russian"         : "dance-russian",
      "sad"             : "emote-sad",
      "savage"          : "dance-tiktok8",
      "shuffle"         : "dance-tiktok10",
      "shy"             : "emote-shy",
      "singalong"       : "idle_singing",
      "sit"             : "idle-loop-sitfloor",
      "snowangel"       : "emote-snowangel",
      "snowball"        : "emote-snowball",
      "swordfight"      : "emote-swordfight",
      "telekinesis"     : "emote-telekinesis",
      "teleport"        : "emote-teleporting",
      "thumbsup"        : "emoji-thumbsup",
      "tired"           : "emote-tired",
      "tummyache"       : "emoji-gagging",
      "viral"           : "dance-tiktok9",
      "wave"            : "emote-wave",
      "weird"           : "dance-weird",
      "worm"            : "emote-snake",
      "wrong"           : "dance-wrong",
      "yes"             : "emote-yes",
      "zombierun"       : "emote-zombierun",
      "ANGRY"           : "emoji-angry",
      "BOW"             : "emote-bow",
      "CASUAL"          : "idle-dance-casual",
      "CHARGING"        : "emote-charging",
      "CONFUSION"       : "emote-confused",
      "CURSING"         : "emoji-cursing",
      "CURTSY"          : "emote-curtsy",
      "CUTEY"           : "emote-cutey",
      "DONT"            : "dance-tiktok2",
      "EMOTECUTE"       : "emote-cute",
      "ENERGYBALL"      : "emote-energyball",
      "ENTHUSED"        : "idle-enthusiastic",
      "FASHIONISTA"     : "emote-fashionista",
      "FLEX"            : "emoji-flex",
      "FLIRTYWAVE"      : "emote-lust",
      "FLOAT"           : "emote-float",
      "FROG"            : "emote-frog",
      "GRAVEDANCE"      : "dance-weird",
      "GRAVITY"         : "emote-gravity",
      "GREEDY"          : "emote-greedy",
      "HELLO"           : "emote-hello",
      "HOT"             : "emote-hot",
      "ICECREAM"        : "dance-icecream",
      "KISS"            : "emote-kiss",
      "KPOP"            : "dance-blackpink",
      "LAMBI"           : "emote-superpose",
      "LAUGH"           : "emote-laughing",
      "LETSGO"          : "dance-shoppingcart",
      "MANIAC"          : "emote-maniac",
      "MODEL"           : "emote-model",
      "NO"              : "emote-no",
      "OGDANCE"         : "dance-macarena",
      "PENNYDANCE"      : "dance-pennywise",
      "POSE1"           : "emote-pose1",
      "POSE2"           : "emote-pose3",
      "POSE3"           : "emote-pose5",
      "POSE4"           : "emote-pose7",
      "POSE5"           : "emote-pose8",
      "PUNKGUITAR"      : "emote-punkguitar",
      "RAISETHEROOF"    : "emoji-celebrate",
      "RUSSIAN"         : "dance-russian",
      "SAD"             : "emote-sad",
      "SAVAGE"          : "dance-tiktok8",
      "SHUFFLE"         : "dance-tiktok10",
      "SHY"             : "emote-shy",
      "SINGALONG"       : "idle_singing",
      "SIT"             : "idle-loop-sitfloor",
      "SNOWANGEL"       : "emote-snowangel",
      "SNOWBALL"        : "emote-snowball",
      "SWORDFIGHT"      : "emote-swordfight",
      "TELEKINESIS"     : "emote-telekinesis",
      "TELEPORT"        : "emote-teleporting",
      "THUMBSUP"        : "emoji-thumbsup",
      "TIRED"           : "emote-tired",
      "TUMMYACHE"       : "emoji-gagging",
      "VIRAL"           : "dance-tiktok9",
      "WAVE"            : "emote-wave",
      "WEIRD"           : "dance-weird",
      "WORM"            : "emote -snake",
      "WRONG"           : "dance-wrong",
      "YES"             : "emote-yes",
      "ZOMBIERUN"       : "emote-zombierun",  
      "Angry"           : "emoji-angry",
      "Bow"             : "emote-bow",
      "Casual"          : "idle-dance-casual",
      "Charging"        : "emote-charging",
      "Confusion"       : "emote-confused",
      "Cursing"         : "emoji-cursing",
      "Curtsy"          : "emote-curtsy",
      "Cutey"           : "emote-cutey",
      "Dont"            : "dance-tiktok2",
      "Emotecute"       : "emote-cute",
      "Energyball"      : "emote-energyball",
      "Enthused"        : "idle-enthusiastic",
      "Fashionista"     : "emote-fashionista",
      "Flex"            : "emoji-flex",
      "Flirtywave"      : "emote-lust",
      "Float"           : "emote-float",
      "Frog"            : "emote-frog",
      "Gravedance"      : "dance-weird",
      "Gravity"         : "emote-gravity",
      "Greedy"          : "emote-greedy",
      "Hello"           : "emote-hello",
      "Hot"             : "emote-hot",
      "Icecream"        : "dance-icecream",
      "Kiss"            : "emote-kiss",
      "Kpop"            : "dance-blackpink",
      "Lambi"           : "emote-superpose",
      "Laugh"           : "emote-laughing",
      "Letsgo"          : "dance-shoppingcart",
      "Maniac"          : "emote-maniac",
      "Model"           : "emote-model",
      "No"              : "emote-no",
      "Ogdance"         : "dance-macarena",
      "Pennydance"      : "dance-pennywise",
      "Pose1"           : "emote-pose1",
      "Pose2"           : "emote-pose3",
      "Pose3"           : "emote-pose5",
      "Pose4"           : "emote-pose7",
      "Pose5"           : "emote-pose8",
      "Punkguitar"      : "emote-punkguitar",
      "celebrate"       : "emoji-celebrate",
      "Russian"         : "dance-russian",
      "Sad"             : "emote-sad",
      "Savage"          : "dance-tiktok8",
      "Shuffle"         : "dance-tiktok10",
      "Shy"             : "emote-shy",
      "Singalong"       : "idle_singing",
      "Sit"             : "idle-loop-sitfloor",
      "Snowangel"       : "emote-snowangel",
      "Snowball"        : "emote-snowball",
      "Swordfight"      : "emote-swordfight",
      "Telekinesis"     : "emote-telekinesis",
      "Teleport"        : "emote-teleporting",
      "Thumbsup"        : "emoji-thumbsup",
      "Tired"           : "emote-tired",
      "Tummyache"       : "emoji-gagging",
      "wing"            : "emote-wings",
      "Viral"           : "dance-tiktok9",
      "Wave"            : "emote-wave",
      "Weird"           : "dance-weird",
      "Worm"            : "emote-snake",
      "Wrong"           : "dance-wrong",
      "Yes"             : "emote-yes",
      "Zombierun"       : "emote-zombierun",
      "sayso"           : "idle-dance-tiktok4",
      "Sayso"           : "idle-dance-tiktok4",
      "SAYSO"           : "idle-dance-tiktok4",
      "uwu"             : "idle-uwu",
      "UWU"             : "idle-uwu",
      "bash"            : "emote-shy2",
      "Zero"            : "emote-astronaut",
      "zero"            : "emote-astronaut",
      "bashfull"            : "emote-shy2",
      "Bashfull"         : "emote-shy2",
      "anime"            : "dance-anime",
      "Anime"            : "dance-anime",
      "airguitar"        : "idle-guitar",
      "Airguitar"        : "idle-guitar",
      "revelations"      : "emote-headblowup",
      "revelation"      : "emote-headblowup",
      "Revelations"      : "emote-headblowup",
      "creepy"           : "dance-creepypuppet",
      "Creepy"           : "dance-creepypuppet",
      "creepycute"       : "emote-creepycute",
      "Creepycute"       : "emote-creepycute",
      "penguin" : "dance-pinguin",
      "Penguin" : "dance-pinguin",
      "sleigh" : "emote-sleigh",
      "Sleigh" : "emote-sleigh",
      "hyped" : "emote-hyped",
      "Hyped" : "emote-hyped",
      "jingle" : "dance-jinglebell", 
      "Jingle" : "dance-jinglebell", 
      "nervous" : "idle-nervous",
      "Nervous" : "idle-nervous",
      "gottago" : "idle-toilet",
      "Gottago" : "idle-toilet",
      "Timejump" : "emote-timejump",
      "timejump" : "emote-timejump",
      "repose" : "sit-relaxed",
      "Repose" : "sit-relaxed",
      "kawaii" : "dance-kawai" , 
      "Kawaii" : "dance-kawai" , 
      "scritchy" : "idle-wild" ,
      "Scritchy" : "idle-wild" ,
      "skating" : "emote-iceskating",
      "Skating " : "emote-iceskating",
      "touch" : "dance-touch",
      "Touch" : "dance-touch"
    }
    continuous_emote_task = None
    

    def __init__(self):
        super().__init__()
        self.load_membership()
        self.load_moderators()
        self.load_fans()
        self.load_temporary_vips()
        self.following_username = None
        self.maze_players = {}
        self.user_points = {}  # Dictionary to store user points
        self.bot_id = None
        self.owner_id = None
        self.bot_status = False
        self.tip_data = None
        self.load_tip_data()
        self.bot_position = None
      


    def load_temporary_vips(self):
        try:
            with open("temporary.json", "r") as file:
                self.temporary_vips = json.load(file)
        except FileNotFoundError:
            self.temporary_vips = {}

    def save_temporary_vips(self):
        with open("temporary.json", "w") as file:
            json.dump(self.temporary_vips, file)

    def load_moderators(self):
        try:
            with open("moderators.json", "r") as file:
                self.moderators = json.load(file)
        except FileNotFoundError:
            self.moderators = []
        default_moderators =['Jollyjojo65', '_haIey', 'UntraceableDJ', 'Just.Joke', 'iRoose', 'Willyodasno', 'McSquishems', 'nicciswaving']
        # Add default moderators here
        for mod in default_moderators:
            if mod.lower() not in self.moderators:
                self.moderators.append(mod.lower())
    def load_fans(self):
      try:
          with open("fans.json", "r") as file:
              self.fans = json.load(file)
      except FileNotFoundError:
          self.fans = []

     
    def load_membership(self):
     try:
        with open("membership.json", "r") as file:
            self.membership = json.load(file)
     except FileNotFoundError:
        self.membership = []
    def save_membership(self):
     with open("membership.json", "w") as file:
        json.dump(self.membership, file)

  
    def save_moderators(self):

      with open("moderators.json", "w") as file:
            json.dump(self.moderators, file)

    def save_fans(self):

      with open("fans.json", "w") as file:
          json.dump(self.fans, file)

    def init(self):
        super().init()

        self.Emotes = Emotes

    async def on_emote(self, user: User ,emote_id : str , receiver: User | None )-> None:
      print (f"{user.username} , {emote_id}")

    


        
        

        

    




    async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions) 

    

    async def on_user_move(self, user: User, pos: Position) -> None:
        
         if user.username == "UntraceableDJ":
           print(pos)
  
    async def teleport_requester_to_user(self, target_username: str, requester_user: User):
      room_users = await self.highrise.get_room_users()
      target_user_position = None

      for user, position in room_users.content:
          if user.username.lower() == target_username.lower():
              target_user_position = position
              break

      if target_user_position is not None:
          requester_position = Position(target_user_position.x, target_user_position.y, target_user_position.z + 1, target_user_position.facing)
          requester_dict = {
              "id": requester_user.id,
              "position": requester_position
          }
          await self.highrise.teleport(requester_dict["id"], requester_dict["position"])
      else:
          print("Target user not found.")




    







    
    async def teleport_user_next_to(self, target_username: str, requester_user: User):
        room_users = await self.highrise.get_room_users()
        requester_position = None

        for user, position in room_users.content:
          if user.id == requester_user.id:
              requester_position = position
              break
        for user, position in room_users.content:
          if user.username.lower() == target_username.lower(): 
            z = requester_position.z 
            new_z = z + 1 

            user_dict = {
              "id": user.id,
              "position": Position(requester_position.x, requester_position.y, new_z, requester_position.facing)
            }
            await self.highrise.teleport(user_dict["id"], user_dict["position"])

    
    async def on_chat(self, user: User, message: str) -> None:
       #this to got any message user say in the room in console
        print(f"{user.username} said: {message}")
        response = await self.command_handler(user.id, message)
        if response:
            try:
                await self.highrise.chat(response)
            except Exception as e:
                print(f"Chat Error: {e}")

        #this to buy voice
        if message.lower().startswith("!buyvoice") and user.username in moderators:
            response = await self.highrise.buy_voice_time(payment="bot_wallet_only")
            print (response)


        #this to buy boost token
        
        if message.lower().startswith("!buyboost") and user.username in moderators:
            response = await self.highrise.buy_room_boost(payment="bot_wallet_only", amount=1)
            print (response)


        #this to go someone 

        if message.startswith("!go") and user.username in moderators:
           target_username = message.split("@")[-1].strip()
           if target_username not in ["", ""]:
              await self.teleport_requester_to_user(target_username, user)

        #this to tele someone to you
        if message.startswith("!tp") and user.username in moderators:
           target_username = message.split("@")[-1].strip()
           if target_username not in ["", ""]:
              await self.teleport_user_next_to(target_username, user)


        
#get item
        if message.lower().startswith("!buyvoice") and user.username in moderators:
            response = await self.highrise.buy_voice_time(payment="bot_wallet_only")
            print (response)
      
        if message.lower().startswith("!buyboost") and user.username in moderators:
            response = await self.highrise.buy_room_boost(payment="bot_wallet_only", amount=1)

        if message == "!fit5":
          shirt = ["shirt-f_punklace"]
          pant = ["skirt-n_room12019pleatedskirtblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018openthinpeaked', account_bound=False, active_palette=9),

                  Item(type='clothing', amount=1, id='hair_front-n_registrationavatars2023gothgirlhair', account_bound=False, active_palette=2),
                  Item(type='clothing', amount=1, id='hair_back-n_registrationavatars2023gothgirlhair', account_bound=False, active_palette=2),
                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows06', account_bound=False, active_palette=2),
                  Item(type='clothing', amount=1, id='eye-n_registrationavatars2023gymgirleyes', account_bound=False, active_palette=7),
                  
                  Item(type='clothing', amount=1, id='freckle-n_registrationavatars2023contour', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=2),
                  Item(type='clothing', amount=1, id='hat-n_registrationavatars2023wolfears', account_bound=False, active_palette=2),
                  
                  


          ]) 
          await self.highrise.chat(f"{xox}") 

        
        if message.lower().startswith("/getitem"):
          outfit_response = await self.highrise.get_my_outfit()
          fifth_item = outfit_response.outfit[4].id
          item_response = await self.webapi.get_item(item_id=fifth_item)
          print (item_response)

        
       
#tip 5 random tip 2 to 10 users 

       
        if message == ("/tip 2 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:2]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 3 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:3]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")

        if message == ("/tip 4 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:4]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 5 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:5]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 6 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:6]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")

        if message == ("/tip 7 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:7]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")

        if message == ("/tip 8 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:8]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 9 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:9]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 10 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:10]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 20 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:20]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")



        
#tip 10g 2 to 10 users



        

        if message == ("/tip 2 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:2]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 3 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:3]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")

        if message == ("/tip 4 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:4]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 5 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:5]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 6 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:6]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")

        if message == ("/tip 7 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:7]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")

        if message == ("/tip 8 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:8]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 9 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:9]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 10 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:10]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 20 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:20]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")



        

#tip 1 random tip 2 to 10 users


        

        if message == ("/tip 2 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:2]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")


        if message == ("/tip 3 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:3]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")

        if message == ("/tip 4 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:4]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")


        if message == ("/tip 5 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:5]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")


        if message == ("/tip 6 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:6]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")

        if message == ("/tip 7 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:7]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")

        if message == ("/tip 8 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:8]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")


        if message == ("/tip 9 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:9]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 10 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:10]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")


        if message == ("/tip 20 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:20]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")

       
       

        #this command for tip all users in the room you can use any amount like !tip 1 or 5 or 10 or 50 or 100 or 500 or 1000 or 5000 or 10000 should to add name here to work and should to add the same name in HR eith capital and small letters
        
       
        if message.startswith("!tip ") and user.username in moderators:
          try:
              await self.highrise.chat(f"𝔫𝔬𝔴 𝔞𝔩𝔩 𝔤𝔢𝔱 𝔱𝔦𝔭 𝔣𝔯𝔬𝔪 @{user.username}")
              tip_amount = int(message.split(" ")[1])
          except IndexError:
              await self.highrise.chat("plz add how much you want to tip all")
              return
          except ValueError:
              await self.highrise.chat("CAN YOU WRITE THE RIGHT COMMAND !tip amount")
              return
          if user.username in ['UntracableDJ', 'Just.Joke', 'iRoose', 'Willyodasno', 'McSquishems', 'nicciswaving']:
              response = await self.highrise.get_room_users()
              num_users = len(response.content)
              total_gold = tip_amount * num_users

              bot_wallet = await self.highrise.get_wallet()
              bot_amount = bot_wallet.content[0].amount

              if bot_amount >= total_gold:
                  for content in response.content:
                      user_id = content[0].id
                      await self.highrise.tip_user(user_id, f"gold_bar_{tip_amount}")
              else:
                  await self.highrise.chat("send gold to send tips")

        
#this to fin id any item you want
     
        if message.lower().startswith("/item "):
            parts = message.split(" ")
            if len(parts) < 2:
                await self.highrise.chat("Invalid command")
                return
            item_name = ""
            for part in parts[1:]:
                item_name += part + " "
            item_name = item_name[:-1]
            print (item_name)
            try:
                response = await self.webapi.get_items(item_name=item_name)
                print (response)
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
       

#rhis to heart the user with any amount you want like ❤️ @name amount 1 to 100 
        
        if message.startswith("❤️ ") and user.username in ["QueenNatsumi","DJBLOOD","DJBABYSHARK","DJBABYSHARK","HidenShadow","catoptric"]: 
          try:
              
              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("heart", target_user.id)
                      else:
                          await self.highrise.chat(f"the user {target_username} Not available in the room.")
              else:
                  await self.highrise.chat("1  _ 100  only ")
          except ValueError:
              await self.highrise.chat("❤️ @name number you forget to write it")
            
#mod commands
        
        if message.startswith("!kick"):
            if user.username.lower() in self.moderators:
                parts = message.split()
                if len(parts) < 2:
                    await self.highrise.chat(user.id, "Usage: !kick @username")
                    return

                mention = parts[1]
                username_to_kick = mention.lstrip('@')  # Remove the '@' symbol from the mention
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]  # Extract the User objects
                user_ids = [user.id for user in users]  # Extract the user IDs

                if username_to_kick.lower() in [user.username.lower() for user in users]:
                    user_index = [user.username.lower() for user in users].index(username_to_kick.lower())
                    user_id_to_kick = user_ids[user_index]
                    await self.highrise.moderate_room(user_id_to_kick, "kick")
                    await self.highrise.chat( f"Kicked {mention}.")
                else:
                    await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
            else:
                await self.highrise.send_whisper(user.id, "You can't use this command.")

        elif message.startswith("!mute"):
            if user.username.lower() in self.moderators:
                parts = message.split()
                if len(parts) < 2:
                    await self.highrise.chat(user.id, "Usage: !mute @username")
                    return

                mention = parts[1]
                username_to_mute = mention.lstrip('@')  # Remove the '@' symbol from the mention
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]  # Extract the User objects
                user_ids = [user.id for user in users]  # Extract the user IDs

                if username_to_mute.lower() in [user.username.lower() for user in users]:
                    user_index = [user.username.lower() for user in users].index(username_to_mute.lower())
                    user_id_to_mute = user_ids[user_index]
                    await self.highrise.moderate_room(user_id_to_mute, "mute",3600)  # Mute for 1 hour
                    await self.highrise.chat(f"Muted {mention} for 1 hour.")
                else:
                    await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
            else:
                await self.highrise.send_whisper(user.id, "You can't use this command.")

        elif message.startswith("!unmute"):
            if user.username.lower() in self.moderators:
                parts = message.split()
                if len(parts) < 2:
                    await self.highrise.chat(user.id, "Usage: !mute @username")
                    return

                mention = parts[1]
                username_to_mute = mention.lstrip('@')  # Remove the '@' symbol from the mention
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]  # Extract the User objects
                user_ids = [user.id for user in users]  # Extract the user IDs

                if username_to_mute.lower() in [user.username.lower() for user in users]:
                    user_index = [user.username.lower() for user in users].index(username_to_mute.lower())
                    user_id_to_mute = user_ids[user_index]
                    await self.highrise.moderate_room(user_id_to_mute, "mute",1)  # Mute for 1 hour
                    await self.highrise.chat(f"{mention} Unmuted.")
                else:
                    await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
            else:
                await self.highrise.send_whisper(user.id, "You can't use this command.")

        elif message.startswith("!ban"):
            if user.username.lower() in self.moderators:
                parts = message.split()
                if len(parts) < 2:
                    await self.highrise.chat(user.id, "Usage: !ban @username")
                    return

                mention = parts[1]
                username_to_ban = mention.lstrip('@')  # Remove the '@' symbol from the mention
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]  # Extract the User objects
                user_ids = [user.id for user in users]  # Extract the user IDs

                if username_to_ban.lower() in [user.username.lower() for user in users]:
                    user_index = [user.username.lower() for user in users].index(username_to_ban.lower())
                    user_id_to_ban = user_ids[user_index]
                    await self.highrise.moderate_room(user_id_to_ban, "ban", 3600)  # Ban for 1 hour
                    await self.highrise.chat(f"Banned {mention} for 1 hour.")
                else:
                    await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
            else:
                await self.highrise.send_whisper(user.id, "You can't use this command.")

#dress bot 
 
        if message == "!fit4":
          shirt = ["shirt-n_2016fallblackkknottedtee"]
          pant = ["pants-n_room22019undiesblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),
                  
                  Item(type='clothing', amount=1, id='hair_front-n_basic2018straightpulledback', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018straighthighpony', account_bound=False, active_palette=1),
                  
                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018teardrop', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle32', account_bound=False, active_palette=-1),
                  
                  
            
          ]) 
          await self.highrise.chat(f"good {xox}")
        

        if  message.startswith("!wallet"):
            if user.username in moderators :

                  wallet = (await self.highrise.get_wallet()).content
                  await self.highrise.send_whisper(user.id, f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")

            else: 
                await  self.highrise.send_whisper(user.id, f"Only Moderators Can View the Wallet")

        if message == "!fit3":
          shirt = ["shirt-n_room22019bratoppink"]
          pant = ["skirt-n_room12019pleatedskirtpink"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullround', account_bound=False, active_palette=8),

                  Item(type='clothing', amount=1, id='hair_back-n_basic2018straighthighpony', account_bound=False, active_palette=17),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2018wavypulledback', account_bound=False, active_palette=17),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018definedlashes', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_room22019heelspink', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle32', account_bound=False, active_palette=-1),
                  
                  
                  Item(type='clothing', amount=1, id='earrings-n_room32019chainearrings', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),


          ]) 
          await self.highrise.chat(f"good {xox}")

        
        
        if message.lower().startswith("/get "):
            parts = message.split(" ")
            if len(parts) != 2:
                await self.highrise.chat("Invalid command")
                return
            item_id = parts[1]
            try:
                response = await self.highrise.buy_item(item_id)
                await self.highrise.chat(f"Item bought: {response}")
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")



        if message.lower().startswith("/item "):
            parts = message.split(" ")
            if len(parts) < 2:
                await self.highrise.chat("Invalid command")
                return
            item_name = ""
            for part in parts[1:]:
                item_name += part + " "
            item_name = item_name[:-1]
            print (item_name)
            try:
                response = await self.webapi.get_items(item_name=item_name)
                print (response)
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
        

        if message == "!fit2":
          shirt = ["shirt-n_starteritems2019femtshirtwhite"]
          pant = ["pants-n_room32019rippedpantsblue"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_basic2018newnose20', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018thinpeaked', account_bound=False, active_palette=-1),
                  
                  Item(type='clothing', amount=1, id='hair_front-n_basic2019wavyflipdroop', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018wavymed', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2019wavyflipdroop', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018femaleovalslant', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_converse_black', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle32', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='necklace-n_SCSpring2018camera', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='glasses-n_room12019circleframes', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='earrings-n_room32019chainearrings', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),
                  
            
          ]) 
          await self.highrise.chat(f"good {xox}")

        
        if message == "!fit1":
          shirt = ["shirt-f_punklace"]
          pant = ["pants-n_room22019shortcutoffsdenim"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullround', account_bound=False, active_palette=9),

                  Item(type='clothing', amount=1, id='hair_back-n_basic2018wavyhighpony', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2019faceframewaves', account_bound=False, active_palette=1),
                  
                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018butterflyeyes', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_converse_black', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  
                  
                  Item(type='clothing', amount=1, id='necklace-n_room32019locknecklace', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='bag-n_room32019sweaterwrapblack', account_bound=False, active_palette=-1),
                  
                  Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),


          ]) 
          await self.highrise.chat(f"good {xox}")

        

        
#this teleports you can add you name in on user move to get the location you want in console and you can just add in await self.highrise.teleport(u.id,Position(and add here)) and also do the same with seconde one   also this tele only for mod
        

        

        if message.startswith("!vip"):
           if user.username.lower() in self.moderators or user.username.lower() in self.temporary_vips:
              split = message.split()
              if len(split) == 2:
                  name = split[1].lower()
                  response = await self.highrise.get_room_users()
                  users = [content[0] for content in response.content]
                  try:
                      for u in users:
                          u_give = str("@") + str((u.username).lower())
                          if str((u_give).lower()).strip() == str(name).strip():
                              await self.highrise.teleport(u.id,Position(x=17.0, y=12.0, z=1.0, facing='FrontRight')) 
                              break
                  except:
                      pass
              else:
                  await self.highrise.teleport(user.id,Position(x=17.0, y=12.0, z=1.0, facing='FrontRight'))

        
        if message.startswith("!host"):
           if user.username.lower() in self.moderators or user.username.lower() in self.temporary_vips:
              split = message.split()
              if len(split) == 2:
                  name = split[1].lower()
                  response = await self.highrise.get_room_users()
                  users = [content[0] for content in response.content]
                  try:
                      for u in users:
                          u_give = str("@") + str((u.username).lower())
                          if str((u_give).lower()).strip() == str(name).strip():
                              await self.highrise.teleport(u.id,Position(x=12.0, y=2.0, z=19.0, facing='FrontRight')) 
                              break
                  except:
                      pass
              else:
                  await self.highrise.teleport(user.id,Position(x=12.0, y=2.0, z=19.0, facing='FrontRight'))


        if message.startswith("!dj"):
         if user.username.lower() in self.moderators or user.username.lower() in self.temporary_vips:
          
            split = message.split()
            if len(split) == 2:
                name = split[1].lower()
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                try:
                    for u in users:
                        u_give = str("@") + str((u.username).lower())
                        if str((u_give).lower()).strip() == str(name).strip():
                            await self.highrise.teleport(u.id, Position(x=15.0, y=13.0, z=18.0, facing='FrontRight'))
                            break
                except:
                    pass
            else:
                await self.highrise.teleport(user.id,Position(x=15.0, y=13.0, z=18.0, facing='FrontRight'))

        #this tele for all users 
        
        if message.startswith(('!f1','!F1','f1','F1')):
           parts = message.split()
           if len(parts) == 1:
              await self.highrise.teleport(f"{user.id}", Position(x=9.0, y=8.75, z=5.5, facing='FrontRight'))
             
        if message.startswith(('f2','F2','!F2','!f2')):
           parts = message.split()
           if len(parts) == 1:
              await self.highrise.teleport(f"{user.id}", Position(x=11.5, y=15.75, z=0.5, facing='BackLeft'))
              
             
        if message.startswith(('!f0','!F0','f0','F0')):
           parts = message.split()
           if len(parts) == 1:
              await self.highrise.teleport(f"{user.id}", Position(x=2.0, y=1.25, z=0.5, facing='BackLeft'))
                
        

                  
                            
        if "!down" in message:
          try:
              await self.highrise.teleport(f"{user.id}", Position(x=18.0, y=1.0, z=27.0, facing='FrontRight'))
          except:
              print("error 3")

            

        #this to buy item from shope with the gold bot have

        if message.lower().startswith("/buy "):
            parts = message.split(" ")
            if len(parts) != 2:
                await self.highrise.chat("Invalid command")
                return
            item_id = parts[1]
            try:
                response = await self.highrise.buy_item('eye-m_01b')
                await self.highrise.chat(f"Item bought: {response}")
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")

        
        #this to find id all items you wear

        if message.lower().startswith("outfit"):
            print(await self.highrise.get_user_outfit(user.id))
       
        if message.lower().startswith("/getinventory"):
            inventory = await self.highrise.get_inventory()
            print (inventory)
        
        if message.lower().startswith("/getoutfit"):
          response = await self.highrise.get_my_outfit()
          for item in response.outfit:
              await self.highrise.chat(item.id)
       
        



        


        
        
        
        #this to emote all you have from p1 to p39 only mods can use


        if message.startswith("p1"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-float", roomUser.id)

        if message.startswith("p2"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-teleporting", roomUser.id)

        if message.startswith("p3"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-shy2", roomUser.id)



        if message.startswith("kawaii"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-kawai", roomUser.id)

        if message.startswith("p4"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id)



        if message.startswith("p5"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)

        if message.startswith("p6"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-flex", roomUser.id)

        if message.startswith("p7"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-employee", roomUser.id)


        if message.startswith("p8"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)

        if message.startswith("p9"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-wild", roomUser.id)

        if message.startswith("p10"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-timejump", roomUser.id)



        if message.startswith("p11"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-iceskating", roomUser.id)

        if message.startswith("p12"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-touch", roomUser.id)

        if message.startswith("p13"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("sit-relaxed", roomUser.id)

        if message.startswith("p14"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-sleigh", roomUser.id)

        if message.startswith("p15"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)

        if message.startswith("p16"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)

        if message.startswith("p17"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)

        if message.startswith("p18"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-uwu", roomUser.id)

        if message.startswith("p19"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)

        if message.startswith("p20"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)

        if message.startswith("p21"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-wrong", roomUser.id)

        if message.startswith("p22"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok9", roomUser.id)





        if message.startswith("p23"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)

        if message.startswith("p24"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-swordfight", roomUser.id)

        if message.startswith("p25"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)

        if message.startswith("p26"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-celebrate", roomUser.id)

        if message.startswith("p27"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)

        if message.startswith("p28"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gravity", roomUser.id)



        if message.startswith("p29"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-creepycute", roomUser.id)

        if message.startswith("p30"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-frog", roomUser.id)

        if message.startswith("p31"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gift", roomUser.id)

        if message.startswith("p32"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-boxer", roomUser.id)

        if message.startswith("p33"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)

        if message.startswith("p34"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-casual", roomUser.id)

        if message.startswith("p35"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hearteyes", roomUser.id)

        if message.startswith("p36"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-exasperatedb", roomUser.id)

        if message.startswith("p37"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-enthusiastic", roomUser.id)

        if message.startswith("p38"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hot", roomUser.id)

        if message.startswith("p39"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)








#this command to know everything about profile user like followers and friens and posts and likes and more !userinfo @name only mods can use it



        
        if message.startswith("!userinfo"):
          if user.username.lower() in self.moderators:
              parts = message.split(" ")
              if len(parts) != 2:
                  await self.highrise.chat("Incorrect format, please use !userinfo <@username>")
                  return
              #Removes the @ from the username if it exists
              if parts[1].startswith("@"):
                  username = parts[1][1:]
              else:
                  username = parts[1]
              #Get the user id from the username
              user = await self.webapi.get_users(username = username, limit=1)
              if user:
                  user_id = user.users[0].user_id
              else:
                  await self.highrise.chat("User not found, please specify a valid user")
                  return

              #Get the user info
              userinfo = await self.webapi.get_user(user_id)
              number_of_followers = userinfo.user.num_followers
              number_of_friends = userinfo.user.num_friends
              number_of_folowing = userinfo.user.num_following
              joined_at = (userinfo.user.joined_at).strftime("%d/%m/%Y %H:%M:%S")
              try:
                  last_login = (userinfo.user.last_online_in).strftime("%d/%m/%Y %H:%M:%S")
              except:
                  last_login = "Last login not available"
              #Get the number of posts and the most liked post
              userposts = await self.webapi.get_posts(author_id = user_id)
              number_of_posts = 0
              most_likes_post = 0
              try:
                  while userposts.last_id != "":
                      for post in userposts.posts:
                          if post.num_likes > most_likes_post:
                              most_likes_post = post.num_likes
                          number_of_posts += 1
                      userposts = await self.webapi.get_posts(author_id = user_id, starts_after=userposts.last_id)
              except Exception as e:
                  print (e)

              #Send the info to the chat
              await self.highrise.chat(f"User: {username}\nNumber of followers: {number_of_followers}\nNumber of friends: {number_of_friends}\nNumber of following: {number_of_folowing}\nJoined at: {joined_at}\nLast login: {last_login}\nNumber of posts: {number_of_posts}\nMost likes in a post: {most_likes_post}")
        
#name item
      
        


        #this replys you can change them if you want


        if message.startswith("!help"):
                help_message = (
                    "Available Commands:\n"
                    "!time @username - Check remaining time for temporary VIP status\n"
                    "!kick @username - Kick a user from the room\n"
                    "!mute @username - Mute a user in the room for 1 hour\n"
                    "!unmute @username - Unmute a muted user\n"
                    "!ban @username - Ban a user from the room for 1 hour\n"
                    "!tip 5 - Tip all users in the room 5 gold bars (charfield736 only)\n"
                    "!tip 1 - Tip all users in the room 1 gold bar (charfield736 only)\n"
                    "/tip 1...10 5g - Tip RANDOM users in the room 5 gold bars (charfield736 only)\n"
                    "/tip 1....10 10g - RANDOM users in the room 1 gold bar (charfield736 only)\n"
                  
                    "Wallet - View the bot's wallet (moderators only)\n"
                    
                    "!down  - Teleport  to a lower location (moderators/VIPs)\n"
                    "!vip @username - Teleport user to a  location (moderators/VIPs)\n"
                    
                    "!dj @username - Teleport user to a  location (moderators/VIPs)\n"
                   
                  
                    
                    # ... (other commands)
                )

                # Chunk the message to avoid exceeding message length limits
                chunk_size = 250
                for i in range(0, len(help_message), chunk_size):
                    chunk = help_message[i : i + chunk_size]
                    await self.highrise.send_whisper(user.id, chunk)

        if message.startswith("!help"):
          help_message = (
              
              "❤️ this reaction make user mod in code permanent (Modrators)\n"
              "😉 this reaction make user mod in code 24h (Modrators)\n"
              "👏  this reaction remove user from  mod in code (Modrators)\n"
              "👏  this reaction remove user from  mod in code (Modrators)\n"
              "👍 This reaction getir any user in any place (moderators)\n"
              


              # ... (other commands)
          )

          # Chunk the message to avoid exceeding message length limits
          chunk_size = 250
          for i in range(0, len(help_message), chunk_size):
              chunk = help_message[i : i + chunk_size]
              await self.highrise.send_whisper(user.id, chunk)

        
  
    async def on_whisper(self, user: User, message: str ) -> None:
        print(f"{user.username} whispered: {message}")
        response = await self.command_handler(user.id, message)
        if response:
            try:
                await self.highrise.send_whisper(user.id, response)
            except Exception as e:
                print(f"Whisper Error: {e}")

        
        if message == "here":
            if user.username.lower() in self.moderators:
                response = await self.highrise.get_room_users()
                users = [content for content in response.content]
                for u in users:
                    if u[0].id == user.id:
                        try:
                            await self.highrise.teleport(Counter.bot_id,Position((u[1].x),(u[1].y),(u[1].z),"FrontRight"))


                            break
                        except:

                            pass
       
        if message.startswith("/say"):
            if user.username.lower() in self.moderators:
                text = message.replace("/say", "").strip()
                await self.highrise.chat(text)

   
         

        elif message.startswith("/come"):
            if user.username.lower() in self.moderators:
                response = await self.highrise.get_room_users()
                your_pos = None
                for content in response.content:
                    if content[0].id == user.id:
                        if isinstance(content[1], Position):
                            your_pos = content[1]
                            break
                if not your_pos:
                    await self.highrise.send_whisper(user.id, "Invalid coordinates!")
                    return
                await self.highrise.chat(f"@{user.username} I'm coming ..")
                await self.highrise.walk_to(your_pos)

        elif message.lower().startswith("follow"):
         
            target_username = message.split("@")[1].strip()

            if target_username.lower() == self.following_username:
                await self.highrise.send_whisper(user.id,"I am already following.")
            elif message.startswith("/say"):
              if user.username.lower() in self.moderators:
                  text = message.replace("/say", "").strip()
                  await self.highrise.chat(text)
            else:
                self.following_username = target_username
                await self.highrise.chat(f"hey {target_username}.")
            
                await self.follow_user(target_username)
        elif message.lower() == "stop following":
            self.following_username = None
          
            await self.highrise.walk_to(Position(16.6,5.64,13.5,"FrontRight"))

  
    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
        _bid = "3924652a4704263c98811b368f2589d5a1c75802ebc826c330f251efa87cddb5"
        _id = f"1_on_1:{_bid}:{user_id}"
        _idx = f"1_on_1:{user_id}:{_bid}"
        _rid = "65ec4568e248187394630dda" 
        response = await self.highrise.get_messages(conversation_id)
        if isinstance(response, GetMessagesRequest.GetMessagesResponse):
            message = response.messages[0].content
            print (message)
        conversation = await self.highrise.get_messages(conversation_id)
        message = conversation.messages[0].content
        response = await self.command_handler(user_id, message)
        if response:
            try:
                await self.highrise.send_message(conversation_id, response)
            except Exception as e:
                print(f"Messaging Error: {e}")
        #this private chat
        
        if message.lower().lstrip().startswith(("hello","hi","ello","hello bot","hi bot","ello bot")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"𝙃𝙚𝙡𝙡𝙤 𝙝𝙣 ")
            a

        #this when user say join bot add him in fans json to send him all news
        
        if message.lower().lstrip().startswith(("join","keep me posted" ,"subscribe","sub","!sub")):
           if conversation_id in self.fans :
             await asyncio.sleep(2)
             await self.highrise.send_message(conversation_id, "You have already joined and i will update you with all upcoming parties .")
           else:
                await asyncio.sleep(2)
          
                conversation_id =conversation_id
                self.fans.append(conversation_id)
                self.save_fans()
                try:
                   await self.highrise.send_message(conversation_id, "𝙉𝙤𝙬 𝙮𝙤𝙪 𝙟𝙤𝙞𝙣 𝙤𝙪𝙧 𝙘𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮! ")
                   await asyncio.sleep(2)
                   await self.highrise.send_message(conversation_id, "𝐖𝐢𝐥𝐥 𝐬𝐞𝐧𝐝 𝐭𝐨 𝐲𝐨𝐮 𝐚𝐥𝐥 𝐧𝐞𝐰𝐬 𝐚𝐧𝐝 𝐞𝐯𝐞𝐧𝐭𝐬! 🎫")
                except Exception as e:
                   print(f"An exception occured: {e}")

        if message.startswith("/say") and conversation_id in moderators:
                text = message.replace("/say", "").strip()
                for conversation_id in self.fans:
                  await asyncio.sleep(2)
                  await self.highrise.send_message(conversation_id,text)
        
          

       
        #this to mute the bot to send invites or messges 
                     
        if message.lower().lstrip().startswith(("leave","mute" ,"unsubscribe")):
          conversation_id = conversation_id
          self.fans.remove(conversation_id)
          self.save_fans()
          await asyncio.sleep(2)
          await self.highrise.send_message(conversation_id, "Partying updates muted! ")

        #this to know how many fans in fans json
          
        if message.lower().lstrip().startswith(("my fans","number of fans")) and conversation_id in moderators:
             fans = json.load(open("fans.json"))
             Fn = len(fans)
             await asyncio.sleep(2)
             await self.highrise.send_message(conversation_id, f"Total number of fans of your club is {Fn} fans.")

        #this to invit all users in fans json
        
        if message.lower().lstrip().startswith(("invite fans", "bring fans", "send invites")) and conversation_id in moderators:
          parts = message[1:].split()
          args = parts[1:]
          url = f"https://webapi.highrise.game/users?&username={args[0][1:]}&sort_order=asc&limit=1"
          response = requests.get(url)
          data = response.json()
          users = data['users']

          for conversation_id in self.fans:
         
              __id = f"1_on_1:{_bid}:{user_id}"
              __idx = f"1_on_1:{user_id}:{_bid}"
              __rid = "6576820f8ed81d395c9f2591" #add id room here
              
          try:
              await self.highrise.send_message(conversation_id, "ᴇᴠᴇɴᴛ ꜱᴛᴀʀᴛ ᴊᴏɪɴ🚀", "invite", __rid)
              await self.highrise.send_message(conversation_id, f"NEW EVENT DJ AND TIP PARTY START BY @Jollyjojo65 🚀")
          except highrise.ResponseError as e:
    # Handle or log the error
              print(f"Failed to send message: {e}")
              
    

    
    async def get_emote_df(self, target) -> None:

        try:
            emote_info = self.emotesdf.get(target)
            return emote_info
        except ValueError:
            pass
       
          
    async def send_continuous_emote(self, emote_id: str, user_id: int,emote_duration: float):
            try:
                while True:
                    await self.highrise.send_emote(emote_id, user_id)
                    await asyncio.sleep(emote_duration)
            except ConnectionResetError:
               if message.lower().lstrip().startswith("loop"):
                parts = message.split("6 ")
                if len(parts) < 2:
                    await self.highrise.chat("Invalid command format. Usage: loop<emote_name> ")
                    return

                emote_name = parts[1]

                if len(parts) >= 3:
                    try:
                        float(parts[2])
                    except ValueError:
                        await self.highrise.chat("Invalid delay value. The delay must be a valid number in seconds.")
                        return
                else:
                    pass  # Default delay of 7.5 seconds
  
    

    async def stop_continuous_emote(self, user_id: int):
      if user_id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user_id].cancelled():
          task = self.continuous_emote_tasks[user_id]
          task.cancel()
          with contextlib.suppress(asyncio.CancelledError):
              await task
          del self.continuous_emote_tasks[user_id]
    
   

        
        


    async def command_handler(self, user_id, message: str):
        if user_id != self.owner_id:  # Only listen to host's commands
            return
        command = message.lower().strip()

        if command.startswith("!set"): # Set the bot at your location
            set_position = await self.set_bot_position(user_id)
            return set_position
        elif command.startswith("!top"): # Build a 10 top tippers leaderboard
            top_tippers = self.get_top_tippers()
            formatted_tippers = []
            for i, (user_id, user_data) in enumerate(top_tippers):
                username = user_data['username']
                total_tips = user_data['total_tips']
                formatted_tippers.append(f"{i + 1}. {username} ({total_tips}g)")

            tipper_message = '\n'.join(formatted_tippers)
            return f"Top Tippers:\n{tipper_message}"
        elif command.startswith("!get "): # Query a specific user's tips
            username = command.split(" ", 1)[1].replace("@", "")
            tip_amount = self.get_user_tip_amount(username)
            if tip_amount is not None:
                return f"{username} has tipped {tip_amount}g"
            else:
                return f"{username} hasn't tipped."
        elif command.startswith("!wallet"): # Get Bot wallet gold
            wallet = await self.highrise.get_wallet()
            for currency in wallet.content:
                if currency.type == 'gold':
                    gold = currency.amount
                    return f"I have {gold}g in my wallet."
            return "No gold in wallet."

    async def on_tip(
        self, sender: User, receiver: User, tip: CurrencyItem | Item
    ) -> None:
        if isinstance(tip, CurrencyItem):
            print(f"{sender.username} tipped {tip.amount}g -> {receiver.username}")
            if receiver.id == self.bot_id:
                if sender.id not in self.tip_data:
                    self.tip_data[sender.id] = {"username": sender.username, "total_tips": 0}

                self.tip_data[sender.id]['total_tips'] += tip.amount
                self.write_tip_data(sender, tip.amount)

                if tip.amount >= 500:
                    await self.highrise.chat(f"Thank you {sender.username} for the generous {tip.amount}g tip!")
        
    async def delayed_message_command(self, message, command):
        # Implementation of delayed_message_command goes here
        pass


    def get_top_tippers(self):
        sorted_tippers = sorted(self.tip_data.items(), key=lambda x: x[1]['total_tips'], reverse=True)
        return sorted_tippers[:10]

    # Return the amount a particular username has tipped
    def get_user_tip_amount(self, username):
        for _, user_data in self.tip_data.items():
            if user_data['username'].lower() == username.lower():
                return user_data['total_tips']
        return None

    # Place bot on start
    async def place_bot(self):
        while self.bot_status is False:
            await asyncio.sleep(0.5)
        try:
            self.bot_position = self.get_bot_position()
            if self.bot_position != Position(0, 0, 0, 'FrontRight'):
                await self.highrise.teleport(self.bot_id, self.bot_position)
                return
        except Exception as e:
            print(f"Error with starting position {e}")

    # Write tip event to file
    def write_tip_data(self, user: User, tip: int) -> None:
        with open("./data.json", "r+") as file:
            data = load(file)
            file.seek(0)
            user_data = data["users"].get(user.id, {"total_tips": 0, "username": user.username})
            user_data["total_tips"] += tip
            user_data["username"] = user.username
            data["users"][user.id] = user_data
            dump(data, file)
            file.truncate()

    # Set the bot position at player's location permanently
    async def set_bot_position(self, user_id) -> None:
        position = None
        try:
            room_users = await self.highrise.get_room_users()
            for room_user, pos in room_users.content:
                if user_id == room_user.id:
                    if isinstance(pos, Position):
                        position = pos

            if position is not None:
                with open("./data.json", "r+") as file:
                    data = load(file)
                    file.seek(0)
                    data["bot_position"] = {
                        "x": position.x,
                        "y": position.y,
                        "z": position.z,
                        "facing": position.facing
                    }
                    dump(data, file)
                    file.truncate()
                set_position = Position(position.x, (position.y + 0.0000001), position.z, facing=position.facing)
                await self.highrise.teleport(self.bot_id, set_position)
                await self.highrise.teleport(self.bot_id, position)
                await self.highrise.walk_to(position)
                return "Updated bot position."
            else:
                return "Failed to update bot position."
        except Exception as e:
            print(f"Error setting bot position: {e}")

    # Load tip data on start
    def load_tip_data(self) -> None:
        with open("./data.json", "r") as file:
            data = load(file)
            self.tip_data = data["users"]

    # Load bot position from file
    def get_bot_position(self) -> Position:
        with open("./data.json", "r") as file:
            data = load(file)
            pos_data = data["bot_position"]
            return Position(pos_data["x"], pos_data["y"], pos_data["z"], pos_data["facing"])


    
    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:
        await asyncio.sleep(5)
        #welcome message
        await self.highrise.send_whisper(user.id, F"welcome @{user.username}")

    async def on_start(self, session_metadata: SessionMetadata) -> None:
      
        Counter.bot_id = session_metadata.user_id
        print("is booting ...")
        pass
        self.load_temporary_vips()
        #this to handle bot place you can find it in console
        self.bot_id = session_metadata.user_id
        self.owner_id = session_metadata.room_info.owner_id
        if self.bot_status:
            await self.place_bot()
        self.bot_status = True
        while True:
            #this to make bot emote loop 
            await asyncio.sleep(5)
            await self.highrise.send_emote(
         random.choice(['emoji-flex', 'dance-tiktok10', 'emote-snake', 'emote-roll', 'emote-superpunch', 'emote-kicking', 'idle-floorsleeping2', 'emote-hero', 'idle_layingdown2', 'idle_layingdown', 'dance-sexy', 'emoji-hadoken', 'emote-disappear', 'emote-graceful', 'sit-idle-cute', 'idle-loop-aerobics', 'dance-orangejustice', 'emote-rest', 'dance-martial-artist', 'dance-breakdance', 'emote-astronaut', 'emote-zombierun', 'idle_singing', 'emote- frollicking', 'emote-float', 'emote-kicking', 'emote-ninjarun', 'emote-secrethandshake', 'emote-apart', 'emote-headball', 'dance-floss', 'emote-jetpack', 'emote-ghost-idle', 'dance-spiritual', 'dance-robotic', 'dance-metal', 'idle-loop-tapdance', 'idle-dance-swinging', 'emote-mindblown', 'emote-gangnam', 'emote-harlemshake', 'emote-robot', 'emote-nightfever', 'dance-anime', 'idle-guitar', 'emote-headblowup', 'dance-creepypuppet', 'emote-creepycute', 'emote-sleigh', 'emote-hyped', 'dance-jinglebell', 'idle-nervous', 'idle-toilet', 'emote-timejump', 'sit-relaxed', 'dance-kawai', 'idle-wild', 'emote-iceskating', 'sit-open', 'dance-touch']))

def data_file(filename: str, default_data: str = "{}") -> None:
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write(default_data)

DEFAULT_DATA = '{"users": {}, "bot_position": {"x": 0, "y": 0, "z": 0, "facing": "FrontRight"}}'
data_file("./data.json", DEFAULT_DATA)
#send to tomyHR IF YOU NEED HELP TY