from spotipy.oauth2 import SpotifyOAuth
import discord
import spotipy
import re
from configTEST import *

scope = 'playlist-modify-public'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(clientID, secretID, redirect, scope=scope))

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str
    
def IDfromURL(url):
    url = convertTuple(url)
    trackID = url.split('/track/')[1]
    trackID = trackID.split('?')[0]
    return trackID

def addTracks(trackIDs):
    sp.playlist_add_items(weeklyPlaylist,trackIDs) # adds to the weekly playlist
    sp.playlist_add_items(foreverPlaylist,trackIDs) # adds to the forever playlist

def removeTrack(trackID):
    sp.playlist_remove_all_occurrences_of_items(weeklyPlaylist, [trackID]) # removes from the weekly playlist
    sp.playlist_remove_all_occurrences_of_items(foreverPlaylist, [trackID]) # adds to the forever playlist

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

URLregex = "(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"

@client.event
async def on_message(message):
    global urls
    global lastmessage

    if message.author == client.user:
        return

    if "https://open.spotify.com/track" in str(message.content) and not (message.content.startswith(prefix+"remove")):
        if str(message.channel) == str(channelLock):
            curGuild = message.guild.id
            trackIDs = []
            for guild in client.guilds:
                if guild.id == curGuild:
                    break
            lastmessage = message
            urls = re.findall(URLregex, message.content)
            for url in urls:
                urlstring = str(url[0])+"://"+str(url[1])+str(url[2])
                trackID = IDfromURL(url)
                try:
                    sp.track(''.join(url))
                    trackIDs.append(trackID)
                    await message.add_reaction("✅")
                    
                except Exception as e:
                    print("ERROR: "+str(e))
                    await message.add_reaction("❌")
                    await message.channel.send("I couldn't find that track (*"+urlstring+"*) is that a valid link?")

            if len(trackIDs) > 0:
                addTracks(trackIDs)

    if message.content.startswith(prefix+"remove") and (message.author.guild_permissions.administrator or str(message.author.id) in superusers):
        if message.content == (prefix+"remove"):
            for url in urls:
                trackID = IDfromURL(url)
                removeTrack(trackID)
                foctrack = sp.track(''.join(url))
                await lastmessage.remove_reaction("✅", client.user)
                await message.channel.send("Succesfully removed all instances of **" + foctrack['name'] + " - " + foctrack['artists'][0]['name'] + "**!")
        elif (message.author.guild_permissions.administrator or str(message.author.id) in superusers):
            urls = str(message.content).split(' ')
            trackLinks = []
            for url in urls:
                if "https://open.spotify.com/track" in url:
                    removeTrack(IDfromURL(url))
                    foctrack = sp.track(''.join(url))
                    await message.channel.send("Succesfully removed all instances of **" + foctrack['name'] + " - " + foctrack['artists'][0]['name'] + "**!")


client.run(passkey)