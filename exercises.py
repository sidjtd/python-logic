#Logic 

#Conditional statements gives us the ability to check conditions and make decisions based on the condition.

#In this exercise, you'll be asked to create conditional statements using if, elif and else.

#1. Declare a variable named weather and assign it a string value of 'rain'. Next create a conditional statement that will check the weather and print 'Bring an umbrella' if weather equals 'rain'.

weather = 'rain'
if(weather == 'rain'):
    print('Bring an umbrella')

#2 Declare a variable named score and assign it a number value of 70. Next create a conditional statement that will check the score and print 'You pass!' if the score is 70 and above and print 'Study harder!' if the score is less than 70.

score = 0
if(score >= 70):
    print('You pass!')
else:
    print('Study harder!')

#3. Declare a variable named download_speed and assign it a data value of 50. Next create a conditional statement that will check the download speed and print the following based on the condition:

# <= 50 'Basic Package'
# <=100 'Premium Package'
# >100 'Platinum Package'

download_speed = 50

if(download_speed <= 50):
    print('Basic Package')
elif(download_speed <= 100):
    print('Premium Package')
else:
    print('Platinum Package')

 #4 Function - check_password
 #Create a function named check_password which will take a parameter password.

 #The function will return true if the input passed into the function is equal to 'qwerty'. Declare a variable named login_result and print your result.

def check_password(password):
    if(password == 'qwerty'):
        return True
check_password('qwerty')

login_result = check_password('qwerty')
print(login_result)



