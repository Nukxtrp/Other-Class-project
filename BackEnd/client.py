import socket
import threading
import time
import os
import sqlite3

ack = "<|ACK|>"
err = "<|ERR|>"

def clear():
    os.system('cls')

def login():
    logged_in = False
    s.sendall("1".encode())
    while (not logged_in):
        username = input('What is your username: ')
        s.sendall(username.encode())
        password = input('What is your password?: ')
        s.sendall(password.encode())
        response = s.recv(1024)
        if response.decode() == ack:
            logged_in = True
        else:
            print('Sorry either the username or the password are incorrect')

def signup():
    s.sendall("2".encode())
    username = input('What would you like your username to be?: ')
    s.sendall(username.encode())
    response = s.recv(1024)
    while response.decode() == err:
        username = input('Your username was invalid please try again: ')
        s.sendall(username.encode())
        response = s.recv(1024)
    
    Password = input('What would you like your password to be?: ')
    s.sendall(Password.encode())



s = socket.socket()


ip = '127.0.0.1'
port = 19427          

try:
    s.connect((ip, port))
    print(f"Connected to {ip}:{port}")
    clear()

    while(True):
        choice = input("Please choose\n1: login\n2: sign up\n:")
        if choice == '1' or choice == 'log in':
            login()
            break
        elif choice == '2' or choice == 'sign up':
            signup()
            break
        else:
            print('Sorry that input is invalid')
            

except ConnectionRefusedError:
    print("Server is not running or unreachable. Make sure the server is up and running.")
    
finally:
    s.close()
    