print("      Hello Friends! ")
print("   What Item do you want to buy???????")
print("   You may Check our Product_List")
product=["Rice","Cereal","Soap","Shampoo","Biscuit","Brush","Chips","Salt","Bodywash"]
catagory=({"Basmati Rice":90,
  "Luit":100,
  "Gouri":85,
  "Gobindovog":79,
  "Golden Silky Rice":26,
  "Bhagar":76,
  "Raw Rice":50},
  {"Arhar Dal":271,
  "Toor Dal":212,
  "Chana Dal":150,
  "Red Masoor Dal":200,
  "Urad Dal":300,
  "Green Moong Dal":200,
  "Mot Matki":240},
{"Fiama Gel Bar":192,
  "Dettol":206,
  "Pears":192,
  "Dove":312,
  "Santoor":132,
  "Savlon":150,
  "Jo Lime Fresh":196,
  "Liril":234,
  "Cinthol":256},
{"Dove":390,
  "Loreal":424,
  "Tresemme":325,
  "kesh_king":135,
  "Himalaya":208,
  "Dabur vatika":190,
  "Pantene":300,
  "Wow":312,
  "Biotique":102},
{"Little heart":13,
  "Parle g gold":100,
  "Horlicks":90,
  "Britannia":30,
  "Hide & Seek":50,
  "Jim jam":32,
  "Choco pic":50,
  "Dark Fantasy":93,
  "Cream Cracker":32,
  "Milk bikis":52,
  "Bourbon":80,
  "Oreo":72,
  "Digestive_Oats_Biscuit":42,
  "Crack & jack":30,
  "Good Day":20
},{"Bamboo toothbrush":225,
  "Oral-b":120,
  "Colgate":84,
  "Calcybrite-zest":266,
  "Park Daniel":219
},{"Lays":40,
  "Kurkure":45,
  "jolochip":199,
  "maxx":10
},{"Black Salt":119,
  "Himalayan pink salt":115,
   "Tata Salt":22,
  "Ashirbad":18
},{"nivea_combo":337,
  "vivel":180,
  "fiama":219,
  "dove":270
})
cart=[]
price=[]
while(1):
  x=input("Any Item do you want to buy? Press- yes /  Press- x to exit")
  if x=="x":

    break
  if x=="yes":
    print("Available products are :")
    for i in product:
      print(i)
    p=input("What product do you want?")
    indx=product.index(p)
    for i,j in catagory[indx].items():
      print(i,":",j)
    item=input("Which type do you want?")
    qnty=int(input("How many product??"))
    cart.append(item)
    price.append(catagory[indx][item]*qnty)
print("____________ INVOICE_____________")

print(cart,price)
total=sum(price)

print("The Total Price is :" ,total)
print("""Go to Cart and Checkout....
      Thank You For Shopping With Us!""")
