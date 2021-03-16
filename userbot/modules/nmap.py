import nmap3
from userbot import CMD_HELP
from userbot.events import register

@register(pattern="^.ss (.*)", outgoing=True)
async def capture(url):
    """For .ss command, scan the given url and send the result"""
    await url.edit("Processing...")
    nm = nmap3.Nmap()
   




CMD_HELP.update({
    "nmap":
    ".nmap <url/ip>\
    \nUsage: Does a simple port scan on given IP/URL.\
    \nExample of a valid IP : `127.0.0.1`"
})
