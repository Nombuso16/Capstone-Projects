from enum import Flag
from xml.dom import UserDataHandler
 
'''
Feature name:
Username generator
Feature Purpose:
A feature that generates a unique bootcamp username based on a format

1. prompt a user to input Their First Name, Last Name, Campus and the cohort year they are entering.
2. validate user input in the following ways: 
    a. First name and last name name should not contain digits 
    b. Campus should be a valid campus 
    c. Cohort year should be a valid cohort year - a candidate can’t join a cohort in the past 3. 
3. create a function that produces the username from the input provided. 
4. ask the user if the final username is correct
5. Let the user know what the format of the username is and if the final username is correct.
'''




from xml.dom import UserDataHandler

#function of the user_details
#1. prompt a user to input Their First Name, Last Name, Campus and the cohort year they are entering.
def user_details():
    """
    Prompt user input
    """

    #checking if function does not contain any non-alphebetic input
    # validate user input in the following ways:
    #creating a variable and initialising it into a boolean true to test for the validity 
    loop = True
    
    while loop:
        #asking for an input from the user
        first_name = input('Insert your first name').lower()
        
        #using if/else to test if the input entered does not contain any non- alphabetic inputs
        if first_name.isalpha():
            #escape the loop if the 
            loop = False
        
        #testing the else statement as the if statement condition is not met    
        else:
            #printing blank space
            print()
            #printing the error message
            print('Invalid first name')
               
          
            
            
            
                
    #checking if function does not contain any non-alphebetic input
    # validate user input in the following ways:
    #creating a variable and initialising it into a boolean true to test for the validity
    
    a = True
    while a:
        #printing a blank space
        print()
        #asking the user to enter his last name
        last_name = input('Insert your last name').lower()
        
        #testing if the last_name contains any non-alphabetic input
        if last_name.isalpha():
            #escaping the while loop if the last_name does not contain any 
            #non-alphabetic input
            a = False
        
        #testing the else statement as the if statement condition is not met    
        else:
            #printing a blank line
            print()
            #printing an error message
            print('Invalid last name',end="")
        
    #asking the user to enter the cohort year
    #printing an error message
    print()
    #asking for the user to input an interger that is a year
    cohort = int(input('Insert your cohort'))
    #using while loop to validate the year as past cohort year are not needed
    while cohort < 2022:
        #printing an empty line
        print()
        #asking for the user to input an interger that is a year if an invalid year is entered
        cohort = int(input('Insert your cohort'))
        
   
    #asking the user to enter the name of the final campus
    #for outside of while loop accessibility
    final_campus =''
    #using a while loop to check if input entered by the user exists
    while user_campus(final_campus).lower()=='Invalid Campus'.lower():
        print()
        final_campus = input('Insert the campus you will be attending in\n').lower()
        #if I have found the campus then escape the loop
        if user_campus(final_campus).lower()!='Invalid Campus'.lower():
            break
        #if campus not found print error
        else:
            print('Invalid campus',end="")
        # final_campus = input('Insert the campus you will be attending in').lower()
    
    #printing username
    print(create_user_name(first_name, last_name, cohort, final_campus))
    
   
def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    
    #ELO - Last 3 letters of first name (if their name is less than 3 letters you should add the letter O at the end)
    # first_name = first_name[-3:].upper()
    #calling the campus() function to access the campuses name 
    abv_final_campus = user_campus(final_campus)
    #initializing an f_name variable into empty
    f_name = ''
    #initializing an l_name into empty
    l_name = ''
    #testing if the length of the name is equal and greater than 3
    if len(first_name) >= 3  :
        #printing the username if the condition is met
        f_name = first_name[-3:].lower()

    #testing if the length of the name is equal and greater than 3
    elif len(first_name) == 0:
        #returning an error if length of first_name is 0
        return 'Invalid First Name '
    
    else:
        if len(first_name) == 1:
            f_name = first_name[-3:].lower()+ 'oo'
        elif len(first_name) == 2:
            f_name = first_name[-3:].lower()+ 'o'
        
        
    if len(last_name) >= 3  :
        l_name = last_name[:3].lower()

    elif len(last_name) == 0:
        return 'Invalid First Name '

    else:
        if len(last_name) == 1:
            l_name =last_name[:3].lower()+ 'oo' 
        elif len(last_name) == 2:
            l_name = last_name[:3].lower()+ 'o' 
    return f_name+l_name+str(cohort) +abv_final_campus

def user_campus(campus):
    """
    Return valid campus abbreviations
    """

    if campus == 'johannesburg':
        campus = 'JHB'
        
    elif campus == 'cape town':
        campus = 'CPT'

    elif campus == 'durban':
        campus = 'DBN'
        
    elif campus == 'phokeng':
        campus = 'PHO'

    else:
        return 'Invalid Campus'
        
    return campus



if __name__ == '__main__':
    user_details()
    