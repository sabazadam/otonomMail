#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

startingLetter = ""
nameList = ""
nameArray = []
with open("Input/Names/invited_names.txt", "r") as name:
    nameFile = name.readlines()
    for i in nameFile:
        nameArray.append(i.replace("\n",""))
print(nameArray)
with open("Input/Letters/starting_letter.txt") as file:
    startingLetter = file.read()
    #startingLetter = startingLetter.replace("[name]", "Kero")
    for name in nameArray:
        newFile = open(f"Output/ReadyToSend/letter_to_{name}", "w")
        newFile.write(startingLetter.replace("[name]", name))
        newFile.close()
