editing = ["Coreldraw", "Photoshop", "Macromedia"]
for x in editing:
    print(x) 
print()

print (f"Data sblum ditambah : {editing}")
editing.append("Blender")
print ()
print (f"Sesudah ditambah : {editing}")
print()
print("----------------------------------------------------------")
print()
print (f"Data sblum diextend : {editing}")
print()
software = ["Premiere", "Illustrator"]
editing.extend(software)
print (f"Sesudah diextend : {editing}")
print()

print (f"Data sblum diinsert : {editing}")
print()
editing.insert(2, "Premiere Pro")
print ()
print (f"Sesudah diinsert : {editing}")
print()

print()
print(f"Sebelum diclear : {editing}")
print()
editing.clear()
print(f"Sesudah diclear : ")
print()

print(f"Data sblum diremove : {editing}")
print()
editing.remove("Photoshop")
print(f"Sesudah diremove : ")
print()

print (f"Data sblum dihapus dgn pop : {editing}")
print()
editing.pop(3)
print ()
print (f"Sesudah dihapus dgn pop : {editing}")
print()

 = editing.count("cherry")