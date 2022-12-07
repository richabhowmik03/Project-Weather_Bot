
<h1 align="center">
  <br>
  WeatherBot 🌤
  <br>
</h1>


<h3 align=center>A fully customizable bot built with <a href=https://github.com/Pycord-Development/pycord>Pycord</a></h3>

--------------------------------

<div align=center>
<img src="https://img.icons8.com/color/48/000000/discord--v2.png"/>

<img src="https://img.icons8.com/fluency/48/000000/python.png"/>

<img src="https://img.icons8.com/external-creatype-filed-outline-colourcreatype/48/000000/external-document-file-extension-web-format-file-creatype-filed-outline-colourcreatype-14.png"/>

<img src="https://img.icons8.com/external-flaticons-flat-flat-icons/48/000000/external-api-no-code-flaticons-flat-flat-icons-2.png"/>

<img src="https://img.icons8.com/color/48/000000/bot.png"/>


</div>

<p align="center">
  <a href="#about">About</a>
  •
  <a href="#Features">Features</a>
  •
  <a href="#Dependency">Dependency</a>
  •
  <a href="#Working">Working</a>
</p>


----------------------------------

## ❓ About

Discord Weather Bot is a fully constomizable Discord Bot that is growing constantly.This bot look for a specific command prefix, such as "#" in our example of Weather Bot. When this combination of are primarily is entered on a server where the bot programme is present and has been allowed access to read the messages, the bot is activated and determines which answer to deliver based on the functions specified. The needed output is sent to the guild if the command is found. Occasionally, data is fetched through an [API](https://en.wikipedia.org/wiki/API) request to a third-party service.

----------------------------------------------------------------

## ❗ Features


- Weather Bot is able to perform multiple functions while present in a discord server.
- It can be modified to perform several more functions in the future if required.
- It is able to read messages and commands that are made by the discord users on a server. 
- It is able to forecast the weather details of any city or country when commanded with ``“w city name”`` where the city name is the name of the city of which the user wants to know about the weather.

```python
 if message.content.startswith('#w'):

```
- Thus, any discord user who wants to get a weather forecast of his desired city would have to specify his command to “#w”. 
- It promotes user interaction on the server.
- If we input an invalid city name, the bot will return an error message.

----------------------------------------------------------------------

## 📰 Dependency

- For building this project, I did require multiple things to bring out the final outcome.
- Initially for interacting I had to use the discord API integration, discord.py( “discord.py is a modern, easy to use, feature-rich, and async ready API wrapper for Discord.”).
- But later [Pycord](https://github.com/Pycord-Development/pycord) has been used over [discord.py](https://github.com/Rapptz/discord.py) for the convenience of implementing ``Slash Command``.
- After that for weather forecasting and JSON parsing the libraries and modules used here are requests from the urlib library and JSON for JSON parsing.
- For getting the weather details about any city [OpenWeatherMap](https://en.wikipedia.org/wiki/OpenWeatherMap) API has been used.
- Future potential is that it can be connected to a database like [MongoDB](https://en.wikipedia.org/wiki/MongoDB) for fetching previous Weather history.

----------------------------------
## 🛠 Working

<img width="570" alt="image" src="https://user-images.githubusercontent.com/85113641/183232544-8a3f1186-860b-4325-baf2-061ac856fd1b.png">


<img width="550" alt="image" src="https://user-images.githubusercontent.com/85113641/183232605-f80234f3-3668-427a-9ecd-132eadbc97d9.png">


------------------------

