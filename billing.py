from tkinter import *
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title('Billing Software')
        bgcolor='#074463'
        title=Label(self.root,text="Billing software",fg='white',bd=12,bg=bgcolor,relief=GROOVE,font=('times new roman',30,'bold'),pady=2).pack(fill=X)
    #=======CUstomer details+======
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=('times new roman',15,'bold'),fg='gold',bg=bgcolor)
        F1.place(x=0,y=80,relwidth=1)

        cusName=Label(F1,text="Customer Name",bg=bgcolor,fg="white",font=('times new roman',18,'bold')).grid(row=0,column=0,padx=20,pady=5)
        cusNametxt=Entry(F1,width=15,bd=7,relief=SUNKEN,font=('times new roman',15)).grid(row=0,column=1,padx=10,pady=5)

        cusNum=Label(F1,text="Phone No",bg=bgcolor,fg="white",font=('times new roman',18,'bold')).grid(row=0,column=2,padx=20,pady=5)
        cusNumtxt=Entry(F1,width=15,bd=7,relief=SUNKEN,font=('times new roman',15)).grid(row=0,column=3,padx=10,pady=5)

        cusbill=Label(F1,text="Bill Number",bg=bgcolor,fg="white",font=('times new roman',18,'bold')).grid(row=0,column=4,padx=20,pady=5)
        cusbilltxt=Entry(F1,width=15,bd=7,relief=SUNKEN,font=('times new roman',15)).grid(row=0,column=5,padx=10,pady=5)
        
        bill_btn=Button(F1,width=10,bd=7,text="Search",font=('times new roman',12,'bold')).grid(row=0,column=6,pady=10,padx=10)
    #=======CUstomer Frame======
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cousmetics",font=('times new roman',15,'bold'),fg='gold',bg=bgcolor)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath soap",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_txt=Entry(F2,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=0,column=1,padx=10,pady=10)

        faceCream_lbl=Label(F2,text="FaceCream",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        faceCream_txt=Entry(F2,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=1,column=1,padx=10,pady=10)

        FaceWash_lbl=Label(F2,text="Face Wash",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        Facewash_txt=Entry(F2,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=2,column=1,padx=10,pady=10)

        body_lbl=Label(F2,text="Body Loshan",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        bath_txt=Entry(F2,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=3,column=1,padx=10,pady=10)

        HairC_lbl=Label(F2,text="Hair Cream",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        Hair_txt=Entry(F2,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=4,column=1,padx=10,pady=10)

        HairG_lbl=Label(F2,text="Hair Gel",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        HairG_txt=Entry(F2,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=5,column=1,padx=10,pady=10)

        #=======Grocery Frame======
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=('times new roman',15,'bold'),fg='gold',bg=bgcolor)
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        g2_txt=Entry(F3,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="oil",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        g2_txt=Entry(F3,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="wheat",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        g3_txt=Entry(F3,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Daal",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        g4_txt=Entry(F3,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="sugar",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        g5_txt=Entry(F3,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Tea",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        g6_txt=Entry(F3,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=5,column=1,padx=10,pady=10)
        
        #=======cool drinksFrame======
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cool drinks",font=('times new roman',15,'bold'),fg='gold',bg=bgcolor)
        F4.place(x=670,y=180,width=325,height=380)

        c1_lbl=Label(F4,text="Maza",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        c1_txt=Entry(F4,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Frooti",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        c2_txt=Entry(F4,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="ThumbsUP",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        c3_txt=Entry(F4,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(F4,text="Sprite",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        c4_txt=Entry(F4,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(F4,text="7 UP",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        c5_txt=Entry(F4,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl=Label(F4,text="mountain dew",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        c6_txt=Entry(F4,width=10,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=5,column=1,padx=10,pady=10)
        
         #=======bill Frame======
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=270,height=380)
        billTitle=Label(F5,text='Bill Area',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
        scrolY=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrolY.set)
        scrolY.pack(side=RIGHT,fill=Y)
        scrolY.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #======Button Menu======
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=('times new roman',15,'bold'),fg='gold',bg=bgcolor)
        F6.place(x=0,y=560,relwidth=1,height=140)

        m1=Label(F6,text="Total Cosmetic Price",bg=bgcolor,fg="white",font=('times new roman',14,'bold')).grid(row=0,column=0,padx=20,pady=1,sticky='w')
        m1entry=Entry(F6,width=18,bd=7,relief=SUNKEN,font=('arial',10,'bold')).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Grocery Price",bg=bgcolor,fg="white",font=('times new roman',14,'bold')).grid(row=1,column=0,padx=20,pady=1,sticky='w')
        m2entry=Entry(F6,width=18,bd=7,relief=SUNKEN,font=('arial',10,'bold')).grid(row=1,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Cooldrinks Price",bg=bgcolor,fg="white",font=('times new roman',14,'bold')).grid(row=2,column=0,padx=20,pady=1,sticky='w')
        m2entry=Entry(F6,width=18,bd=7,relief=SUNKEN,font=('arial',10,'bold')).grid(row=2,column=1,padx=10,pady=1)

        T1=Label(F6,text="Cosmetic Tax",bg=bgcolor,fg="white",font=('times new roman',14,'bold')).grid(row=0,column=2,padx=20,pady=1,sticky='w')
        T1entry=Entry(F6,width=18,bd=7,relief=SUNKEN,font=('arial',10,'bold')).grid(row=0,column=3,padx=10,pady=1)

        T2=Label(F6,text="Grocery Tax",bg=bgcolor,fg="white",font=('times new roman',14,'bold')).grid(row=1,column=2,padx=20,pady=1,sticky='w')
        T2entry=Entry(F6,width=18,bd=7,relief=SUNKEN,font=('arial',10,'bold')).grid(row=1,column=3,padx=10,pady=1)

        T2=Label(F6,text="Cooldrinks Tax",bg=bgcolor,fg="white",font=('times new roman',14,'bold')).grid(row=2,column=2,padx=20,pady=1,sticky='w')
        T2entry=Entry(F6,width=18,bd=7,relief=SUNKEN,font=('arial',10,'bold')).grid(row=2,column=3,padx=10,pady=1)

        btn1=Frame(F6,bd=7,relief=GROOVE)
        btn1.place(x=750,width=580,height=105)

        total_btn=Button(btn1,text='Total',bg='cadetblue',fg='black',font=('arial',15,'bold'),pady=15,width=9).grid(row=0,column=0,padx=5,pady=5)
        gen_btn=Button(btn1,text='Genrate bill',bg='cadetblue',fg='black',font=('arial',15,'bold'),pady=15,width=9).grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn1,text='clear',bg='cadetblue',fg='black',font=('arial',15,'bold'),pady=15,width=9).grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn1,text='Exit',bg='cadetblue',fg='black',font=('arial',15,'bold'),pady=15,width=9).grid(row=0,column=3,padx=5,pady=5)

root = Tk()
obj=Bill_App(root)
root.mainloop()
