# FILE NAME - triangle_area.py

# NAME: James Hotchkiss
# DATE: 02/24/2025
# BRIEF DESCRIPTION:  
#area equation for python


# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience





########## ENTER YER CODE BELOW THIS LINE ##########
   
height_tri = input('Enter the height of the triangle: ')
base_tri = input('Enter the base of the triangle: ')
findarea = (1/2) * float(base_tri) * float(height_tri)

print(f'The area of your triangle is: {findarea}')
    
    
    
    
    
    
    
########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter the height: 1
Enter the base: 1

The area of the triangle is 0.5

'''



'''

Enter the height: 8
Enter the base: 4

The area of the triangle is 16.0

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is the flow of the program? Which line of code kicks off the process?





2. What was the hardest part of this lab?

Traceback (most recent call last):
  File "c:\Users\james\Downloads\triangle_area.py", line 22, in <module>    
    findarea = .5 * base_tri * hight_tri
               ~~~^~~~~~~~~~
TypeError: can't multiply sequence by non-int of type 'float'

kept having an error stating I couldn't multiply... so i added float to my variables.


'''
