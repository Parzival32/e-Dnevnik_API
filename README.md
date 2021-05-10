# e-Dnevnik API
* Kinda slow (avarage 3 seconds) ednevnik api for getting user information.
* You can install this module via pip with command "pip install ednevnik"
* Link to pipy project https://pypi.org/project/ednevnik

### Requirements
* selenium
* chrome
* webdriver (needs to be installed via following link https://chromedriver.chromium.org/downloads [needs to be the same version as chrome installed on your computer])

### Description of functions
* `auth` function returns if given username and password are correct.
* `grade` function returns which class a given user is.
* `nameSurname` function returns a name and surname of given user in a form of list.
* `userNumber` function returns ordinal number of a user.
* `getClassYear` function returns current class year.
* `getSchool` function returns users current school.
* `userInfo` function returns all info of a given user. (output is given in a list in the following order: [name, surname, grade, userNumber, year, school] and every element is a string )

### Example Code 1
```py
import ednevnik

username = "jeremy.clarkson@skole.hr"
password = "76ghBI7g"
path = "C:\Users\James\chromedriver.exe"        #path is your personal path where webdriver is located on your PC

dnevnik = ednevnik.api(username, password, path)

userClass = dnevnik.grade()
print(userClass)
```
### Example Code 2
```py
import ednevnik

dnevnik = ednevnik.api("james.may@skole.hr", "09OIjs65", "C:\Users\James\Programs\chromedriver.exe")

authentication = dnevnik.auth()
if authentication:
    print('User is valid.')
else:
    print("User info is incorrect or doesn't exist.")
```
### Example Code 3
```py
import ednevnik

username = "richard.hammond@skole.hr"
password = "9865Y7jH"
path = "C:\Users\Richard\Modules\chromedriver.exe"       #path is your personal path where webdriver is located on your PC

dnevnik = ednevnik.api(username, password, path)

userInformation = dnevnik.userInfo()
print(userInformation)
```