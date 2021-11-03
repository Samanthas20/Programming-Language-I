#the following program is something that can be used to help students study.\
#The program will work by calculating how many hours a certain student should study given the difficulty\
#and the current grade within that class. The results should produce variying results that will help the student\
#better acieve a good grade in each of their classes.#

print("The following is a program to help you figure out how much you need to study for a class per week")

#The main piece of this function that will state how much to study for each class.
def program():
  course=input("Name of the course:")
  grade=int(input("Grade in the course:"))
  diff=int(input("Difficulty of the class on a scale of 1-3, 3 being the hardest:",  ))
  print("You have a",grade,"in",course,"which you rated at a level", diff, "difficulty.")
  calc(grade,diff,course)
  
#The base line of hours needed to study based off the grade in the course
def calc(grade,diff,course):
  if grade>=90:
    study=1
  elif 80<=grade<=89:
    study=2
  elif 70<=grade<=79:
    study=3
  elif 60<=grade<=69:
    study=4
  elif grade<60:
    study=5

#The modifier to hours needed to study based off of difficulty in the class
  if diff==3:
    mult=2
  elif diff==2:
    mult=1.5
  else:
    mult=1
  
  print("Therefore, you must study for",(study*mult),"hours a week in your",course,"course.")

#The program is designed for 3 classes in your schedule
program()
program()
program()

#A summation of the total hours needed to study for all classes
#User inputs data from the output of previous function
sum=0
total=int(input("Enter the number of hours you have to study for each class.\
  (enter 0 if you have no more hours to input):"))
while total !=0: 
  sum=sum+total
  total=float(input("Enter the number of hours you have to study for each class.\
     (enter 0 if you have no more hours to input):"))
print("The total number of hours you have to study is",sum)

#A countdown for how many hours left total with advice/motivation
#User inputed data from tha summation output
def countdown():
    hours_left=float(input("How many hours left do you have left to study? "))
    course = [hours_left]
    for hours in course:
        if hours >= 5:
         print("Make sure to take a 30 min break every 2 hours to keep your focus")
        elif hours <= 4:
            print("You're almost finished!)")
        elif hours ==0:
            print("Congrats, you're finished for this week. Go out and have a good time with some friends!")

countdown()
countdown()
countdown()
