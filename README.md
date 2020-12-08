# spotiBot

This is a stripped down version of the spotify bot running on my discord server. It has been modified to have less features but also not utilize a database.

It was intially created to be used on the [Good Kid](https://twitter.com/goodkidband "Good Kid") discord server. 

## Set-up
#### Spotify authentication
the first thing you're going to need to do is authenticate a spotify application to run with the bot. A guide on how to do that can be found [here](https://developer.spotify.com/documentation/general/guides/authorization-guide/ "here").

#### Discord authentication
Next, you'll want to set up the bot on discord. A good guide on setting up the profile and inviting it to your sever can be found [here](https://discordpy.readthedocs.io/en/latest/discord.html "here"). To be safe, I would just give the bot all scopes as well as admin, but if you would like to configure them to your preferred security level the bot will still work as long as it still has the appropriate access level.

#### Bot configuration

The bot contains a primary config.py file. This is where you will put your authentication tokens. A guide to what goes where can be found below.

```
# SPOTIFY AUTH
clientID = 'PUT SPOTIFY CLIENT ID HERE '
secretID = 'PUT SPOTIFY SECRET ID HERE'
redirect = 'PUT SPOTIFY REDIRECT HERE' 
# Note, this must match what you have configured on the spotify application.

# DISCORD AUTH
passkey = 'PUT DISCORD PASSKEY HERE'
# I have included instructions on how to get this below.

# PLAYLIST IDs
weeklyPlaylist = 'weeklyID'
foreverPlaylist = 'permanentID'

# BOT CONFIG
prefix = "$"
# This is the symbol you will put before commands. This will only really be used by admins.

# SUPERUSERS
superusers = ['258084676994990082'] 
# My user ID was added at Nick's request. Feel free to remove it. This just allows me to remove songs from the playlist in case of spam. Don't remove the entire array, just the ID. 

# If you want, you can even add other Discord user snowflake ID's here in order to allow them to remove tracks.
```

##### Obtaining discord key:
To get the passkey for your bot, navigate to this panel in the Discord Developer Dashboard:

![](https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/discord-bot-copy-token.1228e6cb6cba.png&w=1512&sig=c8c437a86a1fb23a94e35050f5c969f5f20c4814)
