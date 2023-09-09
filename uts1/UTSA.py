def printList():
    print ("""
KTV Keluarga Penyanyi
Pop - "Uptown Funk" by Mark Ronson ft. Bruno Mars   Rp 1000
Hip-hop - "Jump" by Kris Kross                      Rp 1000
Country - "Friends in Low Places" by Garth Brooks   Rp 1000
Rock - "Livin' on a Prayer" by Bon Jovi             Rp 1000
Disco - "Stayin' Alive" by Bee Gees                 Rp 1000
R&B - "I Will Always Love You" by Whitney Houston   Rp 1000
Input 0 when you're done!
           """)
    0
def checkSongPrice(song):
    if (song==1):
        return 1000
    elif (song==2):
        return 1000
    elif (song==3):
        return 1000
    elif (song==4):
        return 1000
    elif (song==5):
        return 1000
    elif (song==6):
        return 1000
    else:
        print ("Invalid input! Please input the valid option (1-6)")
        return 0

printList()
total=0
while (True) :
    choice=int(input("Please input your choice! (1-6) :"))
    if (choice==0):
        break
    else :
        price=checkSongPrice(choice)
        total=total+price
        print("Current total cost is Rp ", total)
        
print("Total cost : Rp ",total)
while (True) :
    payment=int(input("Please input the amount of money for payment! :"))
    change=payment-total
    print ("Change : Rp ",change)
    if (payment>=total) :
        print ("Thank you for your purchase! enjoy your karaoke experience!")
        break
    else :
        print ("invalid payment amount! Please make sure that the payment amount is sufficient")