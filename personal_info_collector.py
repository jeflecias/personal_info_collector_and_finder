# program asks the user to input their personal info
# saves the info into a text file

# this stores the information of multiple people 
def check_special_char(given):
    spec_char = "0123456789!@#$%^&*()[]{}-=_+;\\/:"
    
    for i in given:
        if i in spec_char:
            return False
    return True

available_btypes = ["A+","A-","B+","B-","AB+","AB-","O"]
yes_no = ["yes","no"]
people_array = []

#keeps the while loop running
cont_1 = "yes"
while cont_1 == "yes":
    # ask the user for their info!!!!
    # ask name
    name = input("What is your name? ")
    while not check_special_char(name):
        name = input("Please enter a valid name! ")

    # ask the user for age
    while True:
        try:
            age = int(input("What is your age? "))
            if age < 0 or age > 110:
                raise
            break
        except:
            print("Please enter a valid age!")
    
    # ask the user for birthmonth
    while True:
        try:
            birthday_month = int(input("When is your birth month? "))
            if birthday_month < 1 or birthday_month > 12:
                raise
            break
        except:
            print("Please enter a valid month!")
    
    # ask the user for birth day
    while True:
        try:
            birth_day = int(input("When is your birth day? "))
            if birth_day < 1 or birth_day > 31:
                raise
            break
        except:
            print("Please enter a valid day!")

    # ask the user for birth year
    while True:
        try:
            birthday_year = int(input("When is your birth year? "))
            if birthday_year < 0 or birthday_year > 2024:
                raise
            break
        except:
            print("Please enter a valid year!")

    # format birthday
    birthday = str(birthday_month) + "/" + str(birth_day) + "/" + str(birthday_year)

    # ask for blood type
    blood_type = input("What is your blood type? ")
    while not blood_type.upper().strip() in available_btypes:
        blood_type = input("Please enter a valid blood type!")
    
    # ask if the user has a criminal record
    criminal_record = input("Do you have a criminal record? yes/no ")
    while not criminal_record.lower().strip() in yes_no:
        criminal_record = input("Do you have a criminal record? yes/no ")

    people_array.append(
        ["Name: " + name,
         "Age: " + str(age),
         "Birthday: " + birthday,
         "Blood type: " + blood_type.upper(),
         "Criminal record: " + criminal_record]
         )

    cont_1 = input("Would you like to input another person? yes/no ")
    while not cont_1.lower().strip() in yes_no:
        cont_1 = input("Would you like to input another person? yes/no ")

#write file
try:
    with open("list_of_people.txt","w") as file:
        for i in people_array:
            for b in i:
                file.write(b + "\n")
            file.write("-----------------------------------------\n")
except:
    print(".txt file does not exist")

