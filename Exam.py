#                             Exam
#20th February 2023


#intro
print("Good morning students, today we will have a \"Random questions exam.\"")
print("It is out of ten , i begins now and Good luck!")

#Questions

marks = 0
q1 = int(input("Write the year sudan and south sudan got split: "))
if q1 == int(2011):
    print("Correct answer!")
    marks +=1
else:
    print("You are incorrect.")


q2 = str.lower(input("What is the longest river in the world? "))
if q2 == "nile":
    print("Correct answer.")
    marks += 1
else:
    print("Incorrect answer.")

q3 = int(input("How many hearts does an octupus have? "))
if q3 == 3:
    print("Correct answer.")
    marks += 1
else:
    print("Incorrect answer")

q4 = int(input("In what year was Hiroshima bombed? "))
if q4 == 1945:
    print("Correct answers.")
    marks += 1
else:
    print("Incorrect answer.")

q5 = str.lower(input("What is the chemical symbol of silver? "))
if q5 == "ag":
    print("Correct answer")
    marks +=1
else:
    print("Incorrect answer.")

q6 = str.lower(input("Is there meaning in life? Answer with either yes or no: "))
if q6 == "yes" or "no":
    print("Correct answer.")
    marks +=1
else:
    print("Correct answer")
    marks +=1

q7 = str.lower(input("What is the softest mineral in the world? "))          
if q7 == "talc":
    print("Correct answer.")
    marks += 1
else:
    print("Inorrect answer.")

q8 = int(input("How many eyes does a bee have? "))
if q8 == 5:
    print("Correct answer")
    marks +=1
else:
    print("Incorrect answer.")

q9 = str.lower(input("Who was the first woman to win a nobel prize? "))
if q9 == "marie curie":
    print("Correct answer.")
    marks +=1
else:
    print("Incorrect answer.")

q10 = str.lower(input("What is a community of ants called? "))
if q10 == "colony":
    print("Correct answer.")
    marks +=1
elif q10 == "a colony":
    print("Correct answer.")
    marks +=1
else:
    print("Incorrect answer.")


print("You answered " +str(marks)+ " out of 10 questions.\nTotal score = " + str(marks)+"/10")

#Needs a little fixing and polishing
#dont mind the questions please, i ran out of ideas :-)


