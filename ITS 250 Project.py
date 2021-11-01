###the following program is something that can be used to help students study.\
###The program will work by calculating how many hours a certain student should study given the difficulty\
###and the current grade within that class. The results should produce variying results that will help the student\
###better achieve a good grade in each of their classes.
#Noah wrote this.

###if a student takes simpleCourse then his or her study time should be the longest. 
###if a student takes moderateCourse then his or her study time should take less time.
###if a student takes difficultCourse then his or her study time should take fastest.
#Samantha wrote this.

#Pseudocode.\
#Input the constant number of hours a student should study for a course.
#Input the level of course rigor.
#Calculate the number of hours a student should study for a course depending on the level of course rigor.
#Display the number of hours a student should study for a course.
#Samantha wrote this.

#The basic_study_time indicates the minimal study time a student should study for each course, regardless of rigor.')
#Samantha wrote this.
print('Enter the variable, basic_study_time')
#costant study time, regardless of course rigor, with given variables.
#Samantha wrote this.
basic_study_time = 1
if basic_study_time == 1:
    print('This is the minimal study time a student should study for a course, regardless of rigor.')
else:
    print('Incorrect, miminal study time must be 1.')
simpleCourse = 2 
#represents lowest level of course rigor using assignment operator.
#Samantha wrote this.
moderateCourse = 3
#represents moderate level of course rigor using assignment operator.
#Samantha wrote this.
difficultCourse = 4 
#represent highest level of course rigor using assignment operator.
#Samantha wrote this.

study_time_for_simpleCourse = (basic_study_time + simpleCourse)
study_time_for_moderateCourse = (basic_study_time + moderateCourse)
study_time_for_difficultCourse = (basic_study_time + difficultCourse)

#results in Boolean expression
#Samantha wrote this.
simpleCourse <= moderateCourse and moderateCourse > simpleCourse

maxStudy = 5
while maxStudy > 10:
    print('take a break.')

#Ending limit.
#Samantha wrote this.
##for end in range (5):
##    end = int(input('maxStudy: '))

