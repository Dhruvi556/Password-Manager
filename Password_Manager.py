import os.path
from os import path
import random

def menu():                                                                                                              #Menu to choose operations
    while True:
        print("\nChoose operation number\n")
        print("1. Store username - password")
        print("2. Retrieve password")
        print("3. Delete file")
        print("4. Exit")
        choice = int(input("\nChoice: "))                                                           
        print()
        if choice == 1:
            site = input("Enter site: ")
            usn = input("Username: ")
            while True:
                pas1 = input("Password (min. length 8): ")
                if len(pas1) >= 8:
                    break
            while True:
                pwConf = input("Confirm password: ")                                                
                if pas1 == pwConf:          
                    ROT = random.randint(1,5)                                                       
                    L = [chr(ord(i) + ROT) if i.isdigit() != True else i for i in pas1]                                 #L stores the letter obtained after ROT is performed on the current letter or the symbol itself if it is a digit or extra character
                    V = len(L) - 4
                    M = ["R"] + ["O"] + ["T"] + [ROT]
                    for i in range(V):
                        M.append(str(random.randint(1,9)))
                        FINAL = ""
                    for i in range(len(L)):
                        FINAL = FINAL + str(L[i]) + str(M[i])                                                           #FINAL stores the encrypted password.
                    with open(site + ".txt","w") as f:
                        msite = f.write(site)
                        n = f.write('\n')
                        mid = f.write(usn)
                        n1 = f.write('\n')
                        mpass = f.write(FINAL)                                                                          #Account details are written in file.
                    print("Account added successfully!!")
                    break
                else:
                    print("Passwords don't match.")
            
        if choice == 2:                                                                                                 #Account details of the input site are displayed
            site = input("Enter site: ")
            print()
            if path.exists(site + ".txt"):
                with open(site + ".txt") as fp:
                    for i, line in enumerate(fp):
                        if(i%2 !=0):
                            print("Username: ",line)
                        elif(i%2 == 0 and i!=0):
                            KEY = line[7]
                            L = "".join([chr(ord(i) - int(KEY)) if i.isdigit() != True else i for i in line])[::2]      #Decrypt Password
                            print("Password: ",L)
                            
            else:
                print("Account of site doesn't exist.")
        if choice == 3:
            site = input("\nEnter which details are to be deleted: ")                                                   #Enter the site whose account details are to be deleted.
            print()
            if path.exists(site + ".txt"):
                os.remove(site + ".txt")                                                                                
                print("Account details deleted successfully! ")
            else:
                print("Account of site doesn't exist.") 
        if choice == 4:                                                                                                 #Exit Password Manager
            print("Thank you for using Password Manager©. Developed by Dhruvi Bharatbhai Patel.")
            break
            

print("Welcome to DB Password Manager©. Developed by Dhruvi Bharatbhai Patel.\n")
if path.exists("master.txt"):
    print("You need to login using Master credentials")                                                                 #Login into master account 
    masterun = input("Username : ")
    while True:
        masterpw = input("Password (min. length 8): ")
        if len(masterpw) >= 8:
            break
    
    with open("master.txt") as fp:                                                                                      
        for i, line in enumerate(fp):
            if i == 0:
                chkU = line
            elif i == 1:
                KEY = line[7]
                L = "".join([chr(ord(i) - int(KEY)) if i.isdigit() != True else i for i in line])[::2]                  #master account password is encrypted and stored in the master file
                chkP = L

    if chkU == masterun + '\n' and chkP == masterpw:                                                                    #Verify details of master account entered by the user                                                                    
        menu()                                                                                                          #If the master account details are correct, menu is displayed
    else:
        print("Wrong")

else:
    print("You need to create Master Account")                                                                          #Creating a master account
    masterun = input("Username : ")
    while True:
        masterpw1 = input("Password (min. length 8): ")
        if len(masterpw1) >= 8:
            ROT = random.randint(1,5)
            L = [chr(ord(i) + ROT) if i.isdigit() != True else i for i in masterpw1]                                    #Master password is encrypted and stored
            V = len(L) - 4
            M = ["R"] + ["O"] + ["T"] + [ROT]
            for i in range(V):
                M.append(str(random.randint(1,9)))
                masterpw = ""
            for i in range(len(L)):
                masterpw = masterpw + str(L[i]) + str(M[i])
            break
    

    while True:
        pwConf = input("Confirm password: ")                                                                            
        if masterpw1 == pwConf:
            with open("master.txt","a") as f:
                mid = f.write(masterun)
                n = f.write('\n')
                mpass = f.write(masterpw)
            print("\nMaster Account created successfully. Run again to login.\n")    
            break
        else:
            print("\nPasswords don't match.\n")
            


    
        
    
    
    
    
