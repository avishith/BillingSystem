from tkinter import *
import math, random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title('Billing Software')
        bgcolor='#074463'
        title=Label(self.root,text="Billing software",fg='white',bd=12,bg=bgcolor,relief=GROOVE,font=('times new roman',30,'bold'),pady=2).pack(fill=X)
    #====cosmetic variabls====
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.loashan=IntVar()
        self.hairc=IntVar()
        self.gel=IntVar()
        
    #====Grocery variabls====   
        self.rice=IntVar()
        self.oil=IntVar()
        self.wheat=IntVar()
        self.daal=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
    #====cooldrinks variabls====
        self.maza=IntVar()
        self.frooti=IntVar()
        self.thumbsUP=IntVar()
        self.sprite=IntVar()
        self.Up=IntVar()
        self.mountaindew=IntVar()
    #====total price===
        self.cosmeticPrice=StringVar()
        self.groceryPrice=StringVar()
        self.cooldrinksPrice=StringVar()
    #====total price===
        self.cosmetictax=StringVar()
        self.grocerytax=StringVar()
        self.cooldrinkstax=StringVar()
    #====customer===
        self.cusName=StringVar() 
        self.cusNum=StringVar()

        self.billNO=StringVar()
        x=random.randint(1000,9999)
        self.billNO.set(str(x))
    


        





    #=======CUstomer details+======
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=('times new roman',15,'bold'),fg='gold',bg=bgcolor)
        F1.place(x=0,y=80,relwidth=1)

        cusName=Label(F1,text="Customer Name",bg=bgcolor,fg="white",font=('times new roman',18,'bold')).grid(row=0,column=0,padx=20,pady=5)
        cusNametxt=Entry(F1,width=15,textvariable=self.cusName,bd=7,relief=SUNKEN,font=('times new roman',15)).grid(row=0,column=1,padx=10,pady=5)

        cusNum=Label(F1,text="Phone No",bg=bgcolor,fg="white",font=('times new roman',18,'bold')).grid(row=0,column=2,padx=20,pady=5)
        cusNumtxt=Entry(F1,width=15,textvariable=self.cusNum,bd=7,relief=SUNKEN,font=('times new roman',15)).grid(row=0,column=3,padx=10,pady=5)

        cusbill=Label(F1,text="Bill Number",bg=bgcolor,fg="white",font=('times new roman',18,'bold')).grid(row=0,column=4,padx=20,pady=5)
        cusbilltxt=Entry(F1,width=15,textvariable=self.billNO,bd=7,relief=SUNKEN,font=('times new roman',15)).grid(row=0,column=5,padx=10,pady=5)
        
        Search_btn=Button(F1,width=10,bd=7,command=self.findBill,text="Search",font=('times new roman',12,'bold')).grid(row=0,column=6,pady=10,padx=10)
    #=======Cosmetic Frame======
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cousmetics",font=('times new roman',15,'bold'),fg='gold',bg=bgcolor)
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath soap",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_txt=Entry(F2,width=10,textvariable=self.soap,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=0,column=1,padx=10,pady=10)

        faceCream_lbl=Label(F2,text="FaceCream",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        faceCream_txt=Entry(F2,width=10,textvariable=self.face_cream,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=1,column=1,padx=10,pady=10)

        FaceWash_lbl=Label(F2,text="Face Wash",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        Facewash_txt=Entry(F2,width=10,bd=5,textvariable=self.face_wash,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=2,column=1,padx=10,pady=10)

        body_lbl=Label(F2,text="Body Loshan",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        bath_txt=Entry(F2,width=10,bd=5,textvariable=self.loashan,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=3,column=1,padx=10,pady=10)

        HairC_lbl=Label(F2,text="Hair Cream",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        Hair_txt=Entry(F2,width=10,bd=5,textvariable=self.hairc,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=4,column=1,padx=10,pady=10)

        HairG_lbl=Label(F2,text="Hair Gel",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        HairG_txt=Entry(F2,width=10,bd=5,textvariable=self.gel,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=5,column=1,padx=10,pady=10)

        #=======Grocery Frame======
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=('times new roman',15,'bold'),fg='gold',bg=bgcolor)
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        g2_txt=Entry(F3,width=10,textvariable=self.rice,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=0,column=1,padx=10,pady=10)

        g2_lbl=Label(F3,text="oil",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        g2_txt=Entry(F3,width=10,bd=5,textvariable=self.oil,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=1,column=1,padx=10,pady=10)

        g3_lbl=Label(F3,text="wheat",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        g3_txt=Entry(F3,width=10,bd=5,textvariable=self.wheat,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=2,column=1,padx=10,pady=10)

        g4_lbl=Label(F3,text="Daal",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        g4_txt=Entry(F3,width=10,bd=5,textvariable=self.daal,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=3,column=1,padx=10,pady=10)

        g5_lbl=Label(F3,text="sugar",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        g5_txt=Entry(F3,width=10,bd=5,textvariable=self.sugar,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=4,column=1,padx=10,pady=10)

        g6_lbl=Label(F3,text="Tea",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        g6_txt=Entry(F3,width=10,textvariable=self.tea,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=5,column=1,padx=10,pady=10)
        
        #=======cool drinksFrame======
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cool drinks",font=('times new roman',15,'bold'),fg='gold',bg=bgcolor)
        F4.place(x=670,y=180,width=325,height=380)

        c1_lbl=Label(F4,text="Maza",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=0,column=0,padx=10,pady=10,sticky='w')
        c1_txt=Entry(F4,width=10,textvariable=self.maza,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=0,column=1,padx=10,pady=10)

        c2_lbl=Label(F4,text="Frooti",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=1,column=0,padx=10,pady=10,sticky='w')
        c2_txt=Entry(F4,width=10,textvariable=self.frooti,bd=5,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=1,column=1,padx=10,pady=10)

        c3_lbl=Label(F4,text="ThumbsUP",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=2,column=0,padx=10,pady=10,sticky='w')
        c3_txt=Entry(F4,width=10,bd=5,textvariable=self.thumbsUP,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=2,column=1,padx=10,pady=10)

        c4_lbl=Label(F4,text="Sprite",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=3,column=0,padx=10,pady=10,sticky='w')
        c4_txt=Entry(F4,width=10,bd=5,textvariable=self.sprite,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=3,column=1,padx=10,pady=10)

        c5_lbl=Label(F4,text="7 UP",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=4,column=0,padx=10,pady=10,sticky='w')
        c5_txt=Entry(F4,width=10,bd=5,textvariable=self.Up,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=4,column=1,padx=10,pady=10)

        c6_lbl=Label(F4,text="mountain dew",bg=bgcolor,fg="lightgreen",font=('times new roman',16,'bold')).grid(row=5,column=0,padx=10,pady=10,sticky='w')
        c6_txt=Entry(F4,width=10,bd=5,textvariable=self.mountaindew,relief=SUNKEN,font=('times new roman',16,'bold')).grid(row=5,column=1,padx=10,pady=10)
        
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
        m1entry=Entry(F6,width=18,bd=7,textvariable=self.cosmeticPrice,relief=SUNKEN,font=('arial',10,'bold')).grid(row=0,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Grocery Price",bg=bgcolor,fg="white",font=('times new roman',14,'bold')).grid(row=1,column=0,padx=20,pady=1,sticky='w')
        m2entry=Entry(F6,width=18,bd=7,textvariable=self.groceryPrice,relief=SUNKEN,font=('arial',10,'bold')).grid(row=1,column=1,padx=10,pady=1)

        m2=Label(F6,text="Total Cooldrinks Price",bg=bgcolor,fg="white",font=('times new roman',14,'bold')).grid(row=2,column=0,padx=20,pady=1,sticky='w')
        m2entry=Entry(F6,width=18,textvariable=self.cooldrinksPrice,bd=7,relief=SUNKEN,font=('arial',10,'bold')).grid(row=2,column=1,padx=10,pady=1)

        T1=Label(F6,text="Cosmetic Tax",bg=bgcolor,fg="white",font=('times new roman',14,'bold')).grid(row=0,column=2,padx=20,pady=1,sticky='w')
        T1entry=Entry(F6,width=18,bd=7,textvariable=self.cosmetictax,relief=SUNKEN,font=('arial',10,'bold')).grid(row=0,column=3,padx=10,pady=1)

        T2=Label(F6,text="Grocery Tax",bg=bgcolor,fg="white",font=('times new roman',14,'bold')).grid(row=1,column=2,padx=20,pady=1,sticky='w')
        T2entry=Entry(F6,width=18,textvariable=self.grocerytax,bd=7,relief=SUNKEN,font=('arial',10,'bold')).grid(row=1,column=3,padx=10,pady=1)

        T2=Label(F6,text="Cooldrinks Tax",bg=bgcolor,fg="white",font=('times new roman',14,'bold')).grid(row=2,column=2,padx=20,pady=1,sticky='w')
        T2entry=Entry(F6,textvariable=self.cooldrinkstax,width=18,bd=7,relief=SUNKEN,font=('arial',10,'bold')).grid(row=2,column=3,padx=10,pady=1)

        btn1=Frame(F6,bd=7,relief=GROOVE)
        btn1.place(x=750,width=580,height=105)

        total_btn=Button(btn1,command=self.total,text='Total',bg='cadetblue',fg='black',font=('arial',15,'bold'),pady=15,width=9).grid(row=0,column=0,padx=5,pady=5)
        gen_btn=Button(btn1,text='Genrate bill',command=self.billArea,bg='cadetblue',fg='black',font=('arial',15,'bold'),pady=15,width=9).grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn1,text='clear',command=self.clearData,bg='cadetblue',fg='black',font=('arial',15,'bold'),pady=15,width=9).grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn1,text='Exit',bg='cadetblue',command=self.Exit,fg='black',font=('arial',15,'bold'),pady=15,width=9).grid(row=0,column=3,padx=5,pady=5)
        self.welcome()
    def total(self):
        
        self.c_soap=self.soap.get()*40
        self.c_fcream=self.face_cream.get()*40
        self.c_Bloashan=self.loashan.get()*40
        self.c_fwash=self.face_wash.get()*40
        self.c_gel=self.gel.get()*40
        self.c_hairc=self.hairc.get()*40

        self.TcosmeticPrice=float(
            self.c_soap+
            self.c_fcream+
            self.c_Bloashan+
            self.c_fwash+
            self.c_gel+
            self.c_hairc
            )
        self.cosmeticPrice.set('Rs.'+str(self.TcosmeticPrice))
        self.Ctax=self.TcosmeticPrice*0.05
        self.cosmetictax.set('Rs.'+str(self.Ctax))

        self.G_rice=self.rice.get()*40
        self.G_oil=self.oil.get()*40
        self.G_wheat=self.wheat.get()*40
        self.G_daal=self.daal.get()*40
        self.G_sugar=self.sugar.get()*40
        self.G_tea=self.tea.get()*40



        self.TGroceryPrice=float(
            self.G_rice+
            self.G_oil+
            self.G_wheat+
            self.G_daal+
            self.G_sugar
            )
        self.groceryPrice.set('Rs.'+str(self.TGroceryPrice))
        self.Gtax=self.TGroceryPrice*0.05
        self.grocerytax.set('Rs.'+str(self.Gtax))

        

    
        self.D_frooti=self.frooti.get()*40
        self.D_thumbsUP =self.thumbsUP.get()*45
        self.D_sprite=self.sprite.get()*35
        self.D_Up=self.Up.get()*35
        self.D_mountaindew=self.mountaindew.get()*45
        self.D_maza=self.maza.get()*35

        self.TcooldrinksPrice=float(
            self.D_frooti+
            self.D_thumbsUP+
            self.D_sprite+
            self.D_Up+
            self.D_mountaindew+
            self.D_maza
        )    
        self.cooldrinksPrice.set('Rs.'+str(self.TcooldrinksPrice))
        self.Dtax=self.TcooldrinksPrice*0.05
        self.cooldrinkstax.set('Rs.'+str(self.Dtax))
    def welcome(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t WELCOME TO STORE\n")
        self.txtarea.insert(END,f"\n Bill no :{self.billNO.get()}")
        self.txtarea.insert(END,f"\n customer name: {self.cusName.get()}")
        self.txtarea.insert(END,f"\n phone no: {self.cusNum.get()}")
        self.txtarea.insert(END,f"\n============================")
        self.txtarea.insert(END,f"\nitems\t   QTY\t      Price")
        self.txtarea.insert(END,f"\n============================")

    def billArea(self):
        if self.cusName.get()=="" or self.cusNum.get()=="":
            messagebox.showerror("Error","Fill customer details") 
        elif self.cosmeticPrice.get()=="Rs.0.0" and self.cooldrinksPrice.get()=="Rs.0.0" and self.groceryPrice.get()=="Rs.0.0":
            messagebox.showerror("Error","No items purchased")
               
        else:
            self.welcome()
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\nBathsoap\t   {self.soap.get()}\t      {self.c_soap}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\nF.cream\t    {self.face_cream.get()}\t      {self.c_fcream}")
            if self.loashan.get()!=0:
                self.txtarea.insert(END,f"\nB.loshan\t   {self.loashan.get()}\t      {self.c_Bloashan}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\nF.wash\t    {self.face_wash.get()}\t      {self.c_fwash}")
            if self.gel.get()!=0:
                self.txtarea.insert(END,f"\nGel\t    {self.gel.get()}\t      {self.c_gel}")
            if self.hairc.get()!=0:
                self.txtarea.insert(END,f"\nH.cream\t    {self.hairc.get()}\t      {self.c_hairc}")
            #grocery
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\nRice\t    {self.rice.get()}\t      {self.G_rice}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\nWheat\t    {self.wheat.get()}\t      {self.G_wheat}")
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\nDaal\t    {self.daal.get()}\t      {self.G_daal}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\nF.Sugar\t    {self.sugar.get()}\t      {self.G_sugar}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\nTea\t    {self.tea.get()}\t      {self.G_tea}")
            if self.oil.get()!=0:
                self.txtarea.insert(END,f"\nOil\t    {self.oil.get()}\t      {self.G_oil}")
            #cooldrinks
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\nMaza\t    {self.maza.get()}\t      {self.D_maza}")
            if self.Up.get()!=0:
                self.txtarea.insert(END,f"\n7Up\t    {self.Up.get()}\t      {self.D_Up}")
            if self.thumbsUP.get()!=0:
                self.txtarea.insert(END,f"\nThumbsUP\t   {self.thumbsUP.get()}\t      {self.D_thumbsUP}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\nFrooti\t    {self.frooti.get()}\t      {self.D_frooti}")
            if self.mountaindew.get()!=0:
                self.txtarea.insert(END,f"\nMountaindew\t{self.mountaindew.get()}\t      {self.D_mountaindew}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\nSprite\t    {self.sprite.get()}\t      {self.D_sprite}")
            if self.Dtax+self.Gtax+self.Ctax+self.TcooldrinksPrice+self.TcosmeticPrice+self.TGroceryPrice !=0:
                self.txtarea.insert(END,f"\n____________________________")        
                if self.Ctax!=0:
                    self.txtarea.insert(END,f"\n Cosmetic tax {self.Ctax}")
                if self.Gtax!=0:
                    self.txtarea.insert(END,f"\n Grocery tax  {self.Gtax}")
                if self.Dtax!=0:
                    self.txtarea.insert(END,f"\n Drinks tax   {self.Dtax}")
                self.txtarea.insert(END,f"\n____________________________")
                self.txtarea.insert(END,f"\n Total        Rs.{self.Dtax+self.Gtax+self.Ctax+self.TcooldrinksPrice+self.TcosmeticPrice+self.TGroceryPrice}")
                self.saveBill()
    def saveBill(self):
        bill=messagebox.askyesno('Save bill','Do you want to save bill?')
        if bill>0:
            self.billData= self.txtarea.get("1.0",END)
            txt=open('Bills/'+str(self.billNO.get())+".txt","w")
            txt.write(self.billData)
            txt.close()
        else:
            return   
    def findBill(self):
        lenOfBill=1
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.billNO.get():
                lenOfBill=len(os.listdir("Bills/"))
                txt=open(f'Bills/{i}',"r")
                self.txtarea.delete('1.0',END)
                for d in txt:
                    self.txtarea.insert(END,d)
                txt.close()
            lenOfBill+=1
                
            print(lenOfBill)   
            if lenOfBill==len(os.listdir("Bills/")):

                messagebox.showerror("fileError","BILL not found")
    def clearData(self):
    #====cosmetic variabls====
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.loashan.set(0)
        self.hairc.set(0)
        self.gel.set(0)
        
    #====Grocery variabls====   
        self.rice.set(0)
        self.oil.set(0)
        self.wheat.set(0)
        self.daal.set(0)
        self.sugar.set(0)
        self.tea.set(0)
    #====cooldrinks variabls====
        self.maza.set(0)
        self.frooti.set(0)
        self.thumbsUP.set(0)
        self.sprite.set(0)
        self.Up.set(0)
        self.mountaindew.set(0)
    #====total price===
        self.cosmeticPrice.set(0)
        self.groceryPrice.set(0)
        self.cooldrinksPrice.set(0)
    #====total price===
        self.cosmetictax.set(0)
        self.grocerytax.set(0)
        self.cooldrinkstax.set(0)
    #====customer===
        self.cusName.set("") 
        self.cusNum.set("") 

        self.billNO.set('')
        x=random.randint(1000,9999)
        self.billNO.set(str(x))
        self.welcome()
    def Exit(self):
        app=messagebox.askyesno('exit',"Do you really want to exit..?")

        if app>0 :
            self.root.destroy()


    


                                                          
root = Tk()
obj=Bill_App(root)
root.mainloop()
