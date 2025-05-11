from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math
root=Tk()
root.title("Grocery Billing Machine")
root.geometry("1300x700")
def reset():
 entry1.delete(0,END)
 entry1.insert(0, 0)
 entry2.delete(0,END)
 entry2.insert(0, 0)
 entry3.delete(0,END)
 entry3.insert(0, 0)
 entry4.delete(0,END)
 entry4.insert(0, 0)
 entry5.delete(0,END)
 entry5.insert(0, 0)
 entry6.delete(0, END)
 entry6.insert(0, 0)
 entry7.delete(0, END)
 entry7.insert(0, 0)
 entry8.delete(0, END)
 entry8.insert(0, 0)
 entry9.delete(0, END)
 entry9.insert(0, 0)
 entry10.delete(0, END)
 entry10.insert(0, 0)
 entry11.delete(0,END)
 entry11.insert(0, 0)
 entry12.delete(0,END)
 entry12.insert(0, 0)
 entry13.delete(0,END)
 entry13.insert(0, 0)
 entry14.delete(0,END)
 entry14.insert(0, 0)
 entry15.delete(0,END)
 entry15.insert(0, 0)
 entry16.delete(0, END)
 entry16.insert(0, 0)
 entry17.delete(0, END)
 entry17.insert(0, 0)
 entry18.delete(0, END)
 entry18.insert(0, 0)
 entry19.delete(0, END)
 entry19.insert(0, 0)
 entry20.delete(0, END)
 entry20.insert(0, 0)
 entry21.delete(0,END)
 entry21.insert(0, 0)
 entry22.delete(0,END)
 entry22.insert(0, 0)
 entry23.delete(0,END)
 entry23.insert(0, 0)
 entry24.delete(0,END)
 entry24.insert(0, 0)
 entry25.delete(0,END)
 entry25.insert(0, 0)
 entry26.delete(0, END)
 entry26.insert(0, 0)
 entry27.delete(0, END)
 entry27.insert(0, 0)
 entry28.delete(0, END)
 entry28.insert(0, 0)
 entry29.delete(0, END)
 entry29.insert(0, 0)
 entry30.delete(0, END)
 entry30.insert(0, 0)
 entry31.delete(0,END)
def product_1():
 apple_amount = float(entry1.get())*0.12
 banana_amount = float(entry2.get())*60
 mango_amount = float(entry3.get())*0.15
 pineapple_amount = float(entry4.get())*0.060
 greenapple_amount = float(entry5.get())*0.15
 freshfruits_amount = apple_amount + banana_amount + mango_amount + pineapple_amount + greenapple_amount
 onion_amount = float(entry6.get())*0.035
 potato_amount = float(entry7.get())*0.040
 tamoto_amount = float(entry8.get())*0.020
 carrot_amount = float(entry9.get())*0.065
 corn_amount = float(entry10.get())*0.056
 freshvegetables_amount = onion_amount + potato_amount + tamoto_amount + carrot_amount + corn_amount
 chocolates_amount = float(entry11.get()) * 70
 cooldrinks_amount = float(entry12.get()) * 85
 sweets_amount = float(entry13.get()) * 200
 icecreams_amount = float(entry14.get()) * 350
 chips_amount = float(entry15.get()) * 15
 snacks_amount = chocolates_amount + cooldrinks_amount + sweets_amount + icecreams_amount + chips_amount
 salt_amount = float(entry16.get()) * 0.024
 blackpepper_amount = float(entry17.get()) * 0.362
 chillipowder_amount = float(entry18.get()) * 0.326
 sugar_amount = float(entry19.get()) * 0.040
 turmeric_amount = float(entry20.get()) * 0.250
 condiments_amount = salt_amount + blackpepper_amount + chillipowder_amount + sugar_amount + turmeric_amount
 babyhairgrowthoil_amount = float(entry26.get()) * 550
 babysoap_amount = float(entry27.get()) * 398
 babyshampoo_amount = float(entry28.get()) * 575
 babysunscreen_amount = float(entry29.get()) * 599
 babymassageoil_amount = float(entry30.get()) * 475
 baby_care_amount = babyhairgrowthoil_amount + babysoap_amount + babyshampoo_amount + babysunscreen_amount + babymassageoil_amount
 garbage_bags_amount = float(entry21.get())*40
 laundry_soap_amount = float(entry22.get())*30
 dryer_sheets_amount = float(entry23.get())*100
 bleach_amount = float(entry24.get())*40
 dish_soap_amount = float(entry25.get())*20
 household_amount = garbage_bags_amount + laundry_soap_amount + dryer_sheets_amount + bleach_amount + dish_soap_amount
 totalamount=freshfruits_amount + freshvegetables_amount + snacks_amount + condiments_amount + household_amount + baby_care_amount
 billamount=math.ceil(totalamount)
 entry31.insert(0,'Rs '+str(billamount)+' only/-')
def billdesk():
 total_items = {
  'Apple' : math.ceil(float(entry1.get())*0.12),
  'Banana' : math.ceil(float(entry2.get())*60),
  'Mango' : math.ceil(float(entry3.get())*0.15),
  'Pine Apple' : math.ceil(float(entry4.get())*0.060),
  'Green Apple' : math.ceil(float(entry5.get())*0.15),
  'Onion' : math.ceil(float(entry6.get())*0.035),
  'Potato' : math.ceil(float(entry7.get())*0.040),
  'Tomato' : math.ceil(float(entry8.get())*0.020),
  'Carrot' : math.ceil(float(entry9.get())*0.065),
  'Corn' : math.ceil(float(entry10.get())*0.056),
  'Chocolates' : math.ceil(float(entry11.get()) * 70),
  'Cool Drinks' : math.ceil(float(entry12.get()) * 85),
  'Sweets' : math.ceil(float(entry13.get()) * 200),
  'Ice creams' : math.ceil(float(entry14.get()) * 350),
  'Chips' : math.ceil(float(entry15.get()) * 15),
  'Salt' : math.ceil(float(entry16.get()) * 0.024),
  'Black Pepper' : math.ceil(float(entry17.get()) * 0.362),
  'Chilli Powder' : math.ceil(float(entry18.get()) * 0.326),
  'Sugar' : math.ceil(float(entry19.get()) * 0.040),
  'Turmeric' : math.ceil(float(entry20.get()) * 0.250),
  'Baby Hairgrowth Oil' : math.ceil(float(entry26.get()) * 550),
  'Baby Soap' : math.ceil(float(entry27.get()) * 398),
  'Baby Shampoo' : math.ceil(float(entry28.get()) * 575),
  'Baby Sunscreen' : math.ceil(float(entry29.get()) * 599),
  'Baby Massage Oil' : math.ceil(float(entry30.get()) * 475),
  'Garbage Bags' : math.ceil(float(entry21.get())*40),
  'Laundry Soap' : math.ceil(float(entry22.get())*30),
  'Dryer Sheets' : math.ceil(float(entry23.get())*100),
  'Bleach' : math.ceil(float(entry24.get())*40),
  'Dish Soap' : math.ceil(float(entry25.get())*20)
 }
 message = "\n".join([f"{item}: Rs {quantity} only/-" for item, quantity in
 total_items.items()])
 messagebox.showinfo("Bill Details", message)
label_1=Label(root,text="WeLcOmE tO GrOcErY BiLlInG MaChInE",font=("gabriola",50,"bold"),fg='yellow',bg='deeppink',bd=12,relief='groove')
label_1.pack(fill=X)
products=Frame(root)
products.pack()
freshfruits=Label(products,text="FrEsH FrUiTs",font=("times new roman",20,"bold"),fg='limegreen')
freshfruits.grid(row=0,column=0,sticky="w")
weight_freshfruits=Label(products,text="Grams:",font=("gabriola",20,"bold"),fg='black')
weight_freshfruits.grid(row=0,column=1)
apple=Label(products,text="Apple:",font=("courier new",15,"bold"),fg='red')
apple.grid(row=1,column=0,sticky="w")
40
entry1=Entry(products)
entry1.grid(row=1,column=1)
entry1.insert(0,0)
banana=Label(products,text="Banana(per 12 pieces):",font=("courier new",15,"bold"),fg='red')
banana.grid(row=2,column=0,sticky="w")
entry2 = Entry(products)
entry2.grid(row=2,column=1)
entry2.insert(0,0)
mango=Label(products,text="Mango:",font=("courier new",15,"bold"),fg='red')
mango.grid(row=3,column=0,sticky="w")
entry3 = Entry(products)
entry3.grid(row=3, column=1)
entry3.insert(0,0)
pinapple=Label(products,text="Pinapple:",font=("courier new",15,"bold"),fg='red')
pinapple.grid(row=4,column=0,sticky="w")
entry4 = Entry(products)
entry4.grid(row=4, column=1)
entry4.insert(0,0)
greenapple=Label(products,text="Greenapple:",font=("courier new",15,"bold"),fg='red')
greenapple.grid(row=5,column=0,sticky="w")
entry5=Entry(products)
entry5.grid(row=5,column=1)
entry5.insert(0,0)
freshvegetables=Label(products,text="FrEsH vEgEtAbLeS",font=("times new roman",20,"bold"),fg='limegreen')
freshvegetables.grid(row=0,column=2)
weight_freshvegetables=Label(products,text="Grams:",font=("gabriola",20,"bold"),fg='black'
)
weight_freshvegetables.grid(row=0,column=3,sticky="w")
onion=Label(products,text="Onion:",font=("courier new",15,"bold"),fg='red')
onion.grid(row=1,column=2,sticky="w")
entry6=Entry(products)
entry6.grid(row=1,column=3)
41
entry6.insert(0,0)
potato=Label(products,text="Potato:",font=("courier new",15,"bold"),fg='red')
potato.grid(row=2,column=2,sticky="w")
entry7 = Entry(products)
entry7.grid(row=2,column=3)
entry7.insert(0,0)
tamoto=Label(products,text="Tamoto:",font=("courier new",15,"bold"),fg='red')
tamoto.grid(row=3,column=2,sticky="w")
entry8 = Entry(products)
entry8.grid(row=3, column=3)
entry8.insert(0,0)
carrot=Label(products,text="Carrot:",font=("courier new",15,"bold"),fg='red')
carrot.grid(row=4,column=2,sticky="w")
entry9 = Entry(products)
entry9.grid(row=4, column=3)
entry9.insert(0,0)
corn=Label(products,text="Corn:",font=("courier new",15,"bold"),fg='red')
corn.grid(row=5,column=2,sticky="w")
entry10=Entry(products)
entry10.grid(row=5,column=3)
entry10.insert(0,0)
snacks=Label(products,text="SNaCkS",font=("times new roman",20,"bold"),fg='limegreen')
snacks.grid(row=0,column=4,sticky="w")
weight_snacks=Label(products,text="No.of Items:",font=("gabriola",20,"bold"),fg='black')
weight_snacks.grid(row=0,column=5,sticky="w")
chocolates=Label(products,text="Chocolates:",font=("courier new",15,"bold"),fg='red')
chocolates.grid(row=1,column=4,sticky="w")
entry11=Entry(products)
entry11.grid(row=1,column=5)
entry11.insert(0,0)
cooldrinks=Label(products,text="Cooldrinks:",font=("courier new",15,"bold"),fg='red')
cooldrinks.grid(row=2,column=4,sticky="w")
entry12 = Entry(products)
entry12.grid(row=2,column=5)
42
entry12.insert(0,0)
sweets=Label(products,text="Sweets:",font=("courier new",15,"bold"),fg='red')
sweets.grid(row=3,column=4,sticky="w")
entry13 = Entry(products)
entry13.grid(row=3, column=5)
entry13.insert(0,0)
icecreams=Label(products,text="Icecreams:",font=("courier new",15,"bold"),fg='red')
icecreams.grid(row=4,column=4,sticky="w")
entry14 = Entry(products)
entry14.grid(row=4, column=5)
entry14.insert(0,0)
chips=Label(products,text="Chips:",font=("courier new",15,"bold"),fg='red')
chips.grid(row=5,column=4,sticky="w")
entry15=Entry(products)
entry15.grid(row=5,column=5)
entry15.insert(0,0)
condiments=Label(products,text="COnDiMeNtS",font=("times new roman",20,"bold"),fg='limegreen')
condiments.grid(row=6,column=2,sticky="w")
weight_condiments=Label(products,text="Grams:",font=("gabriola",20,"bold"),fg='black')
weight_condiments.grid(row=6,column=3)
salt=Label(products,text="Salt:",font=("courier new",15,"bold"),fg='red')
salt.grid(row=7,column=2,sticky="w")
entry16=Entry(products)
entry16.grid(row=7,column=3)
entry16.insert(0,0)
blackpepper=Label(products,text="Blackpepper:",font=("courier new",15,"bold"),fg='red')
blackpepper.grid(row=8,column=2,sticky="w")
entry17 = Entry(products)
entry17.grid(row=8,column=3)
entry17.insert(0,0)
chillipowder=Label(products,text="Chilli powder:",font=("courier new",15,"bold"),fg='red')
chillipowder.grid(row=9,column=2,sticky="w")
entry18 = Entry(products)
43
entry18.grid(row=9, column=3)
entry18.insert(0,0)
sugar=Label(products,text="Sugar:",font=("courier new",15,"bold"),fg='red')
sugar.grid(row=10,column=2,sticky="w")
entry19 = Entry(products)
entry19.grid(row=10, column=3)
entry19.insert(0,0)
turmeric=Label(products,text="Turmeric:",font=("courier new",15,"bold"),fg='red')
turmeric.grid(row=11,column=2,sticky="w")
entry20=Entry(products)
entry20.grid(row=11,column=3)
entry20.insert(0,0)
household=Label(products,text="HoUsEhOlD",font=("times new roman",20,"bold"),fg='limegreen')
household.grid(row=6,column=0,sticky="w")
weight_household=Label(products,text="No.of Items:",font=("gabriola",20,"bold"),fg='black')
weight_household.grid(row=6,column=1,sticky="w")
garbage_bags=Label(products,text="Garbage Bags:",font=("courier new",15,"bold"),fg='red')
garbage_bags.grid(row=7,column=0,sticky="w")
entry21=Entry(products)
entry21.grid(row=7,column=1)
entry21.insert(0,0)
laundry_soap=Label(products,text="Laundry Soap:",font=("courier new",15,"bold"),fg='red')
laundry_soap.grid(row=8,column=0,sticky="w")
entry22 = Entry(products)
entry22.grid(row=8,column=1)
entry22.insert(0,0)
dryer_sheets=Label(products,text="Dryer Sheets:",font=("courier new",15,"bold"),fg='red')
dryer_sheets.grid(row=9,column=0,sticky="w")
entry23 = Entry(products)
entry23.grid(row=9, column=1)
entry23.insert(0,0)
bleach=Label(products,text="Bleach:",font=("courier new",15,"bold"),fg='red')
44
bleach.grid(row=10,column=0,sticky="w")
entry24 = Entry(products)
entry24.grid(row=10, column=1)
entry24.insert(0,0)
dish_soap=Label(products,text="Dish Soap:",font=("courier new",15,"bold"),fg='red')
dish_soap.grid(row=11,column=0,sticky="w")
entry25=Entry(products)
entry25.grid(row=11,column=1)
entry25.insert(0,0)
baby_care=Label(products,text="BaBy CaRe",font=("times new roman",20,"bold"),fg='limegreen')
baby_care.grid(row=6,column=4,sticky="w")
weight_baby_care=Label(products,text="No.of Items:",font=("gabriola",20,"bold"),fg='black')
weight_baby_care.grid(row=6,column=5,sticky="w")
babyhairgrowthoil=Label(products,text="Baby Hair Growth Oil:",font=("courier new",15,"bold"),fg='red')
babyhairgrowthoil.grid(row=7,column=4,sticky="w")
entry26=Entry(products)
entry26.grid(row=7,column=5)
entry26.insert(0,0)
babysoap=Label(products,text="Baby Soap:",font=("courier new",15,"bold"),fg='red')
babysoap.grid(row=8,column=4,sticky="w")
entry27 = Entry(products)
entry27.grid(row=8,column=5)
entry27.insert(0,0)
babyshampoo=Label(products,text="Baby Shampoo:",font=("courier new",15,"bold"),fg='red')
babyshampoo.grid(row=9,column=4,sticky="w")
entry28 = Entry(products)
entry28.grid(row=9, column=5)
entry28.insert(0,0)
babysunscreen=Label(products,text="Baby Sunscreen:",font=("courier new",15,"bold"),fg='red')
45
babysunscreen.grid(row=10,column=4,sticky="w")
entry29 = Entry(products)
entry29.grid(row=10, column=5)
entry29.insert(0,0)
babymassageoil=Label(products,text="Baby Massage Oil:",font=("courier new",15,"bold"),fg='red')
babymassageoil.grid(row=11,column=4,sticky="w")
entry30=Entry(products)
entry30.grid(row=11,column=5)
entry30.insert(0,0)
label_2=Label(products,bg="black",bd='12',relief='groove')
label_2.grid(row=12,column=2)
amount=Label(label_2,text="Amount:",font=('calibri',20,'bold'),bg='black',fg='purple3')
amount.grid(row=8,column=4,sticky="w")
entry31=Entry(label_2)
entry31.grid(row=8,column=5)
button2=Button(label_2,text='Reset',command=reset,font=('fixedsys',15,'bold'),bg='violet red',fg='yellow')
button2.grid(row=9,column=5)
button1=Button(label_2,text='Proceed',command=product_1,font=('fixedsys',15,'bold'),bg='violet red',fg='yellow')
button1.grid(row=9,column=4)
button3=Button(label_2,text='Bill',command=billdesk,font=('fixedsys',15,'bold'),bg='violet red',fg='yellow')
button3.grid(row=10,column=5)
root.mainloop()
