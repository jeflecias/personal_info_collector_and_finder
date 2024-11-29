# program finds user then prints out their info
try:
    with open("list_of_people.txt","r") as file:
        entire_txt = file.readlines()
        cont_2 = "yes"
        while cont_2 == "yes":
            if_found = 0
            find_name = input("Who do you wish to seek? ")
            for a,b in enumerate(entire_txt):
                if find_name.strip() in b:
                    if_found += 1
                    for c in range(a,a+5):
                        print(entire_txt[c],end='')
            if if_found == 0:
                print("Name not found!")
            while not cont_2.lower().strip() in ["yes","no"]:
                cont_2 = input("Would you like to seek another person? yes/no ")
except:
    print("An error occured!")