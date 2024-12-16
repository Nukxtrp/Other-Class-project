import os   
import socket
import time
import asyncio
import sqlite3 
from clientlist import client_list

ack = "<|ACK|>"
err = "<|ERR|>"

def clear():
    os.system('cls')

clear

connection = sqlite3.connect('Users.db')

async def main(connection):
    CorrectUser = False
    clear()
    print('------------------ Welcome to the Chat server ------------------')
    Login = input('Would you like to log in or sign up: ')
    clear()
    Login = Login.lower()
    if Login == 'sign up':
        Username = input('Please enter a username: ')
        Password = input('Please enter a password: ')
        q= f'''INSERT INTO ServerStart (Username, Password) VALUES ("{Username}","{Password}") RETURNING UID'''
        cursor = connection.cursor()
        cursor.execute(q)
        cursor.fetchall()
        connection.commit()
    elif Login == 'login':
        Username = input('Please enter a username: ')
        Password = input('Please enter a password: ')
        q = f'''SELECT Username FROM ServerStart Where "{Username}" = Username'''
        cursor = connection.cursor()
        cursor.execute(q)
        cursor.fetchall()
        connection.commit()
        CorrectUser = True
        s = socket.socket()
        print('Your socket was created successfully')
        time.sleep(2)
        clear()
        port = 19427
        s.bind(('127.0.0.1',port))
        print('Socket is bound to %s' %(port))
        time.sleep(2)
        clear()
        s.listen(50)
        print('Socket is listening')
        s.setblocking(False)
        clients = client_list()

        loop = asyncio.get_event_loop()

        while True:
            client, _ = await loop.sock_accept(s)


if __name__ == '__main__':
    asyncio.run(main(connection))