#Computer Science Project

#Welcome To Berozgars' Portal

#importing sql
import mysql.connector as sq

# importing tkinter module
import tkinter 
from tkinter import *
#importing fonts
import tkinter.font as tkFont


def c1():
    
    #getting buttons to go to forms
    nw=Tk()
    nw.title("Berozgar")
    nw.geometry("800x800")    
    nw.configure(bg='black')
    fontStyle = tkFont.Font(family="Segoe Script",size=50)
    l2=tkinter.Label(nw,text='\n\n\n\n\n\n\nYou are a \n\n',font=fontStyle,bg='black',fg='white')
    b2=tkinter.Button(nw,text='\n    Unemployed     \n',bg='#54FA9B',command=c2,)
    b3=tkinter.Button(nw,text='\n     Company/Employer     \n',bg='#54FA9B',command=c3)
    l2.pack()
    b2.pack()
    b3.pack()
   
def c2():
    
    #form for unemployed people to get connected to the portal
    nw =Tk()
    nw.title("Form for Unemployed People")
    nw.geometry("800x800")
    nw.configure(bg='dodgerblue')
    L1=Label(nw,text='Name',font=fontStyle2,bg='dodgerblue')
    E1=Entry(nw,width=50,bg='black',fg='white')
    L1.pack()
    E1.pack()
    L2=Label(nw,text='Age (in integers)',font=fontStyle2,bg='dodgerblue')
    E2=Entry(nw,width=10,bg='black',fg='white')
    L2.pack()
    E2.pack()
    L3=Label(nw,text='Skills',font=fontStyle2,bg='dodgerblue')
    E3=Entry(nw,width=50,bg='black',fg='white')
    L3.pack()
    E3.pack()
    bx1 = Button(nw,text="Python Programming",command=lambda:set_text("Python_Programming"),bg='yellow')
    bx1.pack()

    bx2 = Button(nw,text="  C++ Programming  ",command=lambda:set_text("C++Programming"),bg='yellow')
    bx2.pack()
    bx3 = Button(nw,text="     Cooking     ",command=lambda:set_text("Cooking"),bg='yellow')
    bx3.pack()
    bx4 = Button(nw,text="   Car Mechanic  ",command=lambda:set_text("Car_Mechanic"),bg='yellow')
    bx4.pack()
    bx5 = Button(nw,text="    Plumbing     ",command=lambda:set_text("Plumbing"),bg='yellow')
    bx5.pack()
    bx6 = Button(nw,text="Video and Photo Editing",command=lambda:set_text("Video_and_Photo_Editing"),bg='yellow')
    bx6.pack()
    bx7 = Button(nw,text="   Electrician   ",command=lambda:set_text("Electrician"),bg='yellow')
    bx7.pack()
    
    def set_text(text):
        
        #entering the input of selected button in the entry box
        E3.delete(0,END)
        E3.insert(0,text)
        return
    
    L4=Label(nw,text='Minimum Expected Salary (in integers)',bg='dodgerblue',font=fontStyle2)
    E4=Entry(nw,bg='black',fg='white')
    L4.pack()
    E4.pack()
    L5=Label(nw,text='State',font=fontStyle2,bg='dodgerblue')
    E5=Entry(nw,bg='black',fg='white')
    L5.pack()
    E5.pack()
    L6=Label(nw,text='Job Location',font=fontStyle2,bg='dodgerblue')
    E6=Entry(nw,width=50,bg='black',fg='white')
    L6.pack()
    E6.pack()
    bxx1=Button(nw,text="Local",command=lambda:set_text2("Local"),bg='yellow')
    bxx1.pack()
    bxx2=Button(nw,text='Inter-State',command=lambda:set_text2("Inter_State"),bg='yellow')
    bxx2.pack()
    
    def set_text2(text):
        E6.delete(0,END)
        E6.insert(0,text)
        return
    L7=Label(nw,text='Email',font=fontStyle2,bg='dodgerblue')
    E7=Entry(nw,width=50,bg='black',fg='white')
    L7.pack()
    E7.pack()
    L8=Label(nw,text='Qualifications',font=fontStyle2,bg='dodgerblue')
    E8=Entry(nw,width=50,bg='black',fg='white')
    L8.pack()
    E8.pack()
    L9=Label(nw,text='Aadhaar',font=fontStyle2,bg='dodgerblue')
    E9=Entry(nw,width=50,bg='black',fg='white')
    L9.pack()
    E9.pack()
    L10=Label(nw,text='Address',font=fontStyle2,bg='dodgerblue')
    E10=Entry(nw,width=100,bg='black',fg='white')
    L10.pack()
    E10.pack()
    
    def c4():

        #adding data of unemployed people on MYSQL table named "jobless"
        mycon=sq.connect(host="localhost",user="root",passwd="asplasht8",database="records")
        ent1=Entry.get(E1)#name
        naam=ent1.split()
        
        for x in range (len(naam)):
            cap=naam[x].capitalize()
            cap=cap + " "
            naam[x]=cap
        sp=""
        
        for y in range (len(naam)):
            sp=sp+naam[y]
        ent1=sp
        ent2=Entry.get(E2)#age
        ent3=Entry.get(E3)#skills
        ent4=Entry.get(E4)#salary
        ent5=Entry.get(E5)#state
        ent6=Entry.get(E6)#job location
        ent7=Entry.get(E7)#email
        ent7=ent7.lower()
        ent8=Entry.get(E8)#qualifications
        ent9=Entry.get(E9)#aadhar
        ent10=Entry.get(E10)#address
        mycon=sq.connect(host="localhost",user="root",passwd="asplasht8",database="records")
        ins="INSERT into jobless(NAME,AGE,SKILLS,MINIMUM_EXPECTED_SALARY,STATE,JOB_LOCAL_INTERSTATE,EMAIL_ID,QUALIFICATIONS,ADHAAR,ADDRESS) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(ent1,ent2,ent3,ent4,ent5,ent6,ent7,ent8,ent9,ent10)
        cursor=mycon.cursor()
        cursor.execute(ins)
        mycon.commit()
        databack="ent1"+"ent2"+"ent3"
        filebackup=open("jobless.txt","a")
        filebackup.writelines(databack)
        filebackup.close()
                
    b4=tkinter.Button(nw,text='\nSUBMIT\n',command=c4,bg='red',fg='white')
    b4.pack()
    
def c3():
    
    #form for company to get registered to the portal
    nw =Tk()
    nw.configure(bg="orange Red")
    nw.title("Form for Companies to get Details")
    nw.geometry("800x800")
    L11=Label(nw,text='Registration Number',font=fontStyle2,bg="orange Red")
    E11=Entry(nw,width=100,bg='grey25',fg='white')
    L11.pack()
    E11.pack()
    L12=Label(nw,text='Name Of Company',font=fontStyle2,bg="orange Red")
    E12=Entry(nw,width=100,bg='grey25',fg='white')
    L12.pack()
    E12.pack()
    L13=Label(nw,text='Name of Representative',font=fontStyle2,bg="orange Red")
    E13=Entry(nw,width=80,bg='grey25',fg='white')
    L13.pack()
    E13.pack()
    L14=Label(nw,text='Designation of Representative',font=fontStyle2,bg="orange Red")
    E14=Entry(nw,width=50,bg='grey25',fg='white')
    L14.pack()
    E14.pack()
    L15=Label(nw,text='Number of Employee Needed',font=fontStyle2,bg="orange Red")
    E15=Entry(nw,width=30,bg='grey25',fg='white')
    L15.pack()
    E15.pack()
    L16=Label(nw,text='Branch',font=fontStyle2,bg="orange Red")
    E16=Entry(nw,width=50,bg='grey25',fg='white')
    L16.pack()
    E16.pack()
    bx1 = Button(nw,text="Python Programming",command=lambda:set_text3("Python_Programming"),bg='gold')
    bx1.pack()

    bx2 = Button(nw,text="  C++ Programming  ",command=lambda:set_text3("C++Programming"),bg='gold')
    bx2.pack()
    bx3 = Button(nw,text="     Cooking     ",command=lambda:set_text3("Cooking"),bg='gold')
    bx3.pack()
    bx4 = Button(nw,text="   Car Mechanic  ",command=lambda:set_text3("Car_Mechanic"),bg='gold')
    bx4.pack()
    bx5 = Button(nw,text="    Plumbing     ",command=lambda:set_text3("Plumbing"),bg='gold')
    bx5.pack()
    bx6 = Button(nw,text="Video and Photo Editing",command=lambda:set_text3("Video_and_Photo_Editing"),bg='gold')
    bx6.pack()
    bx7 = Button(nw,text="   Electrician   ",command=lambda:set_text3("Electrician"),bg='gold')
    bx7.pack()
    
    def set_text3(text):
        E16.delete(0,END)
        E16.insert(0,text)
        return
  
    L17=Label(nw,text='Job Location(State)',font=fontStyle2,bg="orange Red")
    E17=Entry(nw,width=50,bg='grey25',fg='white')
    L17.pack()
    E17.pack()
    L18=Label(nw,text='Approximate Salary',font=fontStyle2,bg="orange Red")
    E18=Entry(nw,width=50,bg='grey25',fg='white')
    L18.pack()
    E18.pack()
    L19=Label(nw,text='Main Branch Address',font=fontStyle2,bg="orange Red")
    E19=Entry(nw,width=100,bg='grey25',fg='white')
    L19.pack()
    E19.pack()
    L20=Label(nw,text='Company Email Address',font=fontStyle2,bg="orange Red")
    E20=Entry(nw,width=50,bg='grey25',fg='white')
    L20.pack()
    E20.pack()
    L21=Label(nw,text='Phone Number',font=fontStyle2,bg="orange Red")
    E21=Entry(nw,width=50,bg='grey25',fg='white')
    L21.pack()
    E21.pack()
    
    def c5():
        mycon=sq.connect(host="localhost",user="root",passwd="asplasht8",database="records")

        ent11=Entry.get(E11)#reg number
        ent12=Entry.get(E12)#name of company
        naam=ent12.split()

        for x in range (len(naam)):
            cap=naam[x].capitalize()
            cap=cap + " "
            naam[x]=cap
        sp=""
        for y in range (len(naam)):
            sp=sp+naam[y]
        ent12=sp
        ent13=Entry.get(E13)#name of representative
        ent14=Entry.get(E14)#designation of representative
        ent15=Entry.get(E15)#number of employee needed
        ent16=Entry.get(E16)#branch
        ent17=Entry.get(E17)#job location
        ent18=Entry.get(E18)#salary
        ent19=Entry.get(E19)#main branch address
        ent20=Entry.get(E20)#email
        ent20=ent20.lower()
        ent21=Entry.get(E21)#phone
        cursor=mycon.cursor()
        comp="INSERT into company_details(REGISTRATION_NUMBER,NAME_OF_COMPANY,REPRESENTAIVE_NAME,DESIGNATION_OFREPRESENTATIVE,NO_OF_EMPLOYEE_NEEDED,FIELD,JOB_LOCATION,APPROXIMATE_SALARY,MAIN_BRANCH_ADDRRESS,COMPANY_EMAIL,PHONE) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(ent11,ent12,ent13,ent14,ent15,ent16,ent17,ent18,ent19,ent20,ent21)
        cursor.execute(comp)
        mycon.commit()
        out1="SELECT NAME,SKILLS,EMAIL_ID,ADDRESS FROM jobless WHERE MINIMUM_EXPECTED_SALARY<=%s and STATE='%s' and SKILLS='%s'"%(ent18,ent17,ent16,)
        cursor.execute(out1)
        outlab1=cursor.fetchall()
        out2="SELECT NAME,SKILLS,EMAIL_ID,ADDRESS FROM jobless WHERE MINIMUM_EXPECTED_SALARY<=%s and JOB_LOCAL_INTERSTATE='%s' and SKILLS='%s'"%(ent18,'Inter_State',ent16)
        cursor.execute(out2)
        outlab2=cursor.fetchall()
        
        def finout(x):
            #giving final output
            yourData = x
            nw=Tk()
            nw.title("Your Final Output")
            nw.geometry("800x800")
            nw.configure(bg="black")
            labq=Label(nw,text="\n\nYour output is\n\n",bg="black",fg='white')
            labq.pack()
            lab = Label(nw,text=yourData,bg='red',fg='white')
            lab.pack()
            nw.mainloop()

        
        outlab=outlab1+outlab2
        outlab = list(dict.fromkeys(outlab))
        for variable in range(1,((len(outlab)*2)-1),2):
            outlab.insert(variable,"\n\n")
           
        res=finout(outlab)      

    b5=tkinter.Button(nw,text='\nSUBMIT\n',bg='#54FA9B',command=c5)
    b5.pack()


#main program
    
r=tkinter.Tk()
r.geometry("3600x3600")

fontStyle = tkFont.Font(family="Segoe Script",size=50)
fontStyle2 = tkFont.Font(family="Calibri",size=15)
fontStyle3 = tkFont.Font(family="Arial Black",size=20)

main=tkinter.Label(r,text='\nWelcome to\n SKILLED BEROZGAARS PORTAL\n', font=fontStyle,bg="blue",fg='white') #main page
main.pack()
lx=tkinter.Label(r,text="""We are here to serve skilled unemployed people of the country,
so that you can serve the company,
and your company can serve the nation,
TOGETHER WE SERVE THE NATION
THANK YOU""",font=fontStyle3)
lx.pack()

b1=tkinter.Button(r,text='    Next    ',command=c1,font=fontStyle2,bg='white',fg='red')
b1.pack()
r.mainloop()

