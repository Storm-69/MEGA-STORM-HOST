import os

from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import (
    GetAdminedPublicChannelsRequest,
    LeaveChannelRequest,
)
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User

from userbot.utils import admin_cmd, sudo_cmd
@bot.on(admin_cmd(pattern="pjoin (.*)"))
@bot.on(sudo_cmd(pattern="pjoin (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bc = event.pattern_match.group(1)
    event = await edit_or_reply(event, "Trying Joining")
    try:
        await event.client(ImportChatInviteRequest(bc))
        await event.edit("Succesfully Joined")
    except Exception as e:
        await event.edit(str(e))


@bot.on(admin_cmd(pattern="join (.*)"))
@bot.on(sudo_cmd(pattern="join (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bc = event.pattern_match.group(1)
    event = await edit_or_reply(event, "Trying Joining")
    try:
        await event.client(functions.channels.JoinChannelRequest(channel=bc))
        await event.edit("Succesfully Joined")
    except Exception as e:
        await event.edit(str(e))


@bot.on(admin_cmd(pattern="leave (.*)"))
@bot.on(sudo_cmd(pattern="leave (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bc = int(event.pattern_match.group(1))
    print(bc)
    event = await edit_or_reply(event, "Trying Leaving...")
    try:
        await event.client(LeaveChannelRequest(bc))
        await event.edit("Succesfully Left")
    except Exception as e:
        await event.edit(str(e))

