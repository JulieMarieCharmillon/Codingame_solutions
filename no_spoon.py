# for node in nodes:
    # print(f"{x1} {y1} {x2} {y2} {x3} {y3}") où x1y1= noeud, x2y2 = voisin de droite, x3y3 = voisin du bas
        
# en input j'ai une chaine de caractère tq "0"=un noeud "."=une cellule vide

width, height = [int(i) for i in input("w,h").split()] # the number of cells on the X axis

tableau=[]
for y in range(height):
    line = input()  # width characters, each either 0 or .
    liste_characters_by_line = [(x, character) for x, character in enumerate(line)]
    tableau.append( liste_characters_by_line)
print(tableau)

# retourner l'élément à partir du tableau:

for y in range(height):
    for x in range(width):
        character = tableau[y][x][1]
        # NODE CASE
        if character == "0":
            x1, y1 = x, y 
            x2,y2, x3, y3 = "a","b","c","d"
            # X2 Y2 :
            X = x+1
            while X < width:
                if tableau[y][X][1] == "0":
                    x2, y2 = X, y
                    break
                else:
                    X += 1
                    if X == width:
                        x2, y2 = -1, -1
            
            # X3 Y3
            Y= y+1
            while Y < height:
                if tableau[Y][x][1] == "0":
                    x3, y3 = x, Y
                    break
                else:
                    Y +=1
                    if Y == height:
                        x3, y3 = -1, -1 

            


            # if x+1 == width:
            #     x2, y2 = -1, -1
            # elif x+1 < width:
            #     if tableau[y][x+1][1] == "0":
            #         x2, y2 = x+1, y
            #     elif tableau[y][x+1][1] == ".":
            #         x2, y2 = -1, -1
            # if y+1 == height:
            #     x3, y3 = -1, -1     
            # elif y+1 < height: # inside tableau
                # if tableau[y+1][x][1] == "0":
                #     x3, y3 = x, y+1
                # elif tableau[y+1][x][1] == ".":
                #     x3, y3 = -1, -1

            print(f"{x1} {y1} {x2} {y2} {x3} {y3}")