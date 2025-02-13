apprentis = [
        {"nom": "Lea", "x": 1, "y": 10},
        {"nom": "Alya", "x": 3, "y": 10},
        {"nom": "Carl", "x": 2, "y": 9},
        {"nom": "Achile", "x": 2, "y": 11},
        {"nom": "Julia", "x": 18, "y": 10},
        {"nom": "Charles", "x": 21, "y": 10},
        {"nom": "Amir", "x": 19, "y": 9},
        {"nom": "Jade", "x": 19, "y": 11}]
oeufs = [
        {"nom": "Smorn", "x": 4, "y": 4},
        {"nom": "Eorth", "x": 4, "y": 5},
        {"nom": "Parim", "x": 5, "y": 4},
        {"nom": "Romor", "x": 5, "y": 5},
        {"nom": "Kraar", "x": 16, "y": 16},
        {"nom": "Siber", "x": 16, "y": 17},
        {"nom": "Wallr", "x": 17, "y": 16},
        {"nom": "Momie", "x": 17, "y": 17}]


def create_map(lenght,widght,oeufs,apprentis): 
    list_of_eggs=[]
    for oeuf   in   oeufs:
         list_of_eggs.append((oeuf["x"],oeuf["y"]))
   
    list_of_positions=[]
    for apprenti in apprentis:
        list_of_positions.append((apprenti["x"],apprenti["y"])) 

    str=""
    for i in range( 1,  lenght   ):#parcours la premier ligne 
        for j in range(1,  widght):#remplie la premier la ligne
           
           if (i,j)  in list_of_positions :
                str+="🧙"
           elif (i,j) in   list_of_eggs:
                str+="🥚"
           else:
                str+="🟩"

        str+="\n"
    return str

print(create_map(25,25,oeufs,apprentis))




    
 