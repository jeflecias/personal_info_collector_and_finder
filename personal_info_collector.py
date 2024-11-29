# program asks the user to input their personal info
# saves the info into a text file

# this stores the information of multiple people
people_array = []

#keeps the while loop running
cont_1 = "yes"
while cont_1 == "yes":
    # ask the user for their info!!!!
    name = input("What is your name? ")
    age = input("What is your age? ")
    birthday = input("When is your birthday? ")
    blood_type = input("What is your blood type? ")
    criminal_record = input("Do you have a criminal record? ")
    people_array.append([name,age,birthday,blood_type,criminal_record])
    cont_1 = input("Would you like to input another person? yes/no ")

#write file
with open("list_of_people.txt","w") as file:
    for i in people_array:
        for b in i:
            file.write(b + "\n")
        file.write("-----------------------------------------\n")

