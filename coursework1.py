import csv
import sys
def program():
    a = input("Planet?:   ").upper()
    print(a)
    DATA_FILE_NAME = "planets.txt"
    Planet_list = []
    Earth = ["EARTH", 127561,1, 149.6]                      
    chosen = []
    with open('planets.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')    
        for row in csv_reader:                              #MAKING LIST SO USER ENTERS A PLANET IN THE FILE
            Planet_list.append(row[0])                                                        #
        while a not in Planet_list:                         # 
            print("not a planet")                           #
            a = input("Planet?:   ").upper()                #
        for row in csv_reader:
            if a  == row[0]:
                print(row)
                chosen.append(row)
    if int(chosen[1]) < 127561:
        print("diameter is less than that of the Earth", int(chosen[1]), "km")
    else:
        print("diameter is more than that of the Earth", int(chosen[1]), "km")
    if int(chosen[2]) < 1:
        print(a, " has less moons that of the earth", int(chosen[2]))
    elif int(chosen[2]) == 1:
        print(a, " has a the same amount of moons than the Earth", int(chosen[2]))
    else:
        print(a, " has more moons than the Earth", int(chosen[2]))
    if int(chosen[3]) < 149.6:
        print(a, " is closer to the sun than the Earth", int(chosen[3]))
    else:
        print(a, " is further from the sun than us", int(chosen[3]))
answer = input("start? (Y/N)")
if answer == "Y" or "y":
    program()
else:
    print("ok")
            
    """
    for row in csv_file:
        print(row)
    #if current rows 2nd value is equal to input, print that row
        if number == row[1]:
             print (row)
for row in csv_reader:
    if a in row:
        return true
        chosen.append(line)
        print(chosen)
        print(232323)
    else:
        print(1)
#return False
            
# if Planet_list[1] > 127561 print
#diameter = lambda Planet_listPlanet_list[1] >  127561


    for row in csv_reader:        
        planets_dict[row[0]] = {'diameter':row[1],'moons':row[2],'sun_distance':row[3]}
 
Choice = input("Do you want to know about diameter, moons or sun_distance")
while Choice != "diameter" or "moons" or "sun distance":
    print("not a choice")
    break
print(planets_dict[a][Choice])
"""






























"""    
compareplanet = input("what planet would you like to compare to?").upper()
while compareplanet not in Planet_list:
            print("not a planet")

choice = input("what comparison?: \n diameter(1), moons(2), or sun_distance(3)")
while choice != ("1" or "2" or "3"):
    print("not a choice")
    break
print(
"""

"""with open('planets.txt', "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=' ')
    planet_name = column[0]
    diameter = column[1]
    moons = column[2]
    sun_distance = column[3]
    for row in planet_name:
        if planet_name == EARTH:
            print("lj")
        
    next(csv_reader)"""
                               

    





































    


       

