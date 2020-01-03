import time
import socket
import logging
import sys
from emoji import emojize


ch=input("Enter streamer name ")
server = 'irc.chat.twitch.tv'
port = 80
tok=input("Enter token from https://twitchapps.com/tmi/ ")
nickname = input("Enter your twitch username ")
token = 'oauth:'+tok
channel = '#'+ch



sock=socket.socket()


sock.connect((server,port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))


cur=int(time.time())
print("Wait for 2 seconds to dump data")
print("Showing live chat for \t "+ch+"\n")
while(True):
    s = sock.recv(2048).decode('utf-8')
    if(int(time.time())>=cur+2):
        user_index=mesg_index=0
        for i in range(len(s)):
            if(s[i]=='!'):
                user_index=i
                break
        temp="PRIVMSG"
        j=0
        for i in range(len(s)):
            if(j==len(temp)-1):
                mesg_index=i+1+len(channel)+3
                break
            if(s[i]==temp[j]):
                j+=1
            elif(j>0):
                j-=1
        user=msg=""
        for i in range(1,user_index):
            user+=s[i]
        for i in range(mesg_index,len(s)):
            msg+=s[i]
        print(user+"\t-\t"+emojize(msg,use_aliases=True)+"\n")
        
    
    if s.startswith('PING'):
        sock.send("PONG\n".encode('utf-8'))






