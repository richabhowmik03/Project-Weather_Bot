import requests 
import discord
import json


# Add your discord token here
token = "<Enter your token here>"

# Create a client
client = discord.Client() 

# When the client is ready, run this code
@client.event 
async def on_ready(): # When the client is ready
    print('We have logged in as {0.user}'.format(client)) # Prints out that the client is ready

# When a message is sent, run this code
@client.event 
async def on_message(message): # When a message is sent
    
    if message.author == client.user: # If the message is from the bot
        return # Do nothing

    #conditioning command messages for the weather
    if message.content.startswith('#w'): #if the message starts with #w or #weather        
        city_name = message.content[slice(3,len(message.content))] #slice the message to get the city name
        my_url = 'https://api.openweathermap.org/data/2.5/weather?q= ' # creating a url to get the weather
        rich_url = '&appid=90bfc1d008683897023cba25d078c9a8' #adding the appid to the url
        final_url = my_url + city_name + rich_url #final url to get the weather
        
        #getting the weather data
        response = requests.get(final_url, stream=True) 
        data = response.json() #converting the response to json
        
        error = data['cod'] #getting the error code
        if (error == '404'): #if the city is not found
            
            embed = discord.Embed(title = "City is not found‼‼‼" , description = "Enter valid city name", color = discord.Color.red()) #creating an embed object
            await message.channel.send(embed=embed) #sending the embed to the channel
        
        #getting the weather data
        rich = data['main'] #getting the main part of the data
        temprature = int(rich['temp'] - 273.15)  #converting kelvin to celsius
        pressure = rich['pressure']  #getting the pressure
        humidity = rich['humidity']  #getting the humidity
        wind_speed = data['wind']['speed'] #getting the wind speed
        feel_like = int(rich['feels_like'] - 273.15)  #converting kelvin to celsius


        #creating the embed 
        for weather in data['weather']: #for each weather in the data
       
            embed = discord.Embed(title = "Weather Report ⛅", description = "This is the Weather Report of " + city_name , color = discord.Color.blue()) #creating an embed object
            embed.set_thumbnail(url='https://openweathermap.org/img/w/' + weather['icon'] + '.png') #setting the thumbnail for the embed
            embed.add_field(name = "Temprature 🌡", value =str(temprature) + ' ' + '°C' , inline = True) #adding a field to the embed
            embed.add_field(name = "Feels Like 🥵", value = str(feel_like) + ' ' + '°C' , inline = True) #adding a field to the embed
            embed.add_field(name = "Pressure 🌞", value = str(pressure) + ' ' + 'hPa', inline = True) #adding a field to the embed
            embed.add_field(name = "Humidity 🌫", value = str(humidity) + ' ' + '%', inline = True) #adding a field to the embed
            embed.add_field(name = "Wind Speed 🌪", value = str(wind_speed) + ' ' + 'm/s', inline = True) #adding a field to the embed
            embed.add_field(name = "Weather Description 🌧", value =weather['description'], inline = True) #adding a field to the embed     
    
            await message.channel.send(embed=embed) #sending the embed to the channel

    else:
        embed = discord.Embed(title = "Error‼‼‼" , description = "Enter valid city name", color = discord.Color.red()) #creating an embed object
        await message.channel.send(embed=embed) #sending the embed to the channel

#running the client
client.run(token) 

