# DIRECTORY VERSION OF polyhedra.py
# Challenged by GEP
sidesdata = {3,6,8,12,20}

shapesdata = {"Triangle","Square","Pentagon"}

user = int(input("How many sides does it have? \n>>> "))

shape = input("What is the face's/side's' shape? \n>>> ")

if user in list(sidesdata) and shape in list(shapesdata):

    if user == 3 and shape == "Triangle":

        print("Is a Tetrahedron")

    elif user == 8 and shape == "Triangle":

        print("Is an Octahedron")

    elif user == 6 and shape == "Square":

        print("Is a Regular Hexahedron (Cube)")

    elif user == 12 and shape == "Pentagon":

       print("Is a Dodecahedron")

    elif user == 20 and shape == "Triangle":

        print("Is an Icosahedron")

if user not in list(sidesdata) and shape not in list(shapesdata):

    print("Its not an regular polyhedra.")
