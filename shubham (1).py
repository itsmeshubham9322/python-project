


practice_id=[1,2,3,4,5]
Date=["1-7-2024","2-7-2024","3-7-2024","4-7-2024","5-7-2024"]
Instrument=["Guitar","violin","flute","Drum","Banjo"]
Duration=[1.00,2.00,2.45,1.30,3.00]
pieces_practice=["A","B","C","D","E"]

def addmusic():
    m_practice_id = int(input("Enter The practice_Id:"))
    m_Date = input("Enter THE DATE:")
    m_Instrument = input("Enter THE Instrument:")
    m_Duration= float(input("enter duration:"))
    m_pieces_practice = input("Enter THE PIECES_PRATICES:")

    practice_id.append(m_practice_id)
    Date.append(m_Date)
    Instrument.append(m_Instrument)
    Duration.append(m_Duration)
    pieces_practice.append(m_pieces_practice)

def deletemusic():
    delete = int(input("Enter The practice_Id to delete ::"))
    for i in range(len(practice_id)):
        if(delete==practice_id[i]):
            practice_id.remove(practice_id[i])
            Date.remove(Date[i])
            Instrument.remove(Instrument[i])
            Duration.remove(Duration[i])
            pieces_practice.remove(pieces_practice[i])
            break

def viewmusic():
    print("practice_ID \t Date \t\t\t\t Instrument \t\t\tDuration \t pieces_practice")
    for i in range(len(practice_id)):
     print(practice_id[i], "\t""\t" ,Date[i], "\t""\t""\t""\t" ,Instrument[i], "\t""\t""\t""\t" ,Duration[i], "\t""\t" ,pieces_practice[i])

def Updatemusic():
    uid=int(input("Enter practice_id to update:"))
    for i in range(len(practice_id)):
        if(uid==practice_id[i]):
            up_practice_id = int(input("Enter New  practice_id::"))
            up_Date = input("Enter The New date:")
            up_Instrument = input("Enter New duration:")
            up_pieces_practice = input("Enter New pieces_practices:")
        
            practice_id[i]=up_practice_id
            Date[i] =up_Date
            Duration[i]=up_Instrument
            pieces_practice[i]=up_pieces_practice
            
def totalpractice():
    total = 0.0
    for i in range(len(practice_id)):
        total += float(Duration[i])
    return total

def reportinstrument():
    for i in range(len(practice_id)):
        print("",Instrument[i])

def averagepracticesession():
    a = totalpractice()
    average = a / len(practice_id)
    print("average practice session  = ",average)

count = 3
while(count!=0):
    username = input("enter the username:")
    password = input("enter the password:")
    if(username=="shubham" and password=="1234"):
        print("login successfully !")
        cnt  = 1
        while(cnt!=0):
            print(" 1.add music data \n 2.view  \n 3.update music data \n 4.remove data \n 5.Total practice in week \n 6.Report of practices by instrument \n 7.Average of practice session")
            ch = int(input("enter the your choice ="))
            if(ch==1):
                print("music data")
                addmusic()
            if(ch==2):
                print("View")
                viewmusic()
                
            if(ch==3):
                print("update")
                Updatemusic()
            if(ch==4):
                print("delete*")
                deletemusic()
            if(ch==5):
                print("Total practice in week")
                print("",totalpractice())
            if(ch==6):
                print("report of practices by instrument")
                reportinstrument()
            if(ch==7):
                print("average of practice session") 
                averagepracticesession()
            if(ch==8):       
                cnt  = 0
            
        cnt-=1
        count=1

    elif(username!="shubham" and password!="1234"):
        print("both id and pass incorrect !")
    elif(username!="shubham"):
        print("username incorrect !")
    elif(password!="1234"):
        print("passwors incorrect !")

    count -=1



