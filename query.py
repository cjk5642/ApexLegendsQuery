#!/usr/bin/env python
# coding: utf-8
import json, os
from apex_legends_api import ApexLegendsAPI, ALPlatform, ALAction, ALPlayer

def get_info(path: str) -> str:
    with open(path, 'r') as file:
        f = json.load(file)
        return f['API_KEY'], f['PLAYER'], f['PLATFORM'], f["ACTION"]

PLATFORM_SERVICES = {"X1": ALPlatform.XBOX, "PS4": ALPlatform.PSN, "PC": ALPlatform.PC}
ACTION_SERVICES = {"info": ALAction.INFO, "get": ALAction.GET}

class Apex:
    def __init__(self, API_KEY, PLAYER, PLATFORM, ACTION):
        self.API_KEY = API_KEY
        self.PLAYER = PLAYER
        self.PLATFORM = PLATFORM
        self.ACTION = ACTION
        self.BASE_URL = f"https://api.mozambiquehe.re/bridge?player={self.PLAYER}&platform={self.PLATFORM}&auth={self.API_KEY}&history=1&action=get"
    
    def to_json(self, data, name):
        filename = f"{name}.json"
        filepath = os.path.abspath(filename)
        with open(filepath, 'w') as file:
            json.dump(data, file)
            
    def create_player_folder(self):
        direct = os.getcwd()
        path = os.path.join(direct, self.PLAYER)
        if not os.path.exists(path):
            os.makedirs(path)
        return path
        
    def get_data(self):
        api = ApexLegendsAPI(api_key = self.API_KEY)
        
        basic = api.basic_player_stats(player_name = self.PLAYER, platform = self.PLATFORM)
        history = api.match_history(player_name=self.PLAYER, platform=self.PLATFORM, action=self.ACTION)
        origin_player = api.get_player_origin(player_name=self.PLAYER, show_all_hits=True)
        
        player_path = self.create_player_folder()
        
        self.to_json(basic, os.path.join(player_path, f'basic_{self.PLAYER}'))
        self.to_json(history, os.path.join(player_path, f'history_{self.PLAYER}'))
        self.to_json(origin_player, os.path.join(player_path, f'origin_player_{self.PLAYER}'))

if __name__ == '__main__':
    path = os.path.abspath(str(input("Please input path of your _secret.json.\t")))
    API_KEY, PLAYERS, PLATFORMS, ACTIONS = get_info(path)
    if type(PLAYERS) == list:
        for PLAYER, PLATFORM, ACTION in zip(PLAYERS, PLATFORMS, ACTIONS):
            data = Apex(API_KEY, PLAYER, PLATFORM_SERVICES[PLATFORM], ACTION_SERVICES[ACTION]).get_data()
            print(f"{PLAYER} has been queried.")
    else:
        data = Apex(API_KEY, PLAYERS, PLATFORM_SERVICES[PLATFORMS], ACTION_SERVICES[ACTIONS]).get_data()
        print(f"{PLAYER} has been queried.")

