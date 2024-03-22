#Simple quest: 
#    Main idea is:
#
#step 1 - Creatae a Club (done)
#   1.1 - Using inshave
#       1.1.1 - Propertys:
#               Name: inshave/ ItemID: 0x10E6/ hue:0
#               
#    
#Step 2 - Check club Property to see if its Slayer
#   2.1 text for slayer wepons:
#            'You have successfully crafted a slayer wepon.'
#            'You have received a club in your backpack'
#   2.2 Club Property:
#       Name:Club/ ID:0x13B4
#Step 3 - Sort it out
#   3.1 - Slayer wep in hand
#   3.2 - normal wep in trash
#
#
# Board ID: 0x1BD7
# Logs ID: 0x1BDD

inshave = 0x10E6 #tool to be used
clubId = 0x13B4 # item do be sorted
trashCan = 0x4197E41B #south on the crafting area trash
backpackGood = 0x409C8AAC #Backpack inside Beetle
beetle = 0x000105ED #beetle id
self = 0x0006B323 #char ID
selfBackpack = 0x40FF6A42   #own backpack id
woodQuant = Items.BackpackCount(0x1BDD,-1) + Items.BackpackCount(0x1BD7,-1)


def createClub():
    Items.UseItemByID(inshave,0)
    #too fast got to pause before action
    Misc.Pause(500)
    Gumps.SendAction( 949095101 ,21) #gump id found with the Inspect Gumps button this one is the "make last" button
    Misc.Pause(1500)
    
    
    
    
    
def sortClub():
    
    if Journal.SearchByType('You have successfully crafted a slayer', 'System'):
       Gumps.SendAction(949095101,0)
       club = Items.FindByID(clubId,-1,selfBackpack,-1,0) #using de id of the item to get serial
       Mobiles.UseMobile(self)
       Misc.Pause(500)
       Items.Move(club,backpackGood,1)
       Misc.Pause(500)
       Mobiles.UseMobile(beetle)
       Journal.Clear()
       Misc.Pause(1500)
    else:
       club = Items.FindByID(clubId,-1,selfBackpack,-1,0) #using de id of the item to get serial
       Items.Move(club,trashCan,1)
    
    
def main():    
    createClub()
    Misc.Pause(500)
    sortClub()
    Misc.Pause(500)
    
Journal.Clear()
    
while woodQuant >= 10:
    main()
