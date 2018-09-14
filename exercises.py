#Logic

#Conditional statements gives us the ability to check conditions and make decisions based on the condition.

#In this assignment, you'll be asked to create conditional statements using if, elif and else.

# Please commit and push your code after each completed exercise.

#1. Declare a variable named weather and assign it a string value of 'rain'. Next create a conditional statement that will check the weather and print 'Bring an umbrella' if weather equals 'rain'.
weather = 'rain'

def weather_checker(weather_condition):
  if(weather_condition=='rain'):
    return 'Bring an umbrella'
  else:
    return 'damn boi'

print(weather_checker(weather))


#2 Declare a variable named score and assign it a number value of 70. Next create a conditional statement that will check the score and print 'You pass!' if the score is 70 and above and print 'Study harder!' if the score is less than 70.
score = 70

def score(score):
  if(score>=70):
    return 'You pass!'
  else:
    return 'You suck'
print(score(score))

#3. Declare a variable named download_speed and assign it a data value of 50. Next create a conditional statement that will check the download speed and print the following based on the condition:

# <= 50: 'Basic Package'
# <=100: 'Premium Package'
# >100: 'Platinum Package'
download_speed = 101

def which_package(score):
  if score<=50:
    return 'Basic Package'
  elif score<=100:
    return 'Premium Package'
  else:
    return 'Platinum Package'

print(which_package(score))

 #4 Function - check_password
 #Create a function named check_password which takes a parameter password.

 #The function will return true if the password passed into the function is equal to 'qwerty'. Declare a variable named password_result and print your result.

passw = 'qwerty'
def password_result(pw):
  return (pw == 'qwerty')

print(password_result(passw))

#5 Function check_login
#Create a function named check_login which takes a parameter login.

#The function will print 'Login Success' if the login passed into the function is equal to 'DevLeague' and print 'Re-enter Login' if it doesn't.

login = 'DevLeague'

def check_login(log):
  if(log == 'DevLeague'):
    return 'Login Success'
  else:
    return 'Re-enter Login'

print(check_login(login))


#6 Function malware_type
#Create a function named malware_type which takes a parameter malware.

#The function will print the following based on the following conditions:
#if malware is adware: 'Low Threat'
#if malware is virus: 'Do not share files'
#default message 'I hope you backed up your data'

checked = 'virus'

def malware_type(malware):
  if(malware == 'adware'):
    return 'Low Threat'
  elif(malware == 'virus'):
    return 'Do not share files'
  else:
    return 'I hope you backed up your data'

print(malware_type(checked))


#7 Function encryption
#Create a function named encryption which takes a parameter keys.

#The function will print 'Encryption Success' if the keys passed into function has 5 characters and print 'Encryption Fail' if it doesn't.
def encryption(keys):
  if(len(keys) == 5):
    return 'Encryption Success'
  else:
    return 'Encryption Fail'

print(encryption('12345'))

#8 Function even_cryptography
#Create a function named even_cryptography which takes a parameter num.

#The function will print 'Decryption Success' if the number passed into the function is even and print 'Decryption Fail' if it isn't.

#9 Function bandwidth
#Declare a variable named mbps and assign it a list of 5 number values of your choosing.

#Next, create a function named bandwidth which takes a parameter usage.
#The function will sum up the list of numbers and print the following messages based on the condition:

#if sum <= 50: 'Light User'
#if sum <= 100: 'Moderate User'
#if sum <=150: 'Multi Media User'
#if sum >150: 'Power User'

#10 Function ssh_keys
#Create a function named ssh_keys which takes two parameters public and private.

#The function will return false if public and private aren't equal and return true if they are equal.

#Declare a variable named ssh_connection and print your result.

#11 Function largest_num
#Create a function named largest_num which takes three parameters: num_1, num_2 and num_3.

#The function will find the largest number among any three numbers that are passed into the function. Declare a variable named large_num_result and print your results.

#12 Function pos_neg
#Create a function named pos_neg which takes a parameter num.

#The function will print 'Positive Number' if the number passed in is positive, print 'Zero' if the number is 0 and print 'Negative Number' for a negative number.

#13 Function name_caps
#Create a function named name_caps which takes a parameter name.

#The function will check the number of characters in the name that is passed into the function and do the following:

#if characters in name <=5: capitalize the first letter in the name
#if characters in name <=10: captialize all the letters in the name
#if characters in name >10: leave the letters as is

#Print your results

#14 Function leap_year

#A leap year occurs every four years. Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but are leap years if they are exactly divisible by 400.

#Create a function named leap_year which takes a parameter year.
#The function will print 'The year x is a leap year.' where x is the year value that is passed into the function and print 'The year x is not a leap year.' if it isn't a leap year.


