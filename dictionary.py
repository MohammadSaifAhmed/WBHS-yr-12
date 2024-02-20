

'''
hogwarts = {

    "Harry Potter":"Gryfindor",
    "Ron Weasly":"Gryfindor",
    "Hermoine Granger":"Gryfindor"

}





hogwarts ["james"] = "house 2" 
hogwarts ["Josh"] = "house 4" 
hogwarts ["Justin"] = "house 3" 


hogwarts.update({"Jake" : "house 3"})

print(hogwarts)


new_student = input("What is the new students name?")
new_student_house = input("What is the students house?")


hogwarts [new_student] = new_student_house
hogwarts.update({new_student : new_student_house})
-
print(list(hogwarts.keys()))

print(list(hogwarts.values()))

'''


harry_potter = {
    "Age":"15",
    "Address":"Number 4, Privet Drive",
    "House": "Gryffindor",
    "Subjects":["Transfguration","Charms","Potions","History of Magic","Defence against the dark arts","Astronomy","Herbology"],
    "House points":155

}


print(f"Hello I am {harry_potter['House']} House but I live at {harry_potter['Address']} My favorite subject is {harry_potter['Subjects'][3]} ")



