import os 
library={}
def clear():
  os.system("cls") if os.name=="nt" else ("clear")

print("welcome to library catalog...")
print("_____________________________")
while True:
   print("menu...")
   print("________")
   print("1- add book ")
   print("2- check out book ")
   print("3- check in back")
   print("4- list books  ")
   print("5- exit ")
   number=int(input("enter your choies number from 1-5 "))

# add_book():
   if number== 1:
      while True:
        clear()
        isbn=input("enter the ISBN for book:")  
        title=input("enter a title : ")
        author=input("enter a author : ")
        if isbn not in library:
           print(f"the book: {title} added was successflly by author: {author}  and ISBN: {isbn}")
           library[isbn]={"title " : title, 
                   "author" : author,
                   "available" : True ,}
        else:
           print(F"that's ISBN: {isbn} in the library .try again..")
        choice=input("Do you want add onther book? (yes/no) ")
        if choice.lower()== "no":
         break
    
 #check_out_book():
   elif number== 2:
      while True:
        clear()
        isbn=input("enter ISBN check out :  ")
        if isbn in library:
          if library[isbn]["available"]:
            print(f"the book {title} is successflly, ISBN: {isbn}")
            library[isbn]["available"]= False
          else:    
           print(" thats book not available ...")
        else:
          print("not found ....try again.")
        choice=input("Do you want check out onther book? (yes/no) ")
        if choice.lower() ==   "no" :
          break  
        
# check_in_book():    
   elif number== 3:     
      while True:
       clear()
       isbn=input("enter ISBN check in :  ")
       if isbn in library:
          if not library[isbn]["available"]:
             library[isbn]["available"]= True
             print(f"the book:*** {title} *** successflly in back ")
          else :
             print(f"that's book {title} in the library ") 
       else:
          print("that's not found ,...try again")
       choice=input("do you want check in back onther book? (yes/no)")        
       if choice.lower()=="no":
          break   

#list_books()
   elif number== 4:
     while True:
       clear()
       print("library catalog:  ")
       print("_________________")
       print(library)
       choice=input("do you want to go back to main menu ? (yes/ no)")
       if choice.lower()=="no":
         break
         
#exit()
   elif number== 5:
     clear()
     print("thanks for uesing.....EXITING.....")
     break
   else:
     print(" that's anviled choice ..")


        