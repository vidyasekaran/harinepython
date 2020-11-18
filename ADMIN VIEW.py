#PART 1 ADMIN VIEW 
#My Changes

import mysql.connector as mys
from datetime import date
from datetime import datetime
import sys

con=mys.connect(host='localhost',username='root',password='guru',charset='utf8')
cur=con.cursor()
cur.execute("create database if not exists staff")
cur.execute("use staff")
print("Database created")
cur.execute("create table if not exists sdetails(Sempno int,Sname char(20),Sdob char(15),Sage int,Sgender char(1),Sadd char(70),Sphone char(11),Semail char(25))")
cur.execute("create table if not exists sregis(Sempno int,Sname char(20),Stype char(30),Sshift char(15),Sjoin char(11))")
print("Tables created")

d=m=y=entry=0
c="0"
z=""

#PASSWORD TO ENTER INTO STAFF VIEW
cho=int(input("\n1: Admin\n2: Staff\n3: Customer\nEnter choice: "))
if cho==1:
    pwd=input("Enter Admin password: ")
    for i in range(3):   
        if pwd!="rootadmin":
            pwd=input("Wrong password, try again: ")
            if i==2:
                print("Attempt failed. Run application again.")
                sys.exit()

#STAFF VIEW'S MAIN MENU
def mainmenu():
    print("\nMain menu")
    amenu=int(input("1: Add new staff \n2: Display staff details\n3: Update 1 staff member detail\
    \n4: Delete 1 staff member detail\n5: Exit\nEnter choice: "))

    if amenu==1:
        add()
    if amenu==2:
        display()  
    if amenu==3:
        update()
    if amenu==4:
        delete()
    if amenu==5:
        sys.exit()

#MENU ITEM 1: ADD NEW CUSTOMER
def add():
    cho=0
    itr=0
    while itr==0:
           print("Enter details below for New staff member:")
           try:
               cur.execute("select Sempno from sdetails ORDER BY Sempno DESC LIMIT 1")
               x=cur.fetchall()
               w=x[0][0]
               emp=w+1
               print("New Staff number: ",emp)
               Sempno=emp
               print()
           except IndexError:
               emp=1001
               print("New Staff number: ",emp)
               Sempno=1001
               x=""
#-------------------------------------------------------------------------------------
           Sname=input("Enter name(First Last): ")
           while Sname=="":
                   Sname=input("Blank entered. Enter valid name: ")
           while Sname.isdigit()==True:
                   Sname=input("Enter valid name: ")
           Sname=Sname.capitalize()
#---------------------------------------------------------------------------------------
           Sdob=input("Enter Date of Birth(DOB):(dd/mm/yyyy): ")
           flagValue=datevalidation(Sdob)
           while flagValue==False:
                Sdob=input("Enter valid date: ")
                flagValue=datevalidation(Sdob)                
           if len(str(Sdob))==9:
                if ('/' in str(Sdob)[0:2]):
                    Sdob="0"+str(Sdob)[0:10]
                elif ('/' in str(Sdob)[3:5]):
                    Sdob=str(Sdob)[0:3]+"0"+str(Sdob)[3:10]
           elif len(str(Sdob))==8:
                Sdob="0"+str(Sdob)[0:2]+"0"+str(Sdob)[2:9]
                
           while ((int(str(Sdob)[6:10])<1903) or (int(str(Sdob)[6:10])>2002)):
                if int(str(Sdob)[6:10])>2002:
                    print("You should be over 18.")
                elif int(str(Sdob)[6:10])<1903:
                    print("Your age is out of range.")
                Sdob=input("Enter valid date: ")    
                flagValue=datevalidation(Sdob)
                while flagValue==False:
                    Sdob=input("Enter valid date: ")
                    flagValue=datevalidation(Sdob)

                if len(str(Sdob))==9:
                    if ('/' in str(Sdob)[0:2]):
                        Sdob="0"+str(Sdob)[0:10]
                    elif ('/' in str(Sdob)[3:5]):
                        Sdob=str(Sdob)[0:3]+"0"+str(Sdob)[3:10]
                elif len(str(Sdob))==8:
                    Sdob="0"+str(Sdob)[0:2]+"0"+str(Sdob)[2:9]

           Sdob=(date(int(Sdob[6:10]),int(Sdob[3:5]),int(Sdob[0:2])))              
           Sage=today-Sdob
           Sage=int(str(Sage//365)[0:3])
#---------------------------------------------------------------------------------------        
           Sgender=input("M-Male\nF-Female\nO-Other\nEnter gender: ")
           while len(Sgender)!=1:
               Sgender=input("Must be 1 letter. Enter valid gender: ")
           while (Sgender not in "FMOfmo"):
               Sgender=input("Enter corresponding option. Enter Gender: ")
           Sgender=Sgender.upper()
#---------------------------------------------------------------------------------------
           Sadd=input("Enter Address: ")
           while Sadd=="":
              Sadd=input("Blank entered. Enter valid Address: ")
           Sadd=Sadd.capitalize()
#--------------------------------------------------------------------------------------- 
           Sphone=input("Enter phone number: ")
           while len(Sphone)!=10:
              Sphone=input("There needs to be 10 digits. Enter valid Phone number: ")
#---------------------------------------------------------------------------------------
           Semail=input("Enter Email id: ")
           while ".com" not in Semail:
              Semail=input("Enter valid Email id: ")
           while "@" not in Semail:
              Semail=input("Enter valid Email id: ")
#---------------------------------------------------------------------------------------        
           cur.execute("insert into sdetails values(%s,%s,%s,%s,%s,%s,%s,%s)",(Sempno,Sname,Sdob,Sage,Sgender,Sadd,Sphone,Semail))
           con.commit()
           print("Staff details saved\n")
#=========================================================================================

           Stype=input("1.Security\n2.Roomkeepers\n3.Receptionist\n4.Resturant staff\nEnter category: ")
           while (Stype not in "1234"):
              Stype=input("Corresponding number needed. Enter valid category: ")
           if Stype=="1":
              Stype="Security"
           elif Stype=="2":
              Stype="Roomkeepers"
           elif Stype=="3":
              Stype="Receptionist"
           elif Stype=="4":
              Stype=input("1.Chef\n2.Server\nEnter category: ")
              while (Stype not in "12"):
                  Stype=input("Corresponding number needed. Enter valid category: ")
              if Stype=="1":
                  Stype="Chef"
              elif Stype=="2":
                  Stype="Server"
           print()
#-----------------------------------------------------------
           Sshift=input("1.6 AM to 6 PM\n2.6 PM to 6 AM\nEnter time shift :")
           while (Sshift not in "12"):
                  Sshift=input("Corresponding number needed. Enter valid time shift: ")
           if Sshift=="1":
              Sshift="6 AM to 6 PM"
           if Sshift=="2":
              Sshift="6 PM to 6 AM"
           print()  
#------------------------------------------------------------
           Sjoin=today
#------------------------------------------------------------
           cur.execute("insert into sregis values(%s,%s,%s,%s,%s)",(Sempno,Sname,Stype,Sshift,Sjoin))
           con.commit()
           print("Staff registration details saved\n")

           itr=int(input("\nFor more new staff Enter: 0-YES | Any other number-NO: "))
           if itr==0:
              pass
           else:
              break

    cho=int(input("\nGo back to main menu? 0-YES | Any other number-NO: "))
    if cho==0:
        mainmenu()
    
            
#MENU ITEM 2: DISPLAY STAFF DETAILS
def display():
   cho=0
   print("\nDo you want to...")
   amenudp=int(input("1: Display all staff details\n2: Display 1 staff member details\
   \n3: Display by category\nEnter choice: "))
          
   if amenudp==1:
       displayAll()   
               
   elif amenudp==2:
       displayOne()
             
   elif amenudp==3:
       displayCtg()

   else:
        while str(amenudp) not in "1 2 3":
            amenudp=int(input("\nEnter valid choice: "))

   cho=int(input("\nGo back to main menu? 0-YES | Any other number-NO: "))
   if cho==0:
        mainmenu()

#MENU ITEM 3: UPDATE CUSTOMER DETAILS
def update():
    itr=0
    while itr==0:
    
        ch=int(input("\nEnter Employee number to Update: "))
    
        cur.execute("select * from sdetails where Sempno="+str(ch))  
        recordCount=cur.fetchall()
        if len(recordCount)!=0:
            print(recordCount)
    
        cur.execute("select * from sregis where Sempno="+str(ch))  
        recordCount=cur.fetchall()
        if len(recordCount)!=0:
            print(recordCount)
            
        if len(recordCount)==1:
            Sch=int(input("\n1: Employee Name\n2: Employee DOB\n3: Employee Gender\n4: Employee Address\n\
            5: Employee Phone number\n6: Employee Email id \n7: Employee Time Shift\n8: Employee Type\n\
            Enter 1 option to update."))
            
            var=""
            if Sch==1:
                var="Sname="
                Sname=input("Enter name(First Last): ")
                while Sname=="":
                    Sname=input("Blank entered. Enter valid name: ")
                while Sname.isdigit()==True:
                    Sname=input("Enter valid name: ")
                Sname=Sname.capitalize()
  
                updateQuery=("update sdetails set "+var+"'"+Sname+"' where Sempno="+str(ch))
                cur.execute(updateQuery)
                con.commit()
                query=("select * from sdetails where Sempno="+str(ch))  
                cur.execute(query)
                recordCount=cur.fetchall()
                print(recordCount)
                
                updateQuery1=("update sregis set "+var+"'"+Sname+"' where Sempno="+str(ch))
                cur.execute(updateQuery1)
                con.commit()
                query1=("select * from sregis where Sempno="+str(ch))  
                cur.execute(query1)
                recordCount1=cur.fetchall()
                print(recordCount1)
                if len(recordCount)==1 and len(recordCount1)==1:
                    print("Record updated succesfully")
                    
            elif Sch==2:
                var="Sdob="
                Sdob=input("Enter Date of Birth(DOB):(dd/mm/yyyy): ")
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
  
                updateQuery=("update sdetails set "+var+"'"+Sdob+"' where Sempno="+str(ch))
                cur.execute(updateQuery)
                con.commit()
                query=("select * from sdetails where Sempno="+str(ch))  
                cur.execute(query)
                recordCount=cur.fetchall()
                print(recordCount)
                if len(recordCount)==1:
                    print("Record updated succesfully")
        
            elif Sch==3:
                var="Sgender="
                Sgender=input("M-Male\nF-Female\nO-Other\nEnter gender: ")
                while len(Sgender)!=1:
                    Sgender=input("Must be 1 letter. Enter valid gender: ")
                while (Sgender not in "FMOfmo"):
                    Sgender=input("Enter corresponding option. Enter Gender: ")
                Sgender=Sgender.upper()
            
  
                updateQuery=("update sdetails set "+var+"'"+Sgender+"' where Sempno="+str(ch))
                cur.execute(updateQuery)
                con.commit()
                query=("select * from sdetails where Sempno="+str(ch))  
                cur.execute(query)
                recordCount=cur.fetchall()
                print(recordCount)
                if len(recordCount)==1:
                    print("Record updated succesfully")

            elif Sch==4:
                var="Sadd="
                Sadd=input("Enter Address: ")
                while Sadd=="":
                    Sadd=input("Blank entered. Enter valid Address: ")
                Sadd=Sadd.capitalize()
  
                updateQuery=("update sdetails set "+var+"'"+Sadd+"' where Sempno="+str(ch))
                cur.execute(updateQuery)
                con.commit()
                query=("select * from sdetails where Sempno="+str(ch))  
                cur.execute(query)
                recordCount=cur.fetchall()
                print(recordCount)
                if len(recordCount)==1:
                    print("Record updated succesfully")

            elif Sch==5:
                var="Sphone="
                Sphone=input("Enter phone number: ")
                while len(Sphone)!=10:
                    Sphone=input("There needs to be 10 digits. Enter valid Phone number: ")
  
                updateQuery=("update sdetails set "+var+"'"+Sphone+"' where Sempno="+str(ch))
                cur.execute(updateQuery)
                con.commit()
                query=("select * from sdetails where Sempno="+str(ch))  
                cur.execute(query)
                recordCount=cur.fetchall()
                print(recordCount)
                if len(recordCount)==1:
                    print("Record updated succesfully")
                    
            elif Sch==6:
                var="Semail="
                Semail=input("Enter Email id: ")
                while ".com" not in Semail:
                    Semail=input("Enter valid Email id: ")
                while "@" not in Semail:
                    Semail=input("Enter valid Email id: ")
  
                updateQuery=("update sdetails set "+var+"'"+Semail+"' where Sempno="+str(ch))
                cur.execute(updateQuery)
                con.commit()
                query=("select * from sdetails where Sempno="+str(ch))  
                cur.execute(query)
                recordCount=cur.fetchall()
                print(recordCount)
                if len(recordCount)==1:
                    print("Record updated succesfully")

            elif Sch==7:
                var="Sshift="
                Sshift=input("1.6 AM to 6 PM\n2.6 PM to 6 AM\nEnter time shift :")
                while (Sshift not in "12"):
                    Sshift=input("Corresponding number needed. Enter valid time shift: ")
                if Sshift=="1":
                    Sshift="6 AM to 6 PM"
                if Sshift=="2":
                    Sshift="6 PM to 6 AM"
                print()  

                updateQuery1=("update sregis set "+var+"'"+Sshift+"' where Sempno="+str(ch))
                cur.execute(updateQuery1)
                con.commit()
                query1=("select * from sregis where Sempno="+str(ch))  
                cur.execute(query1)
                recordCount1=cur.fetchall()
                print(recordCount1)
                if len(recordCount1)==1:
                    print("Record updated succesfully")

            
            if Sch==8:
                var="Stype="            
                Stype=input("1.Security\n2.Roomkeepers\n3.Receptionist\n4.Resturant staff\nEnter category: ")
                while (Stype not in "1234"):
                    Stype=input("Corresponding number needed. Enter valid category: ")
                if Stype=="1":
                    Stype="Security"
                elif Stype=="2":
                    Stype="Roomkeepers"
                elif Stype=="3":
                    Stype="Receptionist"
                elif Stype=="4":
                    Stype=input("1.Chef\n2.Server\nEnter category: ")
                    while (Stype not in "12"):
                        Stype=input("Corresponding number needed. Enter valid category: ")
                    if Stype=="1":
                        Stype="Chef"
                    elif Stype=="2":
                        Stype="Server"
                print()

                updateQuery1=("update sregis set "+var+"'"+Stype+"' where Sempno="+str(ch))
                cur.execute(updateQuery1)
                con.commit()
                query1=("select * from sregis where Sempno="+str(ch))  
                cur.execute(query1)
                recordCount1=cur.fetchall()
                print(recordCount1)
                if len(recordCount1)==1:
                    print("Record updated succesfully")
                    
        else:
            while len(recordCount)!=1:
                print("Employee number does not exist")
                ch=int(input("\nEnter Room number to Update: "))
                
        itr=int(input("To update more Enter: 0-YES | Any other number-NO: "))
        if itr==0:
            pass
        else:
            break
        
    cho=int(input("\nGo back to main menu? 0-YES | Any other number-NO: "))
    if cho==0:
        mainmenu()
        
#MENU ITEM 4: DELETE CUSTOMER DETAILS      
def delete():
    itr=0
    while itr==0:
        query=""
        query2=""
        def check():
            global ch
            ch=int(input("Enter Employee number to delete: "))
            z="select * from sregis where Sempno='"+str(ch)+"'"
            cur.execute(z)
            records=cur.fetchall()
            return records
        
        while len(check())==0:
            print("No such employee number/exists")
                   
        query="delete from sregis where Sempno= '"+str(ch)+"'"
        query2="delete from sdetails where Sempno='"+str(ch)+"'"

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

mainmenu()
print("The end")
con.close()

#=========================================================================================        
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

#DISPLAY PART 0: FETCHING STAFF DETAILS FOR DISPLAY
def executeQuery():
    employeeNumber=int(input("\nEnter Employee number to search: "))
    regisQuery=("select * from sregis where Sempno="+str(employeeNumber))
    detailQuery=("select * from sdetails where Sempno="+str(employeeNumber))
    cur.execute(regisQuery)
    empFetch=cur.fetchall()
    cur.execute(detailQuery)
    empFetch+=cur.fetchall()
    return empFetch;

#DISPLAY PART 1: DISPLAY ONE
def displayOne():
    itr=0
    while itr==0:            
            empDetail=executeQuery()            
            while len(empDetail)==0: 
                    print("No such employee number/exists")
                    empDetail=executeQuery()
                    if len(empDetail)>0:
                        for i in empDetail:
                            print(i) 
                        break
            else:
                for i in empDetail:
                    print(i)                
                empDetail=""                
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
        ch=int(input("1: Staff itentity details\n2: Staff registration details\n3: Both\nEnter choice: "))              
        if ch==1:
           cur.execute("select * from sdetails")
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
            cur.execute("select * from sregis")
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
            cur.execute("SELECT d.Empno,d.Sname,d.Sdob,d.Sage,d.Sgender,d.Sadd,d.Sphone,d.Semail,r.Stype,r.Sshift,r.Sjoin,r.Sbasic,r.Stax,r.Sbonus,r.Snetsalary FROM sdetails d,sregis r WHERE d.Empno=r.Empno")                                
            x=cur.fetchall()
            print("\n")
            for i in x:
                print(i)

            itr=int(input("To display more Enter: 0-YES | Any other number-NO: "))
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
            print("\n1: Employee number\n2: Employee name\n3: Employee DOB\n4: Employee age\n5: Employee gender\
               \n6: Employee type\n7: Employee shift\n8: Employee join date\
               \nEnter 1 or more categories to search.")
            def validate():
                flag=0
                for i in range(len(detailslist)):
                    if(int(detailslist[i])>8 or int(detailslist[i])<1):
                        flag=1
                return flag            
            def userInputFn():
                userInput=input("Ex:1,3,4; Enter categories: ")
                detailslist = userInput.split(",")
                return detailslist
            
            detailslist = userInputFn()
            checkFlag=validate()
            while(checkFlag==1):
                print("Wrong Value Entered - Enter Only 1-8") 
                detailslist = userInputFn()
                checkFlag=validate()
                
            for i in range(len(detailslist)):
                if(int(detailslist[i])==6 or int(detailslist[i])==7 or int(detailslist[i])==8):
                    regislist+=detailslist[i]
            detailslist= [i for i in detailslist if i not in regislist]              
            categories=["Sempno","Sname","Sdob","Sage","Sgender","Sstate","Stype","Sshift","Sjoin"]
            z=""
            for i in detailslist:
                z+=categories[int(i)-1]+","
            z=z[:-1]
            ch=" "
            if len(z)!=0:
                query="select "+z+" from sdetails"
                cur.execute(query)
                ch=cur.fetchall()
                print(ch)#details table
            z=""
            for i in regislist:
                z+=categories[int(i)-1]+","
            z=z[:-1]
            if len(z)!=0:
                query="select "+z+" from sregis" 
                cur.execute(query)
                ch=cur.fetchall()
                print(ch)#regis table
            
            itr=int(input("\nTo display more Enter: 0-YES | Any other number-NO: "))
            if itr==0:
                pass
            else:
                break


            
      
        
        
        
        

