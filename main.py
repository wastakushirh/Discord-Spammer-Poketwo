from webserver import keep_alive
import requests

channelID = 1018034791754514562 
headers = {
    "authorization":
    "MTAxODE4NTMzNjEyNTM5OTA1MA.G3iP6L.FH3NYT8GvypcTG5kXJdP79l4b5nRS6wfmg96S0"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
