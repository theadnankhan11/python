#1 
print("Welcome to my Computer quiz!")

palying = input("Do you want to play? ")

if palying.lower()  != "yes":
    quit()

print("okey! Let's play :)")
score = 0

answer = input("what does CPU stand for? ")
if  answer.lower() == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("InCorrect!")

    
answer = input("what does GPU stand for? ")
if  answer.lower() == "graphical processing unit":
    print("Correct!")
    score +=1
else:
    print("InCorrect!")

    
answer = input("what does RAM stand for? ")
if  answer.lower() == "random access memory":
    print("Correct!")
    score +=1
else:
    print("InCorrect!")

    
answer = input("what does PSU stand for? ")
if  answer.lower() == "power supply unit":
    print("Correct!")
    score +=1
else:
    print("InCorrect!")

answer = input("what does ROM stand for? ")
if  answer.lower() == "read only memory":
    print("Correct!")
    score +=1
else:
    print("InCorrect!")

print("You got " + str(score) + " questions correct!" )
print("You got " + str((score/5) *100) + "%. " )

    


