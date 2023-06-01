user = int(input("How many sides does it have? \n>>> "))
shape = input("What is the face's/side's' shape? \n>>> ")
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
else:
    print("Its not an regular polyhedra.")
