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
 #Create a function named check_password which takes a parameter password.

 #The function will return true if the password passed into the function is equal to 'qwerty'. Declare a variable named password_result and print your result.

def check_password(password):
    if(password == 'qwerty'):
        return True
check_password('qwerty')

password_result = check_password('qwerty')
print(password_result)

#5 Function check_login
#Create a function named check_login which takes a parameter login.

#The function will print 'Login Success' if the login passed into the function is equal to 'DevLeague' and print 'Re-enter Login' if it doesn't.

def check_login(login):
    if(login == 'DevLeague'):
        print('Login Success')
    else:
        print('Re-enter Login')
check_login('DevLeague')

#6 Function malware_type
#Create a function named malware_type which takes a parameter malware. 

#The function will print the following based on the following conditions:
#if malware is adware: 'Low Threat'
#if malware is virus: 'Do not share files'
#default message 'I hope you backed up your data'

def malware_type(malware):
    if(malware == 'adware'):
        print('Low Threat')
    elif(malware == 'virus'):
        print('Do not share files')
    else:
        print('I hope you backed up your files')
malware_type('trojan')

#7 Function encryption
#Create a function named encryption which takes a parameter keys.

#The function will print 'Encryption Success' if the keys passed into function has 5 characters and print 'Encryption Fail' if it doesn't.

def encryption(keys):
    if(len(keys) == 5):
        print('Encryption Success')
    else:
        print('Encryption Fail')
encryption('abcde')

#8 Function even_cryptography
#Create a function named even_cryptography which takes a parameter num.

#The function will print 'Decryption Success' if the number passed into the function is even and print 'Decryption Fail' if it isn't.

def even_cryptography(num):
    if(num%2 == 0):
        print('Decryption Success')
    else:
        print('Decryption Fail')
even_cryptography(2)

#9