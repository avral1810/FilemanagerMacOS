import getpass
import os
import operator
Userslist={}
import shutil
root=os.getcwd()


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


def login():
    uid=raw_input('UID : '.center(180))
    if uid== 'admin':
        pswd=getpass.getpass('PASSWORD : '.center(180))
        if pswd==Userslist[uid]:
            adminpanel(uid)
            main()
        else:
            main()
    trying=0
    if uid in Userslist:
        while trying<3:
            pswd=getpass.getpass('PASSWORD : '.center(180))
            if Userslist[uid]==pswd:
                os.chdir("./." + uid)
                print("\n"*100)
                trying=10
                userpanel(uid)
            else:
                print("INCORRECT PASSWORD \n \a Try Again (max 3 times)")
                trying=trying+1
    else:
        print("\a user not found ")

def adminpanel(uid):
    string2='admin$ : '
    while True:
        print 'FileX $admin$'.center(180)
        command=raw_input(string2)
        if command == 'seeas':
            user=raw_input('User? ')
            if user in Userslist.keys():
                list_files('/Users/Aviral/Desktop/Python/FileX/.' + user)
        elif command=='viewall':
            for i in Userslist.keys():
                print i
            print("\n"*3)
        elif command=='deleteuser':
            user=raw_input('User? ')
            if user in Userslist.keys():
                suicide(user)
            else:
                print "No such user"
        elif command=='exit' or command == 'quit':
            main()
        elif command== 'cls' or command == 'clear':
            print("\n"*100)
        else:
            print("No such command")
                    



def suicide(user):
    shutil.rmtree('/Users/Aviral/Desktop/Python/FileX/.' + user)
    del Userslist[user]
    refresh=open('/Users/Aviral/Desktop/Python/FileX/.datafile.txt','w')
    refresh.close()
    for i in Userslist.keys():
        refresh=open('/Users/Aviral/Desktop/Python/FileX/.datafile.txt','a')
        refresh.write(i + ':' + Userslist[i] + '\n')
        refresh.close()

def userpanel(UID):
    string="LOGGED IN AS " + UID
    print(string.center(180))
    print("\n"*3)
    while True:
        print(string.center(180))
        print("\n" + os.getcwd().center(180) + "\n")
        string2="\n" + UID + " : "
        command=raw_input(string2)

        if command=='mkdir':
            string2="\n" + UID + " ~  mkdir ~  : "
            dirname=raw_input(string2)
            dirname='.' + dirname
            try:
                os.mkdir(dirname)
            except:
                print("Error")
            string2=dirname

        elif command == 'cd' or command == 'chdir':
            string2="\n" + UID + " ~  chdir ~  : "
            dirname=raw_input(string2)
            if dirname == '.' or dirname == '..':
                pass
            else:
                dirname='.'+dirname
            checker='/Users/Aviral/Desktop/Python/FileX/.' + UID
            if os.getcwd() == checker and dirname == '..':
                print("Error moving up")
            else:
                try:
                    os.chdir(dirname)
                except:
                    print("No such directory")
            string2=dirname

        elif command== 'delete' or command== 'remove'  or command == 'dlt' or command == 'rmdir':
            string2="\n" + UID + " ~  rmdir ~  : "
            dirname=raw_input(string2)
            dirname='.' + dirname
            try:
                shutil.rmtree(dirname)
            except:
                print "Error"
            string2=dirname
 
        elif command== 'exit' or command== 'quit':
            string2=''
            print("\n"*100)
            historyfile=open('/Users/Aviral/Desktop/Python/FileX/.' + UID + '/.history.txt' , 'a')
            historyfile.write(command + " : " + string2 + "\n")
            historyfile.close()
            main()

        elif command == 'man' or command == 'help':
            string2=''
            helpfile=open('/Users/Aviral/Desktop/Python/FileX/helpp.txt')
            for eachl in helpfile:
                print(eachl)

        elif command == 'ls' or command== 'list':
            string2=os.getcwd()
            poo=os.listdir(string2)
            for i in poo:
                print i

        elif command == 'history':
            string2=''
            historyfile=open('/Users/Aviral/Desktop/Python/FileX/.' + UID + '/.history.txt')
            for e in historyfile:
                print(e)

        elif command=='clear' or command=='cls':
            string2=''
            print("\n"*100)

        elif command=='copy':
            source=raw_input('Enter source file location: ')
            string2=source
            shutil.copy(source,os.getcwd())
        
        elif command=='move':
            source=raw_input('Enter source file location: ')
            string2=source
            shutil.move(source,os.getcwd())
            string2=source

        elif command=='make':
            string2="\n" + UID + " ~  make ~  : "
            dirname=raw_input(string2)
            dirname=dirname
            filee=open(dirname,'a')
            filee.close()
            filee=open(dirname)
            for a in filee:
               print(a)
            filee.close()
            while True:
                val=raw_input()
                if val == '~:wq':
                    print("WRITTEN")
                    break
                filee=open(dirname,'a')
                filee.write(val)
                filee.close()
            string2=dirname
        elif command == 'cat':
            string2="\n" + UID + " ~  cat ~  : "
            dirname=raw_input(string2)
            filee=open(dirname)
            for a in filee:
               print(a)
            filee.close()
 
        elif command=='xray':
            list_files(os.getcwd())
        elif command=='suicide' or command=='killme':
            sure=raw_input('Are you sure? ')
            sure=sure.lower()
            if sure == 'yes' or sure =='y':
                suicide(UID)
                main()

        else:
            print ("No such command" + "\nEnter 'help' or 'man' for instructions ")
            command=''
            string2=''

        historyfile=open('/Users/Aviral/Desktop/Python/FileX/.' + UID + '/.history.txt' , 'a')
        historyfile.write(command + " : " + string2 + "\n")
        historyfile.close()
        

def createuser():
    while True:
        uid=raw_input("Enter UID : ")
        if uid.isalpha() :
            pass
        else:
             exit()
        if uid not in Userslist.keys():
            break
        else:
            print "User exists, Try with different name\n"
    while True:
        pswd=getpass.getpass("Enter password : ")
        recheck=getpass.getpass("Enter it again : ")
        if pswd==recheck:
            break
        else:
            print "Passwords do not match, enter again\n"
    DataFile=open('.datafile.txt', 'a')
    DataFile.write(str(uid) + ':' + str(pswd))
    DataFile.write('\n')
    DataFile.close()
    Userslist.update({uid:pswd})
    os.mkdir('.'+uid)
    historyfile=open('/Users/Aviral/Desktop/Python/FileX/.' + uid + '/.history.txt' , 'a')
    historyfile.close()
    print("\n"*100)

def displayoptions():
    while True:
        print('1 signup'.center(180))
        print("\n")
        print('2 Login'.center(180))
        print("\n")
        print('3 Exit'.center(180))
        print("\n" * 2)
        ch=int(raw_input('? : '))
        if ch==1:
            createuser()
        elif ch==2:
            login()
        else:
            exit() 
def main():
    try:
        os.chdir('/Users/Aviral/Desktop/Python/FileX')
        root=os.getcwd()
    except:
        print("CANNOT CHANGE DIRECTORY")
        exit()
    datafile=open('.datafile.txt', 'a')
    datafile.close()
    Datafile=open('.datafile.txt')
    for eachline in Datafile:
        (uid,pswd)=eachline.split(':',1)
        pswd=pswd[:-1]
        Userslist.update({uid:pswd})
    Datafile.close()
    print("\n"*75)
    displayoptions()


main()
