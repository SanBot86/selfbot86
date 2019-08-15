# -*- coding: utf-8 -*- 
from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.server import THttpServer,TServer,TProcessPoolServer
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from urllib.parse import quote
from googletrans import Translator
from bs4 import BeautifulSoup
import youtube_dl
from ffmpy import FFmpeg
#from ffmpeg import pypi

cl = LINE("")
cl.log("Auth Token : " + str(cl.authToken))

#=============================================================#
oepoll = OEPoll(cl)
creator = ["uc796c5f7c2558d04bf32dfc4b214eb87"]
owner = ["uc796c5f7c2558d04bf32dfc4b214eb87"]
admin = ["uc796c5f7c2558d04bf32dfc4b214eb87"]
staff = ["uc796c5f7c2558d04bf32dfc4b214eb87"]
clientMid = cl.profile.mid
clientProfile = cl.getProfile()
clientSettings = cl.getSettings()
mid = cl.getProfile().mid
KAC = [cl]
ABC = [cl]
Bots = [mid]
San = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
welcome = []
msg_dict = {}
msg_dict1 = {}

responsename1 = cl.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "changeCover":False,
    "changeVideo":False,
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
 #   "restartPoint": null,
    "userMention":{},
    "timeRestart": {},
    "server": {},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "Limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":False,
    "autolike":False,
    "contact":False,
    "invite":False,
    'autoJoin':False,
    'autoAdd':False,
    'autoBlock':False,
    'Timeline':False,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "mentionKick":False,
    "welcomeOn":False,
    "stickerOn":False,
    "simiSimi":{},
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "unsend":False,
    "mention":"Dasar kang Ngintip....",
    "Respontag":"Apa ngetag tag... tar angen looh...!!",
    "welcome":"Selamat Datang kak !",
    "leave":"Sampai jumpa kk...",
    "comment":" ===AUTO LIKE BY===" + "\n          Bdx Bots" + "\n" + "\n         Open Order" + "\n     Bdx ~ Alka Bots" + "\n" + "\n => Only Self" + "\n => SelfBot + 1 Asist" + "\n => SelfBot + 2 Asist" + "\n => SelfBot + 5 Asist" + "\n => SelfBot + 10 Asist" + "\n => Bot Protect" + "\n => Protect Room" + "\n => Pembekuan Akun Smule" + "\n" + "\n       ~~BERMINAT~~" +"\n               HUB LINE" + "\n" + "\n => ID::line.me/ti/p/~bdx26518" + "\n => ID::line.me/ti/p/~Alka0121" + "\n" + "\n=> SUPORT BY:" + "\n" + "\n GHOST RIDER SQUAD",
    "message":"San Bots",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

coverId = cl.getProfileDetail()["result"]["objectId"]
myProfile["displayName"] = clientProfile.displayName
myProfile["statusMessage"] = clientProfile.statusMessage
myProfile["pictureStatus"] = clientProfile.pictureStatus
cont = cl.getContact(clientMid)
apikey_com = "u0ac948397fbc732bd3bc5ca273faa698"
Extr = cl.getContact(apikey_com).displayName

with open('creator.json', 'r') as fp:
     creator = json.load(fp)
with open('owner.json', 'r') as fp:
     owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
Setmain = json.load(Setbot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def backupData():
    try:
        backup = settings
        f = codecs.open('setingan.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False  
		    
def logError(text):
    cl.log("TERJADI ERROR : " + str(text))
    time_ = datetime.now()
    with open("error.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def Musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+cl.getContact(clientMid).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': cl.getContact(clientMid).statusMessage if cl.getContact(clientMid).statusMessage != '' else 'creator By |ID LINE|\nbdx26518', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': cl.getContact(clientMid).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+clientMid,'MSG_SENDER_NAME':  cl.getContact(clientMid).displayName,}
    return cl.sendMessage(to, cl.getContact(clientMid).displayName, contentMetadata, 19)

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "「 Daftar Member 」\n\n♠1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "Oye{}. ".format(str(no))
            else:
                textx += "\n「 Total {} Member 」".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
           
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Tukang {} Sider 」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Auto Welcome 」\nHallo ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+" Di "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "「 Respon Leave 」\nBaper Ya Kak ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]

def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "Help Menu\n\n" + \
                  "「🌠」 " + key + "Me\n" + \
                  "「🌠」 " + key + "Mid「@」\n" + \
                  "「🌠」 " + key + "Steal「@」\n" + \
                  "「🌠」 " + key + "Cover「@」\n" + \
                  "「🌠」 " + key + "Kick「@」\n" + \
                  "「🌠」 " + key + "Restore\n" + \
                  "「🌠」 " + key + "Reject\n" + \
                  "「🌠」 " + key + "Mybot\n" + \
                  "「🌠」 " + key + "Setting\n" + \
                  "「🌠」 " + key + "About\n" + \
                  "「🌠」 " + key + "Restart\n" + \
                  "「🌠」 " + key + "Runtime\n" + \
                  "「🌠」 " + key + "Creator\n" + \
                  "「🌠」 " + key + "Speed/Sp\n" + \
                  "「🌠」 " + key + "Respontime\n" + \
                  "「🌠」 " + key + "Mention-Cipok\n" + \
                  "「🌠」 " + key + "Bye me\n" + \
                  "「🌠」 " + key + "Leave「Namagrup」\n" + \
                  "「🌠」 " + key + "Ginfo\n" + \
                  "「🌠」 " + key + "Open\n" + \
                  "「🌠」 " + key + "Close\n" + \
                  "「🌠」 " + key + "Url\n" + \
                  "「🌠」 " + key + "Gruplist\n" + \
                  "「🌠」 " + key + "Open「nomer」\n" + \
                  "「🌠」 " + key + "Close「nomer」\n" + \
                  "「🌠」 " + key + "Infogrup「nomer」\n" + \
                  "「🌠」 " + key + "Infomem「nomer」\n" + \
                  "「🌠」 " + key + "Remove chat\n" + \
                  "「🌠」 " + key + "Lurking「on/off」\n" + \
                  "「🌠」 " + key + "Lurkers\n" + \
                  "「🌠」 " + key + "Sider「on/off」\n" + \
                  "「🌠」 " + key + "Updatefoto\n" + \
                  "「🌠」 " + key + "Updategrup\n" + \
                  "「🌠」 " + key + "Updatebot\n" + \
                  "「🌠」 " + key + "Broadcast:「Text」\n" + \
                  "「🌠」 " + key + "Setkey「New Key」\n" + \
                  "「🌠」 " + key + "Mykey\n" + \
                  "「🌠」 " + key + "Resetkey\n" + \
                  "\n「============Turn In Media ============」\n" + \
                  "「🌠」 " + key + "Listmp3\n" + \
                  "「🌠」 " + key + "Listvideo\n" + \
                  "「🌠」 " + key + "Listimage\n" + \
                  "「🌠」 " + key + "Liststicker\n" + \
                  "「🌠」 " + key + "Addimg「Teks」\n" + \
                  "「🌠」 " + key + "Dellimg「Teks」\n" + \
                  "「🌠」 " + key + "Addmp3「Teks」\n" + \
                  "「🌠」 " + key + "Dellmp3「Teks」\n" + \
                  "「🌠」 " + key + "Addvideo「Teks」\n" + \
                  "「🌠」 " + key + "Dellvideo「Teks」\n" + \
                  "「🌠」 " + key + "Addsticker「Teks」\n" + \
                  "「🌠」 " + key + "Dellsticker「Teks」\n" + \
                  "「🌠」 " + key + "Spamtag:「jumlahnya」\n" + \
                  "「🌠」 " + key + "Spamtag「@」\n" + \
                  "「🌠」 " + key + "Spamcall:「jumlahnya」\n" + \
                  "「🌠」 " + key + "Spamcall\n" + \
                  "「🌠」 " + key + "Musik「Nama Penyanyi」\n" + \
                  "「🌠」 " + key + "Music penyanyi judul\n" + \
                  "「🌠」 " + key + "mp4\n" + \
                  "「🌠」 " + key + "Ytmp4:\n" + \
                  "「🌠」 " + key + "Line「ID Line」\n" + \
                  "「🌠」 " + key + "Apk「Query」\n" + \
                  "「🌠」 " + key + "Get-gif「Query」\n" + \
                  "「🌠」 " + key + "Anime「Query」\n" + \
                  "「🌠」 " + key + "Mimpi「Query」\n" + \
                  "「🌠」 " + key + "Get-audio「Query」\n" + \
                  "「🌠」 " + key + "Get-mp3「Query」\n" + \
                  "「🌠」 " + key + "Get-video「Query」\n" + \
                  "「🌠」 " + key + "Bintang「Zodiak」\n" + \
                  "「🌠」 " + key + "Zodiak「Zodiak」\n" + \
                  "「🌠」 " + key + "Cuaca「Nama Kota」\n" + \
                  "「🌠」 " + key + "Lokasi「Nama Kota」\n" + \
                  "「🌠」 " + key + "Lirik「Judul Lagu」\n" + \
                  "「🌠」 " + key + "Instagram「User Name」\n" + \
                  "「🌠」 " + key + "Date「tgl-bln-thn」\n" + \
                  "\n「============ Setting Protection============ 」\n\n" + \
                  "「🌠」 " + key + "Notag「on/off」\n" + \
                  "「🌠」 " + key + "Protecall「on/off」\n" + \
                  "「🌠」 " + key + "Protecturl「on/off」\n" + \
                  "「🌠」 " + key + "Protectjoin「on/off」\n" + \
                  "「🌠」 " + key + "Protectkick「on/off」\n" + \
                  "「🌠」 " + key + "Protectinvite「on/off」\n" + \
                  "「🌠」 " + key + "Protectcancel「on/off」\n" + \
                  "\n「============ Setting User ============」\n" + \
                  "「🌠」 " + key + "Invite「on/off」\n" + \
                  "「🌠」 " + key + "Sticker「on/off」\n" + \
                  "「🌠」 " + key + "Unsend「on/off」\n" + \
                  "「🌠」 " + key + "Respon「on/off」\n" + \
                  "「🌠」 " + key + "Timeline「on/off」\n" + \
                  "「🌠」 " + key + "Autolike「on/off」\n" + \
                  "「🌠」 " + key + "Contact「on/off」\n" + \
                  "「🌠」 " + key + "Autojoin「on/off」\n" + \
                  "「🌠」 " + key + "Autoadd「on/off」\n" + \
                  "「🌠」 " + key + "Welcome「on/off」\n" + \
                  "「🌠」 " + key + "Autoleave「on/off」\n" + \
                  "「🌠」 " + key + "Jointicket「on/off」\n" + \
                  "\n「============ For Admin ============」\n\n" + \
                  "「🌠」 " + key + "Staff:on\n" + \
                  "「🌠」 " + key + "Staff:expell\n" + \
                  "「🌠」 " + key + "Admin:on\n" + \
                  "「🌠」 " + key + "Admin:expell\n" + \
                  "「🌠」 " + key + "Staffadd「@」\n" + \
                  "「🌠」 " + key + "Staffdell「@」\n" + \
                  "「🌠」 " + key + "Adminadd「@」\n" + \
                  "「🌠」 " + key + "Admindell「@」\n" + \
                  "「🌠」 " + key + "Refresh\n" + \
                  "「🌠」 " + key + "Listbot\n" + \
                  "「🌠」 " + key + "Listadmin\n" + \
                  "「🌠」 " + key + "Listprotect\n" + \
                  "\nKetik「 Refresh 」jika sudah\nmenggunakan command diatas...\n"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "Help Menu 2\n\n" + \
                  "「🌠」 " + key + "Blc\n" + \
                  "「🌠」 " + key + "Ban:on\n" + \
                  "「🌠」 " + key + "Unban:on\n" + \
                  "「🌠」 " + key + "Ban「@」\n" + \
                  "「🌠」 " + key + "Unban「@」\n" + \
                  "「🌠」 " + key + "Talkban「@」\n" + \
                  "「🌠」 " + key + "Untalkban「@」\n" + \
                  "「🌠」 " + key + "Talkban:on\n" + \
                  "「🌠」 " + key + "Untalkban:on\n" + \
                  "「🌠」 " + key + "Banlist\n" + \
                  "「🌠」 " + key + "Talkbanlist\n" + \
                  "「🌠」 " + key + "Clearban\n" + \
                  "「🌠」 " + key + "Refresh\n" + \
                  "\n「 Check Settings 」\n\n" + \
                  "「🌠」 " + key + "Cek sider\n" + \
                  "「🌠」 " + key + "Cek comment\n" + \
                  "「🌠」 " + key + "Cek spam\n" + \
                  "「🌠」 " + key + "Cek pesan \n" + \
                  "「🌠」 " + key + "Cek respon \n" + \
                  "「🌠」 " + key + "Cek leave\n" + \
                  "「🌠」 " + key + "Cek welcome\n" + \
                  "「🌠」 " + key + "Set sider:「Text」\n" + \
                  "「🌠」 " + key + "Set comment:「Text」\n" + \
                  "「🌠」 " + key + "Set spam:「Text」\n" + \
                  "「🌠」 " + key + "Set pesan:「Text」\n" + \
                  "「🌠」 " + key + "Set respon:「Text」\n" + \
                  "「🌠」 " + key + "Set leave:「Text」\n" + \
                  "「🌠」 " + key + "Set welcome:「Text」\n" + \
                  "「🌠」 " + key + "Myname:「Nama」\n" + \
                  "「🌠」 " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "「🌠」 " + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "\nKetik「 Refresh 」jika sudah\nmenggunakan command diatas...\n"
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = cl.reissueGroupTicket(op.param1)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.updateGroup(X)
                except:
                    pass

        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Sorry anda bukan admin selfbot\nSelamat tinggal " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " + str(ginfo.name))

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                     try:
                         cl.kickoutFromGroup(op.param1,[op.param2])
                     except:
                         pass
     
                return

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            print ("INFO SELBOT : ADA YANG ADD")
            cl.sendMessage(op.param1, " === BLACK DEATH XEVEN BOTS === \nTERIMAKASIH {} SUDAH ADD\n\n🌠 ™ᴏᴘᴇɴ ᴏʀᴅᴇʀ™ 🌠\n\n🌠 ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n🌠 sʙ ᴏɴʟʏ\n🌠 sʙ + ᴀsɪsᴛ\n🌠 sʙ + ᴀsɪsᴛ + ᴀɴᴛɪ ᴊs\n\n🌠 ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ 🌠\n🌠 ʀᴏᴏᴍ sᴍᴜʟᴇ\n🌠 ʀᴏᴏᴍ ᴇᴠᴇɴᴛ\n🌠 ʀᴏᴏᴍ ᴏʟsʜᴏᴘ\n🌠 VIP Smule\n🌠 Siri\n🌠 ᴅᴀɴ ʟᴀɪɴ\n\nNb :\nJika blm memiliki akun, kami sediakan akun\n\nKᴇᴛᴇRᴀɴɢᴀɴ Lᴇʙɪʜ ʟᴀNᴊᴜᴛ, dan Jɪᴋᴀ ᴀɴᴅᴀ ʙᴇʀᴍɪɴᴀᴛ.SɪʟᴀHᴋᴀɴ Pᴄ/Pᴍ Link\n\n🌠 https://line.me/ti/p/~alka0121\n🌠 http://line.me/ti/p/~bdx26518\n   🌠🌠🌠Bdx Bots🌠🌠🌠\nTERIMAKASIH...🙏🏻🙏🏻🙏🏻 ".format(str(cl.getContact(op.param1).displayName)))

        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    cl.kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

            return

        if op.type == 55:
            try:
                if op.param1 in Setmain["AKreadPoint"]:
                   if op.param2 in Setmain["AKreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["AKreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        ginfo = cl.getGroup(op.param1)
                        contact = cl.getContact(op.param2).picturePath
                        image = 'http://dl.profile.line.naver.jp'+contact
                        cl.sendImageWithURL(op.param1, image) 

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                   if msg._from in wait["blacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              cl.kickoutFromGroup(msg.to, [msg._from])
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              cl.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              cl.kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           saints = cl.getContact(msg._from)
                           sendMention(msg.to, saints.mid, "", wait["Respontag"])
                           #cl.sendMessage(msg.to, None, contentMetadata={"PRDID":"a0768339-c2d3-4189-9653-2909e9bb6f58","PRDTYPE":"THEME","MSGTPL":"6"}, contentType=9)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["mentionKick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in admin:
                           cl.sendMessage(msg.to, "Jangan tag saya ogeb")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "「 Detail Postingan 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\n• Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n• Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n• Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n• Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            cl.sendMessage(to, str(ret_))
                            #channel.like(url[25:58], url[66:], likeType=1006)
                            #channel.comment(url[25:58], url[66:], wait["message"])
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                if wait["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[class~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• STICKER ID : {}".format(stk_id)
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n• STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(pkg_id)
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
                        else:
                            ret_ = "「 Sticker Info 」"
                            ret_ += "\n• PRICE : "+soup.findAll('p', attrs={'class':'mdCMN08Price'})[0].text
                            ret_ += "\n• AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\n• STICKER ID : {}".format(str(stk_id))
                            ret_ += "\n• STICKER PACKAGES ID : {}".format(str(pkg_id))
                            ret_ += "\n• STICKER VERSION : {}".format(str(stk_ver))
                            ret_ += "\n• STICKER URL : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\n• DESCRIPTION :\n"+soup.findAll('p', attrs={'class':'mdCMN08Desc'})[0].text
                            cl.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = cl.downloadFileURL(data)
                               cl.sendImage(msg.to,path)
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to," 「 Contact Info 」\n「✭」 Nama : " + msg.contentMetadata["displayName"] + "\n「✭」 MID : " + msg.contentMetadata["mid"] + "\n「✭」 Status Msg : " + contact.statusMessage + "\n「✭」 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in admin:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            cl.sendMessage(msg.to, "「Dia ke bl kak... hpus bl dulu lalu invite lagi」")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  cl.findAndAddContactsByMid(target)
                                  cl.inviteIntoGroup(msg.to,[target])
                                  ryan = cl.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  "「 Sukses Invite 」\nNama "
                                  ret_ = "「Ketik Invite off jika sudah done」"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  cl.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  cl.sendMessage(msg.to,"Anda terkena limit")
                                  wait["invite"] = False
                                  break
               if msg.contentType == 16:
                   if wait["autolike"] == True:
                       url_post = msg.contentMetadata['postEndUrl']
                       pliter = url_post.replace('line://home/post?userMid=','')
                       pliter = pliter.split('&postId=')
                       cl.likePost(mid=pliter[0],postId=pliter[1])
                       cl.createComment(mid=pliter[0],postId=pliter[1],text=wait["comment"])
                       cl.sendMessage(to,'Like Success')
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot saints")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if wait["Addimage"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        images[wait["Addimage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(wait["Addimage"]["name"])))
                        wait["Addimage"]["status"] = False                
                        wait["Addimage"]["name"] = ""
               if msg.contentType == 2:
                 if msg._from in admin:
                    if wait["Addvideo"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        videos[wait["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(wait["Addvideo"]["name"])))
                        wait["Addvideo"]["status"] = False                
                        wait["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["Addsticker"]["status"] == True:
                        stickers[wait["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(wait["Addsticker"]["name"])))
                        wait["Addsticker"]["status"] = False                
                        wait["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                 if msg._from in admin:
                    if wait["Addaudio"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        audios[wait["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(wait["Addaudio"]["name"])))
                        wait["Addaudio"]["status"] = False                
                        wait["Addaudio"]["name"] = ""
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")
               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["AKfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["AKfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")
               if msg.contentType == 2:
                   if msg._from in admin:
                       if mid in Setmain["AKvideo"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["AKvideo"][mid]
                            cl.updateProfileVideoPicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah jadi video")

               if msg.contentType == 0:
                 if Setmain["autoRead"] == True:
                     cl.sendChatChecked(msg.to, msg_id)
                 if text is None:
                     return
                 else:
                        for sticker in stickers:
                         if msg._from in admin:
                           if text.lower() == sticker:
                              sid = stickers[text.lower()]["STKID"]
                              spkg = stickers[text.lower()]["STKPKGID"]
                              cl.sendSticker(to, spkg, sid)
                        for image in images:
                         if msg._from in admin:
                           if text.lower() == image:
                              cl.sendImage(msg.to, images[image])
                        for audio in audios:
                         if msg._from in admin:
                           if text.lower() == audio:
                              cl.sendAudio(msg.to, audios[audio])
                        for video in videos:
                         if msg._from in admin:
                           if text.lower() == video:
                              cl.sendVideo(msg.to, videos[video])
                        cmd = command(text)
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "help" or text.lower() == 'menu':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage = help()
                                didik = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Selfbot Command 」\n• User : "
                                ret_ = str(helpMessage)
                                ry = str(didik.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':didik.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "help2" or text.lower() == 'menu2':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                helpMessage = helpbot()
                                didik = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Setting Blacklist 」\n• User : "
                                ret_ = str(helpMessage)
                                ry = str(didik.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':didik.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "\n「Settings List Protection」\n"
                                if wait["mentionKick"] == True: md+="🔵  Notag 🔛\n"
                                else: md+="🔶  Notag 📴\n"
                                if wait["stickerOn"] == True: md+="🔵  Sticker 🔛\n"
                                else: md+="🔶  Sticker 📴\n"
                                if wait["contact"] == True: md+="🔵  Contact 🔛\n"
                                else: md+="🔶  Contact 📴\n"
                                if wait["talkban"] == True: md+="🔵  Talkban 🔛\n"
                                else: md+="🔶  Talkban 📴\n"
                                if wait["unsend"] == True: md+="🔵  Unsend 🔛\n"
                                else: md+="🔶  Unsend 📴\n"
                                if wait["detectMention"] == True: md+="🔵  Respon 🔛\n"
                                else: md+="🔶  Respon 📴\n"
                                if wait["Timeline"] == True: md+="🔵  Timeline 🔛\n"
                                else: md+="🔶  Timeline 📴\n"
                                if wait["autoJoin"] == True: md+="🔵  Autojoin 🔛\n"
                                else: md+="🔶  Autojoin 📴\n"
                                if wait["autoAdd"] == True: md+="🔵  Autoadd 🔛\n"
                                else: md+="🔶  Autoadd 📴\n"
                                if settings["autoJoinTicket"] == True: md+="🔵  Jointicket 🔛\n"
                                else: md+="🔶  Jointicket 📴\n"
                                if msg.to in welcome: md+="🔵  Welcome 🔛\n"
                                else: md+="🔶  Welcome 📴\n"
                                if wait["autoLeave"] == True: md+="🔵  Autoleave 🔛\n"
                                else: md+="🔶  Autoleave 📴\n"
                                if msg.to in protectqr: md+="🔵  Protecturl 🔛\n"
                                else: md+="🔶  Protecturl 📴\n"
                                if msg.to in protectjoin: md+="🔵  Protectjoin 🔛\n"
                                else: md+="🔶  Protectjoin 📴\n"
                                if msg.to in protectkick: md+="🔵  Protectkick 🔛\n"
                                else: md+="🔶  Protectkick 📴\n"
                                if msg.to in protectinvite: md+="🔵  Protectinvite 🔛\n"
                                else: md+="🔶  Protectinvite 📴\n"
                                if msg.to in protectcancel: md+="🔵  Protectcancel 🔛\n"
                                else: md+="🔶  Protectcancel 📴\n"
                                ginfo = cl.getGroup(msg.to)
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Selfbot Settings 」\n• User : "
                                ret_ = "• Group : {}\n".format(str(ginfo.name))
                                ret_ += str(md)
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + "\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendText(msg.to,"Ciluuu baaa") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd.startswith('about'):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            try:
                                arr = []
                                today = datetime.today()
                                thn = 2018 
                                bln = 12     #isi bulannya yg sewa
                                hr = 17    #isi tanggalnya yg sewa
                                future = datetime(thn, bln, hr)
                                days = (str(future - today))
                                comma = days.find(",")
                                days = days[:comma]
                                contact = cl.getContact(mid)
                                favoritelist = cl.getFavoriteMids()
                                grouplist = cl.getGroupIdsJoined()
                                contactlist = cl.getAllContactIds()
                                blockedlist = cl.getBlockedContactIds()
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                start = time.time()
                                cl.sendText("uaefd813e590d5a1f51419ccf7a745cfc", '.')
                                elapsed_time = time.time() - start
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Informasi Selfbot 」\n• User : "
                                ret_ = "• Group : {} Group".format(str(len(grouplist)))
                                ret_ += "\n• Friend : {} Friend".format(str(len(contactlist)))
                                ret_ += "\n• Blocked : {} Blocked".format(str(len(blockedlist)))
                                ret_ += "\n• Favorite : {} Favorite".format(str(len(favoritelist)))
                                ret_ += "\n• Version : 「 Bdx-Alka Bots」"
                                ret_ += "\n• Expired : {} - {} - {}".format(str(hr), str(bln), str(thn))
                                ret_ += "\n• In days : {} again".format(days)
                                ret_ += "\n「 Speed Respon 」\n• {} detik".format(str(elapsed_time))
                                ret_ += "\n「 Selfbot Runtime 」\n• {}".format(str(bot))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendContact(to, "uaefd813e590d5a1f51419ccf7a745cfc")
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd == "me":
                          if msg._from in admin:
                            cl.sendContact(to, sender)

                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)

                        elif cmd.startswith("mid "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Steal " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               a = channel.getProfileCoverURL(mid=key1)
                               cl.sendMessage(msg.to, "「 Contact Info 」\n• Nama : "+str(mi.displayName)+"\n• Mid : " +key1+"\n• Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                                   cl.sendImageWithURL(receiver, a)
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                                   cl.sendImageWithURL(receiver, a)

                        elif ("Cover " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    cl.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    cl.sendMessage(receiver, str(e))

                        elif ("Sticker: " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    query = msg.text.replace("Sticker: ", "")
                                    query = int(query)
                                    if type(query) == int:
                                        cl.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        cl.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        cl.sendMessage(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    cl.sendMessage(receiver, str(e))

                        elif "/ti/g/" in msg.text.lower():
                           if msg._from in admin:
                             if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                    if l not in n_links:
                                       n_links.append(l)
                                 for ticket_id in n_links:
                                    group = cl.findGroupByTicket(ticket_id)
                                    cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "Tidak ada undangan yang tertunda")

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("brodcash: "):
                          if wait["selfbot"] == True:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))
                                
                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Setkey 」\nSetkey saat ini「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「 Change Setkey 」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「 Resetkey 」\nSetkey mu telah direset")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 Restarting 」\nUser ", "\nTunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                eltime = time.time() - mulai
                                bot = runtime(eltime)
                                ryan = cl.getContact(mid)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Runtime 」\n• User Self : "
                                ret_ = "• {}".format(str(bot))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "「 Group Info 」\n「✭」 Nama Group : {}".format(G.name)+ "\n「✭」 ID Group : {}".format(G.id)+ "\n「✭」 Pembuat : {}".format(G.creator.displayName)+ "\n「✭」 Waktu Dibuat : {}".format(str(timeCreated))+ "\n「✭」 Jumlah Member : {}".format(str(len(G.members)))+ "\n「✭」 Jumlah Pending : {}".format(gPending)+ "\n「✭」 Group Qr : {}".format(gQr)+ "\n「✭」 Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "「 Group Info 」"
                                ret_ += "\n║⊛  Nama Group : {}".format(G.name)
                                ret_ += "\n║⊛  ID Group : {}".format(G.id)
                                ret_ += "\n║⊛  Pembuat : {}".format(gCreator)
                                ret_ += "\n║⊛  Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n║⊛  Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n║⊛  Jumlah Pending : {}".format(gPending)
                                ret_ += "\n║⊛  Group Qr : {}".format(gQr)
                                ret_ += "\n║⊛  Group Ticket : {}".format(gTicket)
                                ret_ += "\n║⊛  Picture Url : http://dl.profile.line-cdn.net/{}".format(G.pictureStatus)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except:
                                pass

                        elif cmd.startswith("leavegrup "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    ginfo = cl.getGroup(group)
                                    gCreator = ginfo.creator.mid
                                    recky = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「」 '
                                    reck = str(recky.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':recky.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan+zxc + "「Next Mapir Lagi」" 
                                    cl.sendMessage(group, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    cl.sendImageWithURL(group,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=u48c350911cde6604da051d9da06c5db7&oid=faadb1b4f3991376bdccbd5700545da6")
                                    cl.leaveGroup(group)
                                except:
                                    cl.sendMessage(msg.to, "Grup itu tidak ada")
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ginfo = cl.getGroup(group)
                                gCreator = ginfo.creator.mid
                                reck = cl.getContact(gCreator)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = '「 Sukses Leave Group 」\n• Creator :  '
                                recky = str(reck.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':reck.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                ret_ += xpesan +zxc
                                ret_ += "• Nama grup : {}".format(G.name)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Jumlah Member : {}".format(str(len(G.members)))
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as e:
                                cl.sendMessage(to, str(e))

                        elif cmd.startswith("leaveall "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    cl.sendText(group,"")
                                    cl.leaveGroup(group)
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Leave Group 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    cl.sendMessage(msg.to, "Grup itu tidak ada")
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama grup : {}".format(G.name)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Jumlah Member : {}".format(str(len(G.members)))
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as e:
                                cl.sendMessage(to, str(e))

                        elif cmd.startswith("open "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Open Qr 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama : {}".format(G.name)
                                ret_ += "\n• Group Qr : {}".format(gQr)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass

                        elif cmd.startswith("close "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                try:
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Sukses Close Qr 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama : {}".format(G.name)
                                ret_ += "\n• Group Qr : {}".format(gQr)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except:
                                pass
                                
                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "「✭」 "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"「✭」 Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("protectqr|on "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    protectqr[G] = True
                                    f=codecs.open('protectqr.json','w','utf-8')
                                    json.dump(protectqr, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    gCreator = G.creator.mid
                                    dia = cl.getContact(gCreator)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '「 Protect Qr Diaktifkan 」\n• Creator :  '
                                    diaa = str(dia.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                except:
                                    cl.sendMessage(msg.to, "Grup itu tidak ada")
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += xpesan+zxc
                                ret_ += "• Nama grup : {}".format(G.name)
                                ret_ += "\n• Pendingan : {}".format(gPending)
                                ret_ += "\n• Jumlah Member : {}".format(str(len(G.members)))
                                cl.sendMessage(receiver, ret_, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as e:
                                cl.sendMessage(to, str(e))

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Grup "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"☑Sukses membersihkan " +mc)
                              
                        elif cmd == "listadmin" or text.lower() == 'listadmin':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    a = a + 1
                                    end = '\n'
                                    mb += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    a = a + 1
                                    end = '\n'
                                    mc += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 Daftar Admin 」\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Pengguna Selfbot" %(str(len(owner)+len(admin)+len(staff))))
                              
#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["AKfoto"][mid] = True
                                cl.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["AKvideo"][mid] = True
                                cl.sendMessage(msg.to,"Kirim videonya.....")

                        elif cmd.startswith("meup: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "mention" or text.lower() == "cipok":
                          if msg._from in admin:
                                group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    cl.sendMessage(to, "Total {} Mention".format(str(len(nama))))

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 Daftar User Bot 」\n\n"+ma+"\nTotal「%s」List Bots" %(str(len(Bots))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    mb += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    md += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    mc += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    me += str(a) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"「 Daftar Protection 」\n\n「✭」 PROTECT URL :\n"+ma+"\n「✭」 PROTECT KICK :\n"+mb+"\n「✭」 PROTECT JOIN :\n"+md+"\n「✭」 PROTECT CANCEL:\n"+mc+"\n「✭」 PROTECT INVITE:\n"+me+"\nTotal「%s」Grup diamankan" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                sendMention(msg.to, sender, "Ada Kak !!!", "")

                        elif cmd == "bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "Sampai Jumpa "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd == "rtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "「 Respontime 」\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               sendMention(msg.to, sender, "「 Selfbot Speed 」\n• User ", "")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                                
                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['AKreadPoint'][msg.to] = msg_id
                                 Setmain['AKreadMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "「 Status Lurking 」\nBerhasil diaktifkan, selanjutnya ketik lurkers\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['AKreadPoint'][msg.to]
                                 del Setmain['AKreadMember'][msg.to]
                                 cl.sendMessage(msg.to, "「 Status Lurking 」\nBerhasil dimatikan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                            
                        elif cmd == "lurkers":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                            if msg.to in Setmain['AKreadPoint']:
                                if Setmain['AKreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['AKreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  「 Daftar Member 」    \n\n 「 Total {} Sider 」\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['AKreadPoint'][msg.to]
                                        del Setmain['AKreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['AKreadPoint'][msg.to] = msg.id
                                    Setmain['AKreadMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "「 Status Sider 」\nBerhasil diaktifkan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "「 Status Sider 」\nBerhasil dimatikan\n\n• Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"+"\n• Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d'))
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("audio "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " "," ")
                            cond = query.split("|")
                            search = str(cond[0])
                            with requests.session() as web:
                                web.headers["User-Agent"] = "Mozilla/5.0"
                                result = web.get("https://farzain.xyz/api/premium/yt_search.php?apikey=apikey_saintsbot&id={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    if data["respons"] != []:
                                        num = 0
                                        ret_ = "「 Pencarian Audio 」\n"
                                        for res in data["respons"]:
                                            num += 1
                                            ret_ += "\n {}. {}".format(str(num), str(res['title']))
                                        ret_ += "\n\n Total {} Result".format(str(len(data["respons"])))
                                        cl.sendMessage(msg.to, str(ret_))
                                        cl.sendMessage(to, "Ketik Get-yt {} | angka\nuntuk melihat detail lagu".format(str(search)))
                                if len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["respons"]):
                                        res = data["respons"][num - 1]
                                        with requests.session() as web:
                                            web.headers["User-Agent"] = "Mozilla/5.0"
                                            result = web.get("http://rahandiapi.herokuapp.com/youtubeapi?key=betakey&q=https://www.youtube.com/watch?v={}".format(str(res['video_id'])))
                                            data = result.text
                                            data = json.loads(data)
                                            ret_ = "「 Detail Lagu 」\nTitle : "+data['result']['title']
                                            ret_ += "\nLikes : "+str(data['result']['likes'])
                                            ret_ += "\nDislikes : "+str(data['result']['dislikes'])
                                            ret_ += "\nDuration : "+str(data['result']['duration'])
                                            ret_ += "\nRating : "+str(data['result']['rating'])
                                            ret_ += "\nAuthor : "+str(data['result']['author'])+"\n"
                                            cover = data['result']['thumbnail']
                                            if data["result"]["audiolist"] != []:
                                                for koplok in data["result"]["audiolist"]:
                                                    ret_ += "\nType : "+koplok['extension']
                                                    ret_ += "\nResolusi : "+koplok['resolution']
                                                    ret_ += "\nSize : "+koplok['size']
                                                    ret_ += "\nLink : "+koplok['url']
                                                    if koplok['resolution'] == '50k':
                                                        audio = koplok['url']
                                            cl.sendImageWithURL(msg.to,cover)
                                            cl.sendMessage(msg.to, str(ret_))
                                            cl.sendAudioWithURL(msg.to,audio)
                                        
                        elif cmd.startswith("post "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            post = msg.text.replace(sep[0] + " ","")
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("http://m.jancok.com/klik/{}/".format(urllib.parse.quote(post)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                ret_ = '「 Get Postingan 」\n\n'
                                try:
                                    for title in soup.select("[class~=badge-item-title]"):
                                        ret_ += "• Judul : "+title.get_text()
                                        ret_ += "\n• Link : m.jancok.com"
                                    for link in soup.find_all('img',limit=1):
                                        cl.sendMessage(msg.to, ret_)
                                        cl.sendImageWithURL(msg.to, link.get('src'))
                                except Exception as e:
                                    cl.sendMessage(msg.to, "Post kosong")
                                    print(str(e))
                                    
                        elif cmd.startswith("line "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            user = text.replace(sep[0] + " ","")
                            conn = cl.findContactsByUserid(user)
                            try:
                                anu = conn.mid
                                dn = conn.displayName
                                bio = conn.statusMessage
                                sendMention(to, anu, "「 Contact Line ID 」\n• Nama : ", "\n• Nick : "+dn+"\n• Bio : "+bio+"\n• Contact link : http://line.me/ti/p/~"+user)
                                cl.sendContact(to, anu)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("invite: "):
                          if msg._from in admin:
                               sep = text.split(" ")
                               idnya = text.replace(sep[0] + " ","")
                               conn = cl.findContactsByUserid(idnya)
                               cl.findAndAddContactsByMid(conn.mid)
                               cl.inviteIntoGroup(msg.to,[conn.mid])
                               group = cl.getGroup(msg.to)
                               xname = cl.getContact(conn.mid)
                               zx = ""
                               zxc = ""
                               zx2 = []
                               xpesan = '「 Sukses Diinvite 」\nNama contact '
                               recky = str(xname.displayName)
                               pesan = ''
                               pesan2 = pesan+"@a\n"
                               xlen = str(len(zxc)+len(xpesan))
                               xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                               zx = {'S':xlen, 'E':xlen2, 'M':xname.mid}
                               zx2.append(zx)
                               zxc += pesan2
                               text = xpesan+ zxc + "ke grup " + str(group.name) +""
                               cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

                        elif cmd.startswith("listmeme"):
                          if msg._from in admin:
                            proses = text.split(" ")
                            keyword = text.replace(proses[0] + " ","")
                            count = keyword.split("|")
                            search = str(count[0])
                            r = requests.get("http://api.imgflip.com/get_memes")
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                hasil = "「 Daftar Meme Image 」\n"
                                for aa in data["data"]["memes"]:
                                    no += 1
                                    hasil += "\n" + str(no) + ". "+ str(aa["name"])
                                hasil += " "
                                ret_ = "\n\nSelanjutnya ketik:\nListmeme | angka\nGet-meme text1 | text2 | angka"
                                cl.sendText(msg.to,hasil+ret_)
                            if len(count) == 2:
                                try:
                                    num = int(count[1])
                                    gambar = data["data"]["memes"][num - 1]
                                    hasil = "{}".format(str(gambar["name"]))
                                    sendMention(msg.to, msg._from,"「 Meme Image 」\nTunggu ","\nFoto sedang diproses...")
                                    cl.sendMessage(msg.to,hasil)
                                    cl.sendImageWithURL(msg.to,gambar["url"])
                                except Exception as e:
                                    cl.sendMessage(msg.to," "+str(e))
                                    
                        elif cmd.startswith("meme "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            keyword = text.replace(proses[0]+" ","")
                            query = keyword.split("|")
                            atas = query[0]
                            bawah = query[1]
                            r = requests.get("https://api.imgflip.com/get_memes")
                            data = json.loads(r.text)
                            try:
                                num = int(query[2])
                                namamem = data["data"]["memes"][num - 1]
                                meme = int(namamem["id"])
                                api = pyimgflip.Imgflip(username='andyihsan', password='ihsan848')
                                result = api.caption_image(meme, atas,bawah)
                                sendMention(msg.to, msg._from,"「 Meme Image 」\nTunggu ","\nFoto sedang diproses...")
                                cl.sendImageWithURL(msg.to,result["url"])
                            except Exception as e:
                                cl.sendMessage(msg.to," "+str(e))


                        elif cmd.startswith("get-gif "):
                          if msg._from in admin:
                            proses = text.split(" ")
                            urutan = text.replace(proses[0] + " ","")
                            count = urutan.split("|")
                            search = str(count[0])
                            r = requests.get("https://api.tenor.com/v1/search?key=PVS5D2UHR0EV&limit=10&q="+str(search))
                            data = json.loads(r.text)
                            if len(count) == 1:
                                no = 0
                                hasil = "「 Pencarian Gif 」\n"
                                for aa in data["results"]:
                                    no += 1
                                    hasil += "\n" + str(no) + ". " + str(aa["title"])
                                    ret_ = "\n\nSelanjutnya Get-gif {} | angka\nuntuk melihat detail video".format(str(search))
                                cl.sendMessage(msg.to,hasil+ret_)
                            elif len(count) == 2:
                                try:
                                    num = int(count[1])
                                    b = data["results"][num - 1]
                                    c = str(b["id"])
                                    hasil = "Informasi gif ID "+str(c)
                                    hasil += "\n"
                                    cl.sendMessage(msg.to,hasil)
                                    dl = str(b["media"][0]["loopedmp4"]["url"])
                                    cl.sendVideoWithURL(msg.to,dl)
                                except Exception as e:
                                    cl.sendMessage(msg.to," "+str(e))                        
                        
                        elif cmd.startswith("sholat "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「 Jadwal Sholat 」\n"
                                         ret_ += "\n║⊛  Lokasi : " + data[0]
                                         ret_ += "\n║⊛  " + data[1]
                                         ret_ += "\n║⊛  " + data[2]
                                         ret_ += "\n║⊛  " + data[3]
                                         ret_ += "\n║⊛  " + data[4]
                                         ret_ += "\n║⊛  " + data[5]
                                         ret_ += "\n\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                         ret_ += "\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「 Status Cuaca 」\n"
                                    ret_ += "\n「✭」 Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n「✭」 Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n「✭」 Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n「✭」 Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n「✭」 Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「 Info Lokasi 」"
                                    ret_ += "\n║⊛  Location : " + data[0]
                                    ret_ += "\n║⊛  Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik "):
                          if msg._from in admin:
                            data = msg.text.lower().replace("lirik ","")                                
                            artis = data.split('|')
                            artis = artis[1].replace(' ','_')
                            judul = data.split('|')
                            judul = judul[2].replace(' ','_')
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("https://www.wowkeren.com/lirik/lagu/{}/{}.html".format(urllib.parse.quote(artis), judul))
                                x = s.get("https://www.wowkeren.com/seleb/{}/lirik.html".format(urllib.parse.quote(artis)))
                                data = BeautifulSoup(r.content, 'html5lib')
                                data1 = BeautifulSoup(x.content, 'html5lib')
                                ret_ = ''
                                try:
                                    yyk = data1.select("[class~=content]")[1].text
                                    yoyok = yyk.replace("		", " ")
                                    ret_ += "  「 Informasi Penyanyi 」"+yoyok
                                    ret = data.find("div", id="JudulHalaman")
                                    ret_ += "Judul lagu : "+ret.get_text()
                                    ret_ += "\n\n  「 Lirik Lagunya 」"+data.select("[class~=GambarUtama]")[1].text
                                    for link in data1.findAll('div', attrs={'class':'item'}):
                                        cl.sendImageWithURL(msg.to, "https://www.wowkeren.com"+link.find('img')['src'])
                                    cl.sendMessage(to, ret_)
                                except:
                                    cl.sendMessage(to, "lirik tidak tersedia")

                        elif cmd.startswith("lirik "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   url = "http://rahandiapi.herokuapp.com/lyricapi?key=betakey&q={}".format(urllib.parse.quote(search))
                                   link = web.get(url)
                                   data = link.text
                                   data = json.loads(data)
                                   start = timeit.timeit()
                                   ret_ = "「 Lirik Search 」"
                                   ret_ += "\n║⊛  Judul : {}".format(str(data["title"]))
                                   ret_ += "\n║⊛  Time Taken : {}".format(str(start))
                                   ret_ += "\n\n{}".format(str(data["lyric"]))
                                   cl.sendText(msg.to, str(ret_))

                        elif cmd.startswith("musik: "):
                          if msg._from in admin:                        	
                            query = msg.text.replace("musik2:","")
                            search = query.replace(" ","+")
                            result = requests.get("https://api.zicor.ooo/joox.php?song={}".format(search))
                            data = result.text
                            data = json.loads(data)
                            ret_ = ">> Play Music <<"
                            ret_ += "\n- Judul : {}".format(data["title"])
                            ret_ += "\n- Artis : {}".format(data["singer"])
                            ret_ += "\n- Lirik :\n{}".format(data["lyric"])
                            cl.sendImageWithURL(to, data["image"])
                            #aditmadzs.sendMessage(msg_id, to, ret_)
                            cl.sendAudioWithURL(to, data["url"])

                        elif cmd.startswith("musik2: "):
                          if msg._from in admin:    
                            try:
                                dan = msg.text.replace("musik: ","")
                                r = requests.get("https://api.zicor.ooo/joox.php?song={}"+urllib.parse.quote(dan))
                                data = r.json()
                                l = data["lyric"].replace("ti:","Judul: ")
                                i = l.replace("ar:","Penyanyi: ")
                                r = i.replace("al:","Album: ")
                                ii = r.replace("[by:]","")
                                k = ii.replace("[offset:0]","")
                                lirik = k.replace("***Lirik didapat dari pihak ketiga***\n","")
                                cl.sendImageWithURL(msg.to, data["image"])
                                t = "[ Music ]"
                                t += "\n\nJudul: "+str(data["title"])
                                t+="\nPenyanyi: "+str(data["singer"])
                                t+="\n\n[ Finish ]\n\n"+str(lirik)
                                cl.sendMessage(msg.to, str(t))
                                cl.sendAudioWithURL(msg.to, data["url"])
                            except Exception as error:
                                pass

                        elif cmd.startswith("ytmp4"):
                                try:
                                    sep = text.split(" ")
                                    textToSearch = text.replace(sep[0]+" ","")
                                    query = urllib.parse.quote(textToSearch)
                                    search_url="https://www.youtube.com/results?search_query="
                                    mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                    sb_url = search_url + query
                                    sb_get = requests.get(sb_url, headers = mozhdr)
                                    soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                    yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                    x = (yt_links[1])
                                    yt_href =  x.get("href")
                                    yt_href = yt_href.replace("watch?v=", "")
                                    qx = "https://youtu.be" + str(yt_href)
                                    vid = pafy.new(qx)
                                    stream = vid.streams
                                    best = vid.getbest()
                                    best.resolution, best.extension
                                    for s in stream:
                                        me = best.url
                                        hasil = ""
                                        title = "Judul [ " + vid.title + " ]"
                                        author = '\n\nAuthor : ' + str(vid.author)
                                        durasi = '\nDuration : ' + str(vid.duration)
                                        suka = '\nLikes : ' + str(vid.likes)
                                        rating = '\nRating : ' + str(vid.rating)
                                        deskripsi = '\nDeskripsi : ' + str(vid.description)
                                    cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                                    cl.sendVideoWithURL(msg.to, me)         
                                except Exception as e:
                                    cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("mp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n🌠 Author : ' + str(vid.author)
                                    durasi = '\n🌠 Duration : ' + str(vid.duration)
                                    suka = '\n🌠 Likes : ' + str(vid.likes)
                                    rating = '\n🌠 Rating : ' + str(vid.rating)
                                    deskripsi = '\n🌠 Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("apk "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split("|")
                            search = str(cond[0])
                            with requests.session() as s:
                                s.headers['user-agent'] = random.choice(settings["userAgent"])
                                r = s.get("https://apkpure.com/id/search?q={}".format(str(search)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                data = soup.findAll('dl', attrs={'class':'search-dl'})
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "「 Pencarian Aplikasi 」\n"
                                    for apk in data:
                                        num += 1
                                        link = "https://apkpure.com"+apk.find('a')['href']
                                        title = apk.find('a')['title']
                                        ret_ += "\n {}. {}".format(str(num), str(title))
                                    ret_ += "\n\n Total {} Result".format(str(len(data)))
                                    ret = "Selanjutnya ketik:\nGet-apk {} | angka".format(str(search))
                                    cl.sendMessage(to, str(ret_))
                                    cl.sendMessage(to, str(ret))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data):
                                        apk = data[num - 1]
                                        with requests.session() as s:
                                            s.headers['user-agent'] = random.choice(settings["userAgent"])
                                            r = s.get("https://apkpure.com{}/download?from=details".format(str(apk.find('a')['href'])))
                                            soup = BeautifulSoup(r.content, 'html5lib')
                                            data = soup.findAll('div', attrs={'class':'fast-download-box'})
                                            for down in data:
                                                load = down.select("a[href*=https://download.apkpure.com/]")[0]
                                                file = load['href']
                                                ret_ = "File info :\n"+down.find('span', attrs={'class':'file'}).text
                                                with requests.session() as web:
                                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                                    r = web.get("https://api-ssl.bitly.com/v3/shorten?access_token=497e74afd44780116ed281ea35c7317285694bf1&longUrl={}".format(urllib.parse.quote(file)))
                                                    data = r.text
                                                    data = json.loads(data)
                                                    ret_ += "\nLink Download :\n"+data["data"]["url"]
                                                cl.sendMessage(to, str(ret_))

                        elif cmd.startswith("anime "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            anime = msg.text.replace(sep[0] + " ","%20")                
                            with requests.session() as web:
                                web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                            r = web.get("https://kitsu.io/api/edge/anime?filter[text]={}".format(urllib.parse.quote(anime)))
                            data = r.text
                            data = json.loads(data)
                            ret_ = ''
                            if data["data"] != []:
                                for a in data["data"]:
                                    if a["attributes"]["subtype"] == "TV":
                                        sin = a["attributes"]["synopsis"]
                                        translator = Translator()
                                        hasil = translator.translate(sin, dest='id')
                                        sinop = hasil.text
                                        ret_ += '「 Anime {} 」'.format(str(a["attributes"]["canonicalTitle"]))
                                        ret_ += '\n• Rilis : '+str(a["attributes"]["startDate"])
                                        ret_ += '\n• Rating : '+str(a["attributes"]["ratingRank"])
                                        ret_ += '\n• Type : '+str(a["attributes"]["subtype"])
                                        ret_ += '\n• Sinopsis :\n'+str(sinop)
                                        ret_ += '\n\n'
                                        cl.sendImageWithURL(msg.to, str(a["attributes"]["posterImage"]["small"]))
                            cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("zodiak "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            query = text.replace(sep[0] + " ","")
                            r = requests.post("https://aztro.herokuapp.com/?sign={}&day=today".format(urllib.parse.quote(query)))
                            data = r.text
                            data = json.loads(data)
                            data1 = data["description"]
                            data2 = data["color"]
                            translator = Translator()
                            hasil = translator.translate(data1, dest='id')
                            hasil1 = translator.translate(data2, dest='id')
                            A = hasil.text
                            B = hasil1.text
                            ret_ = "「 Ramalan zodiak {} hari ini 」\n".format(str(query))
                            ret_ += str(A)
                            ret_ += "\n======================\n• Tanggal : " +str(data["current_date"])
                            ret_ += "\n• Rasi bintang : "+query
                            ret_ += " ("+str(data["date_range"]+")")
                            ret_ += "\n• Pasangan Zodiak : " +str(data["compatibility"])
                            ret_ += "\n• Angka keberuntungan : " +str(data["lucky_number"])
                            ret_ += "\n• Waktu keberuntungan : " +str(data["lucky_time"])
                            ret_ += "\n• Warna kesukaan : " +str(B)
                            cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("bintang "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            url = msg.text.replace(sep[0] + " ","")    
                            with requests.session() as s:
                                s.headers['user-agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                r = s.get("https://www.vemale.com/zodiak/{}".format(urllib.parse.quote(url)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                ret_ = ""
                                for a in soup.select('div.vml-zodiak-detail'):
                                    ret_ += a.h1.string
                                    ret_ += "\n"+ a.h4.string
                                    ret_ += " : "+ a.span.string +""
                                for b in soup.select('div.col-center'):
                                    ret_ += "\nTanggal : "+ b.string
                                for d in soup.select('div.number-zodiak'):
                                    ret_ += "\nAngka keberuntungan : "+ d.string
                                for c in soup.select('div.paragraph-left'):
                                    ta = c.text
                                    tab = ta.replace("    ", "")
                                    tabs = tab.replace(".", ".\n")
                                    ret_ += "\n"+ tabs
                                    #print (ret_)
                                cl.sendMessage(msg.to, str(ret_))

                        elif text.lower() == 'top kaskus':
                           if msg._from in admin:
                               r = requests.get("https://api.bayyu.net/kaskus-hotthread/?apikey=c28c944199384f191335f1f8924414fa839350d&page=2")
                               data=r.text
                               data=json.loads(data)                                                                                                      
                               if data["hot_threads"] != []:
                                   no = 0
                                   hasil = "「 Kaskus Search 」\n"
                                   for news in data["hot_threads"]:
                                        no += 1                  
                                        hasil += "\n" + str(no) + ". Judul : " + str(news["title"]) + "\n • Deskripsi : " + str(news["detail"]) + "\n• Link: " + str(news["link"]) + "\n"
                                        hasil += "\n"
                                   cl.sendText(msg.to, str(hasil))

                        elif cmd.startswith("get-video "):
                          if msg._from in admin:
                                sep = msg.text.split(" ")
                                search = msg.text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                      web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                      url = web.get("http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(urllib.parse.quote(search)))
                                      data = url.text
                                      data = json.loads(data)
                                      if data["result"] != []:
                                          video = random.choice(data["result"]["videolist"])
                                          vid = video["url"]
                                          start = timeit.timeit()
                                          ret = "「 Informasi Video 」\n"
                                          ret += "• Judul : {}".format(str(data["result"]["title"]))
                                          ret += "\n• Author : {}".format(str(data["result"]["author"]))
                                          ret += "\n• Durasi : {}".format(str(data["result"]["duration"]))
                                          ret += "\n• Like nya : {}".format(str(data["result"]["likes"]))
                                          ret += "\n• Rating : {}".format(str(data["result"]["rating"]))
                                          ret += "\n• TimeTaken : {}".format(str(start))
                                          ret += "\n• Deskripsi : {}\n「 Waiting Encoding 」".format(str(data["result"]["description"]))
                                          cl.sendMessage(msg.to, str(ret))
                                          cl.sendVideoWithURL(msg.to, str(vid))

                        elif cmd.startswith("get-mp3 "):
                          if msg._from in admin:
                                sep = msg.text.split(" ")
                                search = msg.text.replace(sep[0] + " ","")
                                with requests.session() as web:
                                      web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                      url = web.get("http://rahandiapi.herokuapp.com/youtubeapi/search?key=betakey&q={}".format(urllib.parse.quote(search)))
                                      data = url.text
                                      data = json.loads(data)
                                      if data["result"] != []:
                                          audio = random.choice(data["result"]["audiolist"])
                                          aud = audio["url"]
                                          start = timeit.timeit()
                                          ret = "「 Informasi Mp3 」\n"
                                          ret += "• Judul : {}".format(str(data["result"]["title"]))
                                          ret += "\n• Author : {}".format(str(data["result"]["author"]))
                                          ret += "\n• Durasi : {}".format(str(data["result"]["duration"]))
                                          ret += "\n• Like nya : {}".format(str(data["result"]["likes"]))
                                          ret += "\n• Rating : {}".format(str(data["result"]["rating"]))
                                          ret += "\n• TimeTaken : {}".format(str(start))
                                          ret += "\n• Deskripsi : {}\n「 Waiting Encoding 」".format(str(data["result"]["description"]))
                                          cl.sendText(msg.to, str(ret))
                                          cl.sendAudioWithURL(msg.to, str(aud))

                        elif cmd.startswith("get-instagram "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['graphql']['user']['full_name'])
                                bioIG = str(data['graphql']['user']['biography'])
                                mediaIG = str(data['graphql']['user']['edge_owner_to_timeline_media']['count'])
                                verifIG = str(data['graphql']['user']['is_verified'])
                                usernameIG = str(data['graphql']['user']['username'])
                                followerIG = str(data['graphql']['user']['edge_followed_by']['count'])
                                profileIG = data['graphql']['user']['profile_pic_url_hd']
                                privateIG = str(data['graphql']['user']['is_private'])
                                followIG = str(data['graphql']['user']['edge_follow']['count'])
                                link = "• Link : " + "https://www.instagram.com/" + instagram
                                text = "「 Instagram User 」\n• Name : "+namaIG+"\n• Username : "+usernameIG+"\n• Follower : "+followerIG+"\n• Following : "+followIG+"\n• Total post : "+mediaIG+"\n• Verified : "+verifIG+"\n• Private : "+privateIG+"\n• Biography : "+bioIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("get-date "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"「 Date Info 」\n"+"「✭」 Date Of Birth : "+lahir+"\n「✭」 Age : "+usia+"\n「✭」 Ultah : "+ultah+"\n「✭」 Zodiak : "+zodiak)

                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 Clone Profile 」\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    cl.sendMessage(msg.to, "Gagal clone profile")
                            
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  lineProfile.displayName = str(myProfile["displayName"])
                                  lineProfile.statusMessage = str(myProfile["statusMessage"])
                                  lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                  cl.updateProfile(lineProfile)
                                  sendMention(msg.to, sender, "「 Restore Profile 」\nNama ", " \nBerhasil restore profile")
                              except:
                                  cl.sendMessage(msg.to, "Gagal restore profile")

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["AKlimit"] = num
                                cl.sendMessage(msg.to,"「 Status Spamtag 」\nBerhasil diubah jadi {} kali".format(str(strnum)))

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"「 Status Spamcall 」\nBerhasil diubah jadi {} kali".format(str(strnum)))

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["AKlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd.startswith("panggil "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(key1)
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendMessage(msg.to,str(e))

                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                cl.acquireGroupCallRoute(to)
                                cl.inviteIntoGroupCall(to, contactIds=members)
                                        
                        elif cmd.startswith("spamcall "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                proses = text.split(" ")
                                strnum = text.replace(proses[0] + " ","")
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jumlah = int(strnum)
                                cl.sendText(msg.to,"Undangan call grup {} sukses".format(str(strnum)))
                                if jumlah <= 1000:
                                   for x in range(jumlah):
                                   	try:
                                           cl.acquireGroupCallRoute(to)
                                           cl.inviteIntoGroupCall(to, contactIds=members)
                                   	except Exception as e:
                                          cl.sendMessage(msg.to,str(e))

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              cl.sendText(msg.to,"「 Spam Gift 」\nBerhasil spamgift {} kali".format(str(jumlah)))
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      
                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))

#=========== [ Add Image ] ============#
                        elif cmd.startswith("addimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                wait["Addimage"]["status"] = True
                                wait["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim fotonya...") 
                            else:
                                cl.sendText(msg.to, "Foto itu sudah dalam list") 
                                
                        elif cmd.startswith("dellimg "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                cl.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Foto itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listimage":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Image 」\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\nTotal「{}」Images".format(str(len(images)))
                             cl.sendText(to, ret_)
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addvideo "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in videos:
                                wait["Addvideo"]["status"] = True
                                wait["Addvideo"]["name"] = str(name.lower())
                                videos[str(name.lower())] = ""
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim videonya...") 
                            else:
                                cl.sendText(msg.to, "Video itu sudah dalam list") 
                                
                        elif cmd.startswith("dellvideo "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in videos:
                                cl.deleteFile(videos[str(name.lower())])
                                del videos[str(name.lower())]
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus video {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Video itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listvideo":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Video 」\n\n"
                             for video in videos:
                                 no += 1
                                 ret_ += str(no) + ". " + video.title() + "\n"
                             ret_ += "\nTotal「{}」Videos".format(str(len(videos)))
                             cl.sendText(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play video nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addmp3 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in audios:
                                wait["Addaudio"]["status"] = True
                                wait["Addaudio"]["name"] = str(name.lower())
                                audios[str(name.lower())] = ""
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim mp3 nya...") 
                            else:
                                cl.sendText(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in audios:
                                cl.deleteFile(audios[str(name.lower())])
                                del audios[str(name.lower())]
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                            else:
                                cl.sendText(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listmp3":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Lagu 」\n\n"
                             for audio in audios:
                                 no += 1
                                 ret_ += str(no) + ". " + audio.title() + "\n"
                             ret_ += "\nTotal「{}」Lagu".format(str(len(audios)))
                             cl.sendText(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play mp3 nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Sticker ] ============#                                            
                        elif cmd.startswith("addsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                wait["Addsticker"]["status"] = True
                                wait["Addsticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Silahkan kirim stickernya...") 
                            else:
                                cl.sendMessage(msg.to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "Sticker itu tidak ada dalam list") 
                                 
                        elif text.lower() == "liststicker":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Sticker 」\n\n"
                             for sticker in stickers:
                                 no += 1
                                 ret_ += str(no) + ". " + sticker.title() + "\n"
                             ret_ += "\nTotal「{}」Stickers".format(str(len(stickers)))
                             cl.sendMessage(to, ret_)
                             
#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Welcome 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Welcome 」\n" + msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Url 」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect kick 」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Join 」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Cancel 」\n" + msgs)

                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Invite 」\n" + msgs)

                        elif 'Protecall ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecall ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua sudah diaktifkan"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                      msgs += "\nSemua protection diaktifkan"
                                  cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                         msgs += "\nSemua protection dimatikan"
                                    cl.sendMessage(msg.to, "「 Status Protection 」\n" + msgs)

#===========KICKOUT============#
                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           cl.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Alka:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Alka:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus staff")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Alka:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus bot")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                sendMessage(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "admin:expell" or text.lower() == 'admin:expell':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                sendMessage(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                sendMessage(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "staff:expell" or text.lower() == 'staff:expell':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                sendMessage(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                sendMessage(msg.to, sender, "User ", " \nSelfbot direfresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = True
                                sendMention(msg.to, sender, "「 Status Unsend 」\nUser ", "\nSilahkan unsend pesannya,\nKetik unsend off jika sudah slesai")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = False
                                sendMention(msg.to, sender, "「 Status Unsend 」\nUser ", " \nDeteksi unsend dinonaktifkan")

                        elif cmd == "simisimi on" or text.lower() == 'simisimi on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["simiSimi"] = True
                                sendMessage(msg.to, sender, "「 Status Simi-Simi 」\nUser ", "\nDeteksi Simi-Simi di Aktifkan,\nKetik Simisimi off jika sudah slesai")

                        elif cmd == "simisimi off" or text.lower() == 'simisimi off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["simiSimi"] = False
                                sendMessage(msg.to, sender, "「 Status Simi-Simi 」\nUser ", " \nDeteksi Simi-Simi dinonaktifkan")
                                
                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                sendMention(msg.to, sender, "「 Status Timeline 」\nUser ", "\nSilahkan kirim postingannya,\nKetik timeline off jika sudah slesai")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                sendMention(msg.to, sender, "「 Status Timeline 」\nUser ", " \nDeteksi timeline dinonaktifkan")

                        elif cmd == "autolike on" or text.lower() == 'autolike on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autolike"] = True
                                sendMessage(msg.to, sender, "「 Status Auto Like 」\nUser ", "\nSilahkan kirim postingannya,\nKetik Autolike off jika sudah slesai")

                        elif cmd == "autolike off" or text.lower() == 'autolike off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autolike"] = False
                                sendMessage(msg.to, sender, "「 Status Auto Like 」\nUser ", " \nDeteksi Auto Like dinonaktifkan")
                                
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendMessage(msg.to, sender, "「 Status Invite 」\nUser ", "\nSilahkan kirim kontaknya,\nKetik invite off jika sudah slesai")

                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendMessage(msg.to, sender, "「 Status Invite 」\nUser ", " \nInvite via contact dinonaktifkan")
                                
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["mentionKick"] = True
                                cl.sendMessage(msg.to,"「 Status Notag 」\nNotag telah diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["mentionKick"] = False
                                cl.sendMessage(msg.to,"「 Status Notag 」\nNotag telah dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sendMessage(msg.to, sender, "「 Status Contact 」\nUser ", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik contact off")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"「 Status Contact 」\nDeteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"「 Status Respon 」\nAuto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"「 Status Respon 」\nAuto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"「 Status Autojoin 」\nAutojoin telah diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"「 Status Autojoin 」\nAutojoin telah dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"「 Status Autoleave 」\nAutoleave telah diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"「 Status Autoleave 」\nAutoleave telah dinonaktifkan")

                        elif cmd == "autoblock on" or text.lower() == 'autoblock on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = True
                                cl.sendText(msg.to,"「 Status Autoleave 」\nAutoleave telah diaktifkan")

                        elif cmd == "autoblock off" or text.lower() == 'autoblock off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoBlock"] = False
                                cl.sendMention(msg.to,"「 Status Autoleave 」\nAutoleave telah dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"「 Status Autoadd 」\nAutoadd telah diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"「 Status Autoadd 」\nAutoadd telah dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["stickerOn"] = True
                                sendMessage(msg.to, sender, "「 Status Sticker Check 」\n", " [ ON ]\nSilahkan kirim stickernya,\nJika sudah selesai, ketik sticker off")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["stickerOn"] = False
                                cl.sendMessage(msg.to,"「 Status Sticker Check 」\nSticker check dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sendMessage(msg.to, sender, "「 Status Jointicket 」\nUser ", "\nSilahkan kirim link grupnya,\nJika sudah selesai, ketik jointicket off")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"「 Status Jointicket 」\nJointicket telah dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan talkban")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus talkban")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                sendMessage(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                sendMessage(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                sendMessage(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                sendMessage(msg.to, sender, "", "\nSilahkan kirim kontaknya,\nJika sudah selesai, ketik refresh")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"「 Huray not blacklist 」")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 Daftar Blacklist 」\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"「 Daftar Talkban 」\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                  wait["blacklist"] = {}
                                  ragets = cl.getContact(wait["blacklist"])
                                  mc = "「%i」User Blacklist" % len(ragets)
                                  cl.sendMessage(msg.to,"Berhasil dihapus\n" +mc)                         
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nPesan Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set comment: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set comment: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti comment Msg")
                              else:
                                  wait["comment"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nComment Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nWelcome Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Leave Msg")
                              else:
                                  wait["leave"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nLeave Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nRespon Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["AKmessage1"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nSpam Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「 Berhasil Diganti 」\nSider Msg diganti jadi :\n\n{}".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Message 」\nPesan Msg mu :\n\n" + str(wait["message"]))

                        elif text.lower() == "cek comment":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Message 」\nComment Msg mu :\n\n" + str(wait["comment"]))

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Welcome 」\nWelcome Msg mu :\n\n" + str(wait["welcome"]))

                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Leave 」\nLeave Msg mu :\n\n" + str(wait["leave"]))

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Respon 」\nRespon Msg mu :\n\n" + str(wait["Respontag"]))

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Spam 」\nSpam Msg mu :\n\n" + str(Setmain["RAmessage1"]))

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「 Status Sider 」\nSider Msg mu :\n\n" + str(wait["mention"]))

    except Exception as error:
        print (error)


while True:
  try:
      Ops = cl.poll.fetchOperations(cl.revision, 50)
      for op in Ops:
        if op.type != 0:
          cl.revision = max(cl.revision, op.revision)
          bot(op)
  except Exception as E:
    E = str(E)
    if "reason=None" in E:
      print (E)
      time.sleep(60)
      restart_program()
