#PART 2 STAFF VIEW

import mysql.connector as mys
from datetime import date
from datetime import datetime
today=date.today()
import sys

con=mys.connect(host='localhost',username='root',password='guru',charset='utf8')
cur=con.cursor()
cur.execute("create database if not exists customer")
cur.execute("use customer")
print("Database created")
cur.execute("create table if not exists restaurant(Roomno int, Foodprice int)")
cur.execute("create table if not exists details(Roomno int,Name char(25),DOB char(15),Age int,Gender char(1),Country char(15),State char(15),Address char(70),Phone char(11),Email char(25))")
cur.execute("create table if not exists regis(Roomno int,Name char(25),Type char(8),Size char(8),Indate char(11),Outdate char(30),Numroom int,Numppl int,Stay int)")
print("Tables created")
d=m=y=0

print("Welcome to Harine hotel")
#ADDING DEFAULT VALUES TO REGIS,DETAILS,FOOD TABLES
cur.execute("insert ignore into details values(1001,'Nara','03/10/1995',25,'F','India','Kerala','Thiru','9287656172','nv@gmail.com')")
cur.execute("insert ignore into details values(1002,'Smriti','12/10/2000',20,'F','Uae','Dubai','jahh','8889263525','smr@yahoo.com')")
cur.execute("insert ignore into details values(1003,'Sankee','05/12/1996',25,'F','Sg','Coln','Riva','7365526472','sank@hotmail.com')")

cur.execute("insert ignore into regis values(1001,'Nara','Deluxe','Triple','07/11/2020','30/11/2020',1,1,13)")
cur.execute("insert ignore into regis values(1002,'Smriti','Super','Pair','08/11/2020','27/11/2020',1,2,11)")
cur.execute("insert ignore into regis values(1003,'Sankee','Luxury','Single','18/11/2020','18/11/2020',3,3,1)")

cur.execute("insert ignore into restaurant values(1001,800)")
cur.execute("insert ignore into restaurant values(1002,2500)")
cur.execute("insert ignore into restaurant values(1003,2000)")


#PASSWORD TO ENTER INTO STAFF VIEW
cho=int(input("\n1: Admin\n2: Staff\n3: Customer\nEnter choice: "))
if cho==2:
    pwd=input("Enter Staff password: ")
    for i in range(3):   
        if pwd!="rootstaff":
            pwd=input("Wrong password, try again: ")
            if i==2:
                print("Attempt failed. Run application again.")
                sys.exit()

#STAFF VIEW'S MAIN MENU
def mainmenu():
    print("\nMain menu")
    amenu=input("1: Add new customer \n2: Display customer details\n3: Update 1 customer detail\
    \n4: Add restaurant items\n5: Delete 1 customer detail\n6: Generate Bill\n7: Exit\nEnter choice: ")
    
    while ((amenu not in "123456") or (len(str(amenu))!=1)):
        amenu=input("Enter valid menu option: ")
    else:
        if amenu=="1":
            add()
        if amenu=="2":
            display()  
        if amenu=="3":
            update()
        if amenu=="4":
            food()
        if amenu=="5":
            bill()
        if amenu=="6":
            delete()   
        if amenu=="7":
            sys.exit()    

#MENU ITEM 1: ADD NEW CUSTOMER
def add():
    cho=0
    itr=0
    while itr==0:
             print("Enter details below for new New Customer: ")
             try:
               cur.execute("select Roomno from details ORDER BY Roomno DESC LIMIT 1")
               x=cur.fetchall()
               w=x[0][0]
               emp=w+1
               print("This is your room number: ",emp)
               Roomno=emp
               print()               
             except IndexError:
               emp=1004
               print("This is your room number: ",emp)
               Roomno=1004
               x=""              
            #---------------------------------------------------------------------------------------   
             Cname=input("Enter name(First Last): ")
             while Cname=="":
                Cname=input("Blank entered. Enter valid name: ")
             while Cname.isdigit()==True:
                Cname=input("Enter valid name: ")
             Cname=Cname.capitalize()
            #---------------------------------------------------------------------------------------
             Cdob=input("Enter Date of Birth(DOB):(dd/mm/yyyy): ")
             flagValue=datevalidation(Cdob)
             while flagValue==False:
                Cdob=input("Enter valid date: ")
                flagValue=datevalidation(Cdob)                
             if len(str(Cdob))==9:
                if ('/' in str(Cdob)[0:2]):
                    Cdob="0"+str(Cdob)[0:10]
                elif ('/' in str(Cdob)[3:5]):
                    Cdob=str(Cdob)[0:3]+"0"+str(Cdob)[3:10]
             elif len(str(Cdob))==8:
                Cdob="0"+str(Cdob)[0:2]+"0"+str(Cdob)[2:9]
                
             while ((int(str(Cdob)[6:10])<1903) or (int(str(Cdob)[6:10])>2002)):
                if int(str(Cdob)[6:10])>2002:
                    print("You should be over 18.")
                elif int(str(Cdob)[6:10])<1903:
                    print("Your age is out of range.")
                Cdob=input("Enter valid date: ")    
                flagValue=datevalidation(Cdob)
                while flagValue==False:
                    Cdob=input("Enter valid date: ")
                    flagValue=datevalidation(Cdob)

                if len(str(Cdob))==9:
                    if ('/' in str(Cdob)[0:2]):
                        Cdob="0"+str(Cdob)[0:10]
                    elif ('/' in str(Cdob)[3:5]):
                        Cdob=str(Cdob)[0:3]+"0"+str(Cdob)[3:10]
                elif len(str(Cdob))==8:
                    Cdob="0"+str(Cdob)[0:2]+"0"+str(Cdob)[2:9]

             Cdob=(date(int(Cdob[6:10]),int(Cdob[3:5]),int(Cdob[0:2])))              
             Cage=today-Cdob
             Cage=int(str(Cage//365)[0:3])
#---------------------------------------------------------------------------------------        
             Cgender=input("M-Male\nF-Female\nO-Other\nEnter gender: ")
             while len(Cgender)!=1:
                 Cgender=input("Must be 1 letter. Enter valid gender: ")
             while (Cgender not in "FMOfmo"):
                 Cgender=input("Enter corresponding option. Enter Gender: ")
             Cgender=Cgender.upper()
#---------------------------------------------------------------------------------------
             Ccountry=input("Enter Country: ")
             while Ccountry=="":
                 Ccountry=input("Blank entered. Enter valid Country: ")
             while Ccountry.isdigit()==True:
                    Ccountry=input("Enter valid Country: ")
             Ccountry=Ccountry.capitalize()
#---------------------------------------------------------------------------------------
             Cstate=input("Enter State: ")
             while Cstate=="":
                Cstate=input("Blank entered. Enter valid State: ")
             while Cstate.isdigit()==True:
                Cstate=input("Enter valid State: ")
             Cstate=Cstate.capitalize()
#--------------------------------------------------------------------------------------- 
             Cadd=input("Enter Address: ")
             while Cadd=="":
                Cadd=input("Blank entered. Enter valid Address: ")
             Cadd=Cadd.capitalize()
#--------------------------------------------------------------------------------------- 
             Cphone=input("Enter phone number: ")
             while len(Cphone)!=10:
                Cphone=input("There needs to be 10 digits. Enter valid Phone number: ")
#---------------------------------------------------------------------------------------
             Cemail=input("Enter Email id: ")
             while ".com" not in Cemail:
                Cemail=input("Enter valid Email id: ")
             while "@" not in Cemail:
                Cemail=input("Enter valid Email id: ")
#---------------------------------------------------------------------------------------        
             cur.execute("insert into details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Roomno,Cname,Cdob,Cage,Cgender,Ccountry,Cstate,Cadd,Cphone,Cemail))
             con.commit()
             print("Customer details saved\n")
#=========================================================================================
 
             #rooms
             print("{:10}|{:10}|{:10}|{:10}|".format("Types","Single","Pair","Triple"))
             print("{:10}|{:10}|{:10}|{:10}|".format("Cabin","3200₹","4000₹","4800₹"))
             print("{:10}|{:10}|{:10}|{:10}|".format("Deluxe","5700₹","6500₹","7300₹"))
             print("{:10}|{:10}|{:10}|{:10}|".format("Super","7700₹","8500₹","9300₹"))
             print("{:10}|{:10}|{:10}|{:10}|".format("Luxury","9300₹","10000₹","10800₹"))
             print()

             print("Room type:\nC-Cabin\nD-Deluxe\nS-Super\nL-Luxury")
             Croom=input("Enter (first letter) for room type: ")
             while len(Croom)!=1:
                Croom=input("Enter valid room type: ")
             while (Croom.upper() not in "CDSL"):
                Croom=input("Enter valid room type: ")
             if Croom in "Cc":
                Croom="Cabin"
             elif Croom in "Dd":
                Croom="Deluxe"
             elif Croom in "Ss":
                Croom="Super"
             elif Croom in "Ll":
                Croom="Luxury"

             print("\nRoom size:\nS-Single\nP-Pair\nT-Triple")
             Csize=input("Enter (first letter) for room size: ")
             while len(Csize)!=1:
                Csize=input("Enter valid room size: ")
             while (Csize.upper() not in "SPT"):
                Csize=input("Enter valid room size\n:")
             if Csize in "Ss":
                Csize="Single"
             elif Csize in "Pp":
                Csize="Pair"
             elif Csize in "Tt":
                Csize="Triple"
             print("Room type:",Croom.upper(),"/ Room size:",Csize.upper()," ---> Selected.\n")
#---------------------------------------------------------------------------------------  
             print("Format: dd/mm/yyyy")
             Cindate=today
             Coutdate=input("Enter Out-date: ")
             flagValue=datevalidation(Coutdate)
             while flagValue==False:
                Coutdate=input("Enter valid Out-date: ")
                flagValue=datevalidation(Coutdate)
             if len(str(Coutdate))==9:
                if ('/' in str(Coutdate)[0:2]):
                    Coutdate="0"+str(Coutdate)[0:10]
                elif ('/' in str(Coutdate)[3:5]):
                    Coutdate=str(Coutdate)[0:3]+"0"+str(Coutdate)[3:10]
             elif len(str(Coutdate))==8:
                Coutdate="0"+str(Coutdate)[0:2]+"0"+str(Coutdate)[2:9]           
             Coutdate=(date(int(Coutdate[6:10]),int(Coutdate[3:5]),int(Coutdate[0:2])))
             while (Coutdate)<(Cindate):
                print("\nOut-date should be coming after/on today.")
                Coutdate=input("Enter valid date: ")
                flagValue=datevalidation(Coutdate)
                Coutdate=(date(int(Coutdate[6:10]),int(Coutdate[3:5]),int(Coutdate[0:2])))               
#---------------------------------------------------------------------------------------
             Cstay=Coutdate-Cindate
             if str(Cstay)[0]=="0":
                Cstay=1
             else:
                Cstay=str(Coutdate-Cindate)[0:2]
             print("Stay: ",Cstay)             
             Cnumroom=int(input("Enter number of rooms: "))
             Cnumppl=int(input("Enter number of  people: "))
#---------------------------------------------------------------------------------------
             cur.execute("insert into regis values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Roomno,Cname,Croom,Csize,Cindate,Coutdate,Cnumroom,Cnumppl,Cstay))
             query="insert into restaurant (Roomno) values ("+str(Croom)+")"
             cur.execute(query)
             con.commit()
             print("Customer registration details saved\n")
             print("THANKYOU FOR VISITING US")
#---------------------------------------------------------------------------------------
             itr=int(input("\nFor more new customers Enter: 0-YES | Any other number-NO: "))
             if itr==0:
                 pass
             else:
                 break

    cho=int(input("\nGo back to main menu? 0-YES | Any other number-NO: "))
    if cho==0:
        mainmenu()

            
#MENU ITEM 2: DISPLAY CUSTOMER DETAILS
def display():
   cho=0
   print("\nDo you want to...")
   amenudp=int(input("1: Display all Customer details\n2: Display 1 Customer details\
   \n3: Display by category\nEnter choice: "))
          
   if amenudp==1:
       displayAll()   
               
   if amenudp==2:
       displayOne()
             
   if amenudp==3:
       displayCtg()

   cho=int(input("\nGo back to main menu? 0-YES | Any other number-NO: "))
   if cho==0:
        mainmenu()
    

#MENU ITEM 3: UPDATE CUSTOMER DETAILS
def update():
    itr=0
    while itr==0:
        
        ch=int(input("\nEnter Room number to Update: "))
        
        cur.execute("select * from details where Roomno="+str(ch))  
        recordCount=cur.fetchall()
        if len(recordCount)!=0:
            print(recordCount)
    
        cur.execute("select * from regis where Roomno="+str(ch))  
        recordCount=cur.fetchall()
        if len(recordCount)!=0:
            print(recordCount)

        if len(recordCount)==1:   
                Sch=int(input("\n1: Customer name\n2: Customer DOB\n3: Customer gender\
                   \n4: Customer country\n5: Customer state\n6: Customer address\n7: Customer phone\n8: Customer email\
                   \n9: Customer Out-date\n10: Customer (No of rooms)\n11: Customer (no of people)\
                   \nChoose 1 category to update: "))
                     
                var=""                    
                if Sch==1:
                    var="Name="
                    Cname=input("Enter name(First Last): ")
                    while Cname=="":
                        Cname=input("Blank entered. Enter valid name: ")
                    while Cname.isdigit()==True:
                        Cname=input("Enter valid name: ")
                    Cname=Cname.capitalize()

                    updateQuery=("update details set "+var+"'"+Cname+"' where Roomno="+str(ch))
                    cur.execute(updateQuery)
                    con.commit()
                    query=("select * from details where Roomno="+str(ch))  
                    cur.execute(query)
                    recordCount=cur.fetchall()
                    print(recordCount)
                    
                    updateQuery1=("update regis set "+var+"'"+Cname+"' where Roomno="+str(ch))
                    cur.execute(updateQuery1)
                    con.commit()
                    query1=("select * from regis where Roomno="+str(ch))  
                    cur.execute(query1)
                    recordCount1=cur.fetchall()
                    print(recordCount1)
                    if len(recordCount)==1 and len(recordCount1)==1:
                        print("Record updated succesfully")
                        
                elif Sch==2:
                    var="Dob="                    
                    Cdob=input("Enter Date of Birth(DOB):(dd/mm/yyyy): ")
                    flagValue=datevalidation(Cdob)
                    while flagValue==False:
                        Cdob=input("Enter valid date: ")
                        flagValue=datevalidation(Cdob)                
                    if len(str(Cdob))==9:
                        if ('/' in str(Cdob)[0:2]):
                            Cdob="0"+str(Cdob)[0:10]
                        elif ('/' in str(Cdob)[3:5]):
                            Cdob=str(Cdob)[0:3]+"0"+str(Cdob)[3:10]
                    elif len(str(Cdob))==8:
                        Cdob="0"+str(Cdob)[0:2]+"0"+str(Cdob)[2:9]
                    
                    while ((int(str(Cdob)[6:10])<1903) or (int(str(Cdob)[6:10])>2002)):
                        if int(str(Cdob)[6:10])>2002:
                            print("You should be over 18.")
                        elif int(str(Cdob)[6:10])<1903:
                            print("Your age is out of range.")
                        Cdob=input("Enter valid date: ")    
                        flagValue=datevalidation(Cdob)
                        while flagValue==False:
                            Cdob=input("Enter valid date: ")
                            flagValue=datevalidation(Cdob)

                    if len(str(Cdob))==9:
                        if ('/' in str(Cdob)[0:2]):
                            Cdob="0"+str(Cdob)[0:10]
                        elif ('/' in str(Cdob)[3:5]):
                            Cdob=str(Cdob)[0:3]+"0"+str(Cdob)[3:10]
                    elif len(str(Cdob))==8:
                        Cdob="0"+str(Cdob)[0:2]+"0"+str(Cdob)[2:9]
                    Cdob=(date(int(Cdob[6:10]),int(Cdob[3:5]),int(Cdob[0:2])))
                    
                    updateQuery1=("update details set "+var+"'"+str(Cdob)+"' where Roomno="+str(ch))
                    cur.execute(updateQuery1)
                    con.commit()
                    query=("select * from details where Roomno="+str(ch))  
                    cur.execute(query)
                    recordCount=cur.fetchall()
                    print(recordCount)
                    if len(recordCount)==1:
                        print("Record updated succesfully")
            
                elif Sch==3:
                    var="Gender="
                    Cgender=input("M-Male\nF-Female\nO-Other\nEnter new gender: ")
                    while len(Cgender)!=1:
                        Cgender=input("Must be 1 letter. Enter valid gender: ")
                    while (Cgender not in "FMOfmo"):
                        Cgender=input("Enter corresponding option. Enter Gender: ")
                    Cgender=Cgender.upper()
                

                    updateQuery=("update details set "+var+"'"+Cgender+"' where Roomno="+str(ch))
                    cur.execute(updateQuery)
                    con.commit()
                    query=("select * from details where Roomno="+str(ch))  
                    cur.execute(query)
                    recordCount=cur.fetchall()
                    print(recordCount)
                    if len(recordCount)==1:
                        print("Record updated succesfully")

                elif Sch==4:
                    var="Country="
                    
                    Ccountry=input("Enter new Country: ")
                    while Ccountry=="":
                        Ccountry=input("Blank entered. Enter valid Country: ")
                    while Ccountry.isdigit()==True:
                        Ccountry=input("Enter valid Country: ")
                    Ccountry=Ccountry.capitalize()

                    updateQuery=("update details set "+var+"'"+Ccountry+"' where Roomno="+str(ch))
                    cur.execute(updateQuery)
                    con.commit()
                    query=("select * from details where Roomno="+str(ch))  
                    cur.execute(query)
                    recordCount=cur.fetchall()
                    print(recordCount)
                    if len(recordCount)==1:
                        print("Record updated succesfully")

                elif Sch==5:
                    var="State="

                    Cstate=input("Enter new State: ")
                    while Cstate=="":
                        Cstate=input("Blank entered. Enter valid State: ")
                    while Cstate.isdigit()==True:
                        Cstate=input("Enter valid State: ")
                    Cstate=Cstate.capitalize()

                    updateQuery=("update details set "+var+"'"+Cstate+"' where Roomno="+str(ch))
                    cur.execute(updateQuery)
                    con.commit()
                    query=("select * from details where Roomno="+str(ch))  
                    cur.execute(query)
                    recordCount=cur.fetchall()
                    print(recordCount)
                    if len(recordCount)==1:
                        print("Record updated succesfully")

                elif Sch==6:
                    var="Address="
                    Cadd=input("Enter new Address: ")
                    while Cadd=="":
                        Cadd=input("Blank entered. Enter valid Address: ")
                    Cadd=Cadd.capitalize()

                    updateQuery=("update details set "+var+"'"+Cadd+"' where Roomno="+str(ch))
                    cur.execute(updateQuery)
                    con.commit()
                    query=("select * from details where Roomno="+str(ch))  
                    cur.execute(query)
                    recordCount=cur.fetchall()
                    print(recordCount)
                    if len(recordCount)==1:
                        print("Record updated succesfully")
                        
                elif Sch==7:
                    var="Phone="
                    Cphone=input("Enter new phone number: ")
                    while len(Cphone)!=10:
                        Cphone=input("There needs to be 10 digits. Enter valid Phone number: ")

                    updateQuery=("update details set "+var+"'"+Cphone+"' where Roomno="+str(ch))
                    cur.execute(updateQuery)
                    con.commit()
                    query=("select * from details where Roomno="+str(ch))  
                    cur.execute(query)
                    recordCount=cur.fetchall()
                    print(recordCount)
                    if len(recordCount)==1:
                        print("Record updated succesfully")
                        
                elif Sch==8:
                    var="Email="
                    Cemail=input("Enter new email id: ")
                    while ".com" not in Cemail:
                        Cemail=input("Enter valid Email id: ")
                    while "@" not in Cemail:
                        Cemail=input("Enter valid Email id: ")

                    updateQuery=("update details set "+var+"'"+Cemail+"' where Roomno="+str(ch))
                    cur.execute(updateQuery)
                    con.commit()
                    query=("select * from details where Roomno="+str(ch))  
                    cur.execute(query)
                    recordCount=cur.fetchall()
                    print(recordCount)
                    if len(recordCount)==1:
                        print("Record updated succesfully")
                
                elif Sch==9:
                    print("Format: dd/mm/yyyy")
                    Cindate=today
                    Coutdate=input("Enter Out-date: ")
                    flagValue=datevalidation(Coutdate)
                    while flagValue==False:
                        Coutdate=input("Enter valid Out-date: ")
                        flagValue=datevalidation(Coutdate)
                    if len(str(Coutdate))==9:
                        if ('/' in str(Coutdate)[0:2]):
                            Coutdate="0"+str(Coutdate)[0:10]
                        elif ('/' in str(Coutdate)[3:5]):
                            Coutdate=str(Coutdate)[0:3]+"0"+str(Coutdate)[3:10]
                    elif len(str(Coutdate))==8:
                        Coutdate="0"+str(Coutdate)[0:2]+"0"+str(Coutdate)[2:9]
                        
                    Coutdate=(date(int(Coutdate[6:10]),int(Coutdate[3:5]),int(Coutdate[0:2])))
                    
                    while (Coutdate)<(Cindate):
                        print("\nOut-date should be coming after/on today.")
                        Coutdate=input("Enter valid date: ")
                        flagValue=datevalidation(Coutdate)                    
                        Coutdate=(date(int(Coutdate[6:10]),int(Coutdate[3:5]),int(Coutdate[0:2])))
                    Coutdate=str(Coutdate)

                    updateQuery1=("update regis set "+var+"'"+Coutdate+"' where Roomno="+str(ch))
                    cur.execute(updateQuery1)
                    con.commit()
                    query1=("select * from regis where Roomno="+str(ch))  
                    cur.execute(query1)
                    recordCount1=cur.fetchall()
                    print(recordCount1)
                    if len(recordCount1)==1:
                        print("Record updated succesfully")
                        
                elif Sch==10:
                    var="Numroom="
                    Cnumroom=int(input("Enter number of rooms: "))
                    
                    updateQuery1=("update regis set "+var+"'"+Cnumroom+"' where Roomno="+str(ch))
                    cur.execute(updateQuery1)
                    con.commit()
                    query1=("select * from regis where Roomno="+str(ch))  
                    cur.execute(query1)
                    recordCount1=cur.fetchall()
                    print(recordCount1)
                    if len(recordCount1)==1:
                        print("Record updated succesfully")
                    
                elif Sch==11:
                    var="Numppl="
                    Cnumppl=int(input("Enter number of  people: "))

                    updateQuery1=("update regis set "+var+"'"+Cnumppl+"' where Roomno="+str(ch))
                    cur.execute(updateQuery1)
                    con.commit()
                    query1=("select * from regis where Roomno="+str(ch))  
                    cur.execute(query1)
                    recordCount1=cur.fetchall()
                    print(recordCount1)
                    if len(recordCount1)==1:
                        print("Record updated succesfully")
                else:                
                    print("The category you entered is invalid. Enter proper category next time.")                    

        else:
            while len(recordCount)!=1:
                print("Room number does not exist")
                ch=int(input("\nEnter Room number to Update: "))
                    
        itr=int(input("To update more Enter: 0-YES | Any other number-NO: "))
        if itr==0:
            pass
        else:
            break
        
    cho=int(input("\nGo back to main menu? 0-YES | Any other number-NO: "))
    if cho==0:
        mainmenu()
        

#MENU ITEM 4: ADD RESTAURANT ITEMS
def food():
    itr=0
    while itr==0:
        def check():
            global ch
            ch=int(input("Enter Employee number to add items: "))
            z="select * from regis where Roomno='"+str(ch)+"'"
            cur.execute(z)
            records=cur.fetchall()
            return records
        
        while len(check())==0:
            print("No such employee number/exists")
            
        print("-"*41,"RESTAURANT ITEMS","-"*41)
        print("-"*100)
        print("CODE             ITEM\t\t             |   CODE             ITEM")
        print("-"*100)
        print("1             Pongal with Vadai\t\t     |   11            Samosa")
        print("2             Sambhar Idli\t\t     |   12            Pav Bhaji")
        print("3             Poori\t\t             |   13            Tea with Biscuits")
        print("4             Aloo Paratha\t\t     |   14            Filter Coffee")
        print("5             Bread with Scrambled Eggs      |   15            Chappathi")
        print("6             Waffles with Maple Syrup       |   16            Kulcha")
        print("7             Veg Fried Rice\t\t     |   17            Panner Butter Masala")
        print("8             Hakka Noodles\t\t     |   18            Kadai Veg")
        print("9             South Indian Meals             |   19            Bottled Water")
        print("10            North Indian Meals             |   20            Spite")
        print("-"*100)
        x=1
        h=0
        while x==1:
            co=int(input("\nEnter code number(Press 0 when all items are added)   :"))
            if co==0:
                print("-"*100)
                break
            if co in (1,2,3):
                h+=100
            elif co in (4,6):
                h+=150
            elif co in (5,):
                h+=85
            elif co in (7,8):
                h+=220
            elif co in (9,10):
                h+=135
            elif co in (11,19,20):
                h+=20
            elif co in (12,):
                h+=50
            elif co in (13,14):
                h+=30
            elif co in (15,):
                h+=40
            elif co in (16,):
                h+=65
            elif co in (17,18):
                h+=210
            else:
                continue
        print("\n")   
    
        query="update restaurant set Foodprice="+str(h)+"' where Roomno="+str(ch)
        try:
            cur.execute(query)
            print("Customer Room",ch," :ITEMS ADDED")
            con.commit()
        except:
            con.rollback()

        itr=int(input("\nTo add items for another customer Enter: 0-YES | Any other number-NO: "))
        if itr==0:
            pass
        else:
            break
        
    cho=int(input("\nGo back to main menu? 0-YES | Any other number-NO: "))
    if cho==0:
        mainmenu()   


#MENU ITEM 5: GENERATE BILL 
def bill():
    luxTax=18
    serviceTax=5
    indate=""
    outdate=""
    roomNo=""
    noppl=""
    type=""
    size=""
    stay=""
    roomNumber=input("Enter a Customer Number to generate bill: ")
    regisQuery=("select * from regis where Roomno="+str(roomNumber))
    cur.execute(regisQuery)
    custFetch=cur.fetchall()
    for i in custFetch:
        indate=i[4]
        type=i[2]
        size=i[3]
        outdate=i[5]
        roomNo=i[6]
        noppl=i[7]
        stay=i[8]
    detailQuery=("select * from details where Roomno="+str(roomNumber))
    cur.execute(detailQuery)
    detailFetch=cur.fetchall()
    for i in detailFetch:
        name=i[1]
        phone=i[8]
        address=i[7]
        email=i[9]
    print("\n")
    print("*"*73)
    print("****************************Customer Bill********************************")
    print("                                           Date              :",today)
    print("                                           Place             :","Chennai")    
    print("Customer Name     :",name)
    print("Customer Phone    :",phone)
    print("Indate            :",indate)
    print("outdate           :",outdate)
    print("Room number       :",str(roomNumber))
    print("Number of People  :",str(noppl))
    print("Type              :",type)
    print("Room size         :",size)
    print("Number of days    :",stay,"\n")
    cost=roomNo*roomCost(type,size)*int(stay)   
    print("*"*73)
    print("Hotel amount      :",cost)    
    luxCost=cost*(luxTax/100)    
    print("Luxary Tax        :",luxCost)    
    serCost= cost*(serviceTax/100)
    print("Service Tax       :",serCost,"\n")   
    totalTax=cost+luxCost+serCost
    print("*"*73)
    print("Total hotel amount:",totalTax)
    print("*"*73)

    print("Food amount       :",float(h),"  Rs")
    print("Service Tax       :",h*0.18,"  Rs")
    print("Total Food Amount :",h+(h*0.18),"  Rs\n")
    print("*"*73)
    print("GRAND TOTAL       :",totalTax+(h+(h*0.18)))
    print("*"*73)

#MENU ITEM :6 DELETE CUSTOMER DETAILS     
def delete():
    itr=0
    while itr==0:
        query=""
        query2=""
        def check():
            global ch
            ch=int(input("Enter Employee number to delete: "))
            z="select * from regis where Roomno='"+str(ch)+"'"
            cur.execute(z)
            records=cur.fetchall()
            return records
        
        while len(check())==0:
            print("No such employee number/exists")
                   
        query="delete from regis where Roomno= '"+str(ch)+"'"
        query2="delete from details where Roomno='"+str(ch)+"'"

        try:
                cur.execute(query)
                cur.execute(query2)
                print("Employee",ch," :RECORDS DELETED")
                con.commit()
        except:
                con.rollback()

               
        itr=int(input("\nTo delete more Enter: 0-YES | Any other number-NO: "))
        if itr==0:
            pass
        else:
            break

    cho=int(input("\nGo back to main menu? 0-YES | Any other number-NO: "))
    if cho==0:
        mainmenu()

        
#**************************************program functions*****************************************

#STAY OF CUSTOMER
def diff_dates(date1,date2):
    return abs(date2-date1).days

#VALIDATION OF DATES FUNCTION       
def datevalidation(date_string):
    flag= True 
    date_format = '%d/%m/%Y'    
    try:
        date_obj = datetime.strptime(date_string, date_format)
        #print(date_obj)
    except ValueError:
        print("\nIncorrect date/format.")
        flag=False
    return flag

#CALCULATING FEES FOR STAY - PART OF BILLING OR CUSTOMER
def roomCost(Croom,CSize):
    cabinRate=3200
    deluxeRate=5700
    superRate=7700
    luxuryRate=9300
    if Croom =="Cabin":
        if CSize=="Single":
            rate=cabinRate
        elif CSize=="Pair":
            rate=cabinRate+800
        elif CSize=="Triple":
            rate=cabinRate+1600
    elif Croom == "Deluxe":
        if CSize=="Single":
            rate=deluxeRate
        elif CSize=="Pair":
            rate=deluxeRate+800
        elif CSize=="Triple":
            rate=deluxeRate+1600
    elif Croom == "Super":
        if CSize=="Single":
            rate=superRate
        elif CSize=="Pair":
            rate=superRate+800
        elif CSize=="Triple":
            rate=superRate+1600
    elif Croom == "Luxury":
        if CSize=="Single":
            rate=luxuryRate
        elif CSize=="Pair":
            rate=luxuryRate+800
        elif CSize=="Triple":
            rate=luxuryRate+1600
    return rate


#DISPLAY PART 0: FETCHING CUSTOMER DETAILS FOR DISPLAY
def executeQuery():
    custFetch=[]
    roomNumber=int(input("\nEnter Customer's room number to search: "))
    regisQuery=("select * from regis where Roomno="+str(roomNumber))
    detailQuery=("select * from details where Roomno="+str(roomNumber))
    cur.execute(regisQuery)
    custFetch=cur.fetchall()
    cur.execute(detailQuery)
    custFetch+=cur.fetchall()
    return custFetch;

#DISPLAY PART 1: DISPLAY ONE            
def displayOne():
   itr=0
   while itr==0:            
        custDetail=executeQuery()     
        while len(custDetail)==0: 
                print("No such customer room number/exists")
                custDetail=executeQuery()
                if len(custDetail)>0:
                    for i in custDetail:
                        print(i) 
                    break
        else:
            for i in custDetail:
                print(i)                
            custDetail=""                
        itr=int(input("To display more Enter: 0-YES | Any other number-NO: "))
        if itr==0:
            pass
        else:
            break

#DISPLAY PART 2: DISPLAY ALL
def displayAll():
    itr=0
    while itr==0:
        print("\nDo you want to display...")
        ch=int(input("1: Customer itentity details\n2: Customer registration details\n3: Both\nEnter choice: "))              
        if ch==1:
           cur.execute("select * from details")
           x=cur.fetchall()
           print("\n")
           for i in x:
               print(i)
           itr=int(input("\nTo display more Enter: 0-YES | Any other number-NO: "))
           if itr==0:
               pass
           else:
               break
        elif ch==2:
            cur.execute("select * from regis")
            x=cur.fetchall()
            print("\n")
            for i in x:
                print(i)
            itr=int(input("\nTo display more Enter: 0-YES | Any other number-NO: "))
            if itr==0:
                pass
            else:
                break                    
        elif ch==3:
            cur.execute("SELECT d.Roomno,d.Name,d.DOB,d.Age,d.Gender,d.Country,d.State,d.Address,d.Phone,d.Email,r.Type,r.Size,r.Indate,r.Outdate,r.Numroom,r.Numppl,r.Stay FROM details d,regis r WHERE d.Roomno=r.Roomno")                                
            x=cur.fetchall()
            print("\n")
            for i in x:
                print(i)
    
            itr=int(input("\nTo display more Enter: 0-YES | Any other number-NO: "))
            if itr==0:
                pass
            else:
                break

#DISPLAY PART 3: DISPLAY BY CATEGORY
def displayCtg():
    itr=0
    while itr==0:   
            userInput=''
            detailslist=[]
            regislist=[]
            print("\n1: Room number\n2: Customer name\n3: Customer DOB\n4: Customer age\n5: Customer gender\
               \n6: Customer country\n7: Customer state\n8: Customer address\n9: Customer phone\n10: Customer email\
               \n11: Customer In-date\n12: Customer Out-date\n13: Customer (No of rooms)\n14: Customer (no of people)\
               \nEnter 1 or more categories to search.")
            def validate():
                flag=0
                for i in range(len(detailslist)):
                    if(int(detailslist[i])>14 or int(detailslist[i])<1):
                        flag=1
                return flag
            def userInputFn():
                userInput=input("Example : 1,3,4; Enter categories: ")
                detailslist = userInput.split(",")
                return detailslist
            
            detailslist = userInputFn()
            checkFlag=validate()
            while(checkFlag==1):
                detailslist = userInputFn()
                checkFlag=validate()
                
            for i in range(len(detailslist)):
                if(int(detailslist[i])==11 or int(detailslist[i])==12 or int(detailslist[i])==13 or int(detailslist[i])==14):
                    regislist.append(detailslist[i])
            detailslist= [i for i in detailslist if i not in regislist]
            categories=["Roomno","Name","DOB","Age","Gender","Country","State","Address","Phone","Email","Indate","Outdate","Numroom","Numppl"]
            z=""
            for i in detailslist:
                z+=categories[int(i)-1]+","
            z=z[:-1]
            ch=" "
            if len(z)!=0:
                query="select "+z+" from details"
                cur.execute(query)
                ch=cur.fetchall()
                print(ch)#details table
            z=""
            for i in regislist:
                z+=categories[int(i)-1]+","
            z=z[:-1]
            if len(z)!=0:
                query="select "+z+" from regis" 
                cur.execute(query)
                ch=cur.fetchall()
                print(ch)#regis table
            z=""
            #query=("SELECT d.Roomno,d.Name,d.DOB,d.Age,d.Gender,d.Country,d.State,d.Address,d.Phone,d.Email,r.Type,r.Size,r.Indate,r.Outdate,r.Numroom,r.Numppl,r.Stay FROM details d,regis r WHERE d.Roomno=r.Roomno and d.Roomno="+str(ch))
            #cur.execute(query)

            itr=int(input("\nTo display more Enter: 0-YES | Any other number-NO: "))
            if itr==0:
                pass
            else:
                break

#def roomstatus():
            
    #MAKE CONTENTS OF ROOM STATUS FUNCTION - def roomstatus() and put the contents of your program inside this. 
    #then call this roomstatus() function in the add() function in the top which is mainmenu option 1
    #and then at the end of add() function save the roomstatus taken/empty as a seperate column in the regis table present

mainmenu()
print("THANKYOU FOR VISITING US!")
con.close()
        

     

            


