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

# Releases
## 0.0.0 (Current)
Everything that was mentioned above in the `README.md`.

## 0.0.1
Interface to continually look at your stats in realtime in the form of a dashboard.

## 0.0.2
For users that have Supporter or Legend status, create a dashboard that analyzes the data over time to establish current game lobby level and stat trends over time. 
