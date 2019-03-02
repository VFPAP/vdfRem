#!/usr/bin/python3

import socket,sys

print ("""
Author: Vasco Pinto


          Power = 233


        0 = 48    5 = 53
        1 = 49    6 = 54
        2 = 50    7 = 55
        3 = 51    8 = 56
        4 = 52    9 = 57



           ArrUp = 38

ArrLf = 37  Ok = 13  ArrRg = 39

           ArrDw = 40



           Pl/Ps = 19



    VolUp = 175    PrgUp = 33
    VolDw = 174    PrgDw = 34

    Mute  = 173
""")

if len(sys.argv) is 2 or len(sys.argv) > 3:
    print("\nUsage: %s host port\n" %(str(sys.argv[0])))
    raise Exception("Invalid arguments")

if len(sys.argv) is 1:
    host = str(input("Host: "))
    port = int(input("Port: "))

if len(sys.argv) is 3:
    host = str(sys.argv[1])
    port = int(sys.argv[2])

try:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    response = s.recv(1024)

    if "hello" in response.decode('utf-8'):
        print("Connected to %s:%d\n" %(host,port))

        while True:

            key = input("Key: ")
            key = "key="+key+"\n"
            encKey = key.encode('utf-8')


            #print("Encoded: " + str(encKey))
            #print("Decoded: " + encKey.decode('utf-8'))

            s.send(encKey)

            response = s.recv(1024)

            if "ok" in response.decode('utf-8'):
                print("Command sent\n")

            if "ok" not in response.decode('utf-8'):
                print("Command sent but server never said \"ok\"...\nServer said: " + response.decode('utf-8'))

    else:
        print("Server never said \"hello\"...\nServer said: " + response.decode('utf-8'))
        raise Exception("Couldn't connect...")
except:
    print("\n\nExiting...")
    s.close()