import os
from posixpath import pardir
import uuid
import platform
import subprocess
import time
import psutil 

user_input='''
Press 1 to Check current time and Date :- 
Press 2 to Check RAM Size of Your current OS  :- 
Press 3 to KNow Name of YOur current OS :- 
Press 4 to Check What is MAc Address of YOur lapTOP/PC/VM/CLoudVM :- 
Press 5 to create one directory IN your Desktop :- 
Press 6 to Restart Your current OS :- 
Press 7 to Print list of all available Wifi in your laptop Range :-
Press 8 to RUn another code in Your current folder  :-  
Press 9 to exit the programe :- 
'''


while True: 
    print(user_input)
    # to accept input from user 
    user_choice=input()
    # printing user input 
    #print("user has entered ",user_choice)


    if  user_choice ==  '1' :
        mytime=time.ctime()
        print("current date and time IS ",mytime)

    elif  user_choice  ==  '2' :
        print('RAM memory % used:', psutil.virtual_memory()[2] )
        
    elif  user_choice  ==  '3' : 
        os_name=platform.system()
        print(os_name)

    elif  user_choice  ==  '4' :
         print ("The MAC address in formatted way is : ", end="")
         print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
         for ele in range(0,8*6,8)][::-1])) 
    
    elif  user_choice  ==  '5' :
        directory=input("enter name of the directory :-")
        pardir= "C:\\Users\\joshu\\OneDrive\\Desktop"       
        path =os.path.join(pardir,directory)
        os.mkdir(path) 
        print("Directory created")
    
    elif  user_choice  ==  '6' :
        rs = input("Do you want to restart your PC ? (y / n): ")
        if rs == 'n':
                break
        else:
             os.system("shutdown /r /t 1")

    elif  user_choice  ==  '7' :
        devices = subprocess.check_output(['netsh','wlan','show','network'])
        devices = devices.decode('ascii')
        devices= devices.replace("\r","")
        print("Divices that  at the range ")
        print("_____________________________")
        print(devices)
    
    elif  user_choice  ==  '8' :
       print(subprocess.getoutput('task1.py'))
    
    elif  user_choice  ==  '9' :
        exit()

    else :
        print("opps! pressed a wrong key... try again")