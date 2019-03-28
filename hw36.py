from sys import exit

#The second room can have a fairy appear or move on or escape dungeon
def second_room():
    print "You have entered the second room.  Keep going or turn around?"
    next = raw_input(">")
    if "yes" in next:
        t_junction()
    elif "keep going" in next or "yes"in next:
        t_junction()    
    elif "no" in next or "turn around" in next:     
        escape_dungeon()
    else:
        fairy_appears()    
    
#fairy appears can happen throughout.  
def fairy_appears():
    print "*Fairy Appear!*"
    print "Hi.  You look lost.  Want help?"
    response = raw_input(">")
    
    if "yes" in response:
        fairy_help()
    elif "no" in response:
        fairy_leaves("*PBBBFFFTTT. Then Leaves")
    else
        
         
        
def fairy_leaves(why):
    print why
        
def fairy_help():
    print "Do you want to leave?"
    response = raw_input(">")
    if "yes" in response:
        escape_dungeon()
    else :
        fairy_room()    
    

def fairy_room():
    print "You were teleported to a weird room with lots of toys and two doors."
    print "What next?"
    
        
def escape_dungeon():
    print "You have teleported home out of the dungeon."
    
def dead(why):
    print why, "END"
    exit(0)


    
def dungeon_start():
    print "The door slams shut and a Dragon Appears." 
       


def entrance():
    print "Welcome to the dungeon. Would you like to enter?"
    
    next = raw_input(">")
    if next == "yes":
        second_room()
        
    else:
        dungeon_start()
    
    
    
entrance()    
