# ApexLegendsQuery
This is a script to query specific data from the Apex Legends API server. Data obtained will depend on your level for the API. 
Everyone will have access to the API, but Supporter and Legend can only access previous match history. If you are a Supporter or Legend, this will help query for you as well.

## Input File
Your `_secret.json` will hold two values, the `API_KEY` and `PLAYER` items. The file will have a structure like the following:
```
{
"API_KEY": "<YOUR API_KEY OBTAINED FROM https://apexlegendsapi.com/>",
"PLAYER": "<YOUR USERNAME FOR YOUR PLATFORM>", 
"PLATFORM": "X1",
"ACTION": "get"
}
```
This is specific for querying all of the information for a user on Xbox Live. If you would like to query multiple users, you can setup your file accordingly:
```
{
"API_KEY": "<YOUR API_KEY OBTAINED FROM https://apexlegendsapi.com/>",
"PLAYER": ["<PLAYER_1>", "<PLAYER_2>", "<PLAYER_3>"],
"PLATFORM": ["X1", "PS4", "PC"],
"ACTION": ["get", "info", "get"]
}
```

All you need is the path of your `_secret.json` and an API_KEY from the website above and you are good to go!

## Output
A folder will be created in your current working directory (soon to change in release 0.0.1) based off of each Username inside your `_secret.json` file. This folder will contain
3 files:
- `basic_<USERNAME>.json`
- `history_<USERNAME>.json`
- `origin_player_<USERNAME>.json`

Someone with free access will only be able to extract data from `basic_<USERNAME>.json` where someone with Support or Legend status will be able to access all of the files.

# Releases
## 0.0.0 (Current)
Everything that was mentioned above in the `README.md`.

## 0.0.1
Add easier path manipulations for storing User's files in specific locations.

## 0.0.2
Interface to continually look at your stats in realtime in the form of a dashboard.

## 0.0.3
For users that have Supporter or Legend status, create a dashboard that analyzes the data over time to establish current game lobby level and stat trends over time. 
