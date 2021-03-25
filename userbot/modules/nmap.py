import nmap3
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern="^.nmap (.*)")
async def nmap(event):
    await event.edit("`Processing...`")
    ip = event.pattern_match.group(1)
    print(ip)
   


CMD_HELP.update({
    "nmap":
    ".nmap <url/ip>\
    \nUsage: Does a simple port scan on given IP/URL.\
    \nExample of a valid IP : `127.0.0.1`"
})
