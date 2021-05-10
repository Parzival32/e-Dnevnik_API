from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class api:
    def __init__(self,username, passowrd, path):
        self.username = username
        self.password = passowrd
        self.path = path

    loginFailed = 'Login failed'

    def auth(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(self.path, options=chrome_options)

        driver.get("https://ocjene.skole.hr/login")

        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        submit = driver.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()

        if driver.current_url == 'https://ocjene.skole.hr/course':  driver.close(); return True
        else:   driver.close(); return self.loginFailed

    def grade(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(self.path, options=chrome_options)

        driver.get("https://ocjene.skole.hr/login")

        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        submit = driver.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()

        if driver.current_url != 'https://ocjene.skole.hr/course':  driver.close(); return self.loginFailed

        grade_position = driver.find_element_by_xpath('//*[@id="class-administration-menu"]/div[1]/div/div[1]/span[1]')
        grade = grade_position.text
        driver.close()
        return grade

    def nameSurname(self):
        info = []

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(self.path, options=chrome_options)

        driver.get("https://ocjene.skole.hr/login")

        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        submit = driver.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()

        if driver.current_url != 'https://ocjene.skole.hr/course':  driver.close(); return self.loginFailed

        nameSurnamePosition = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/span')
        nameSurname = nameSurnamePosition.text
        name, surname = nameSurname.split()
        info.append(name)
        info.append(surname)
        driver.close()
        return info

    def userNumber(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(self.path, options=chrome_options)

        driver.get("https://ocjene.skole.hr/login")

        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        submit = driver.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()

        if driver.current_url != 'https://ocjene.skole.hr/course':  driver.close(); return self.loginFailed

        driver.get("https://ocjene.skole.hr/personal_data")
        userNumberPosition = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[4]/div/div[2]/span[2]')
        userNumber = userNumberPosition.text
        driver.close()
        return userNumber

    def getClassYear(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(self.path, options=chrome_options)

        driver.get("https://ocjene.skole.hr/login")

        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        submit = driver.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()

        if driver.current_url != 'https://ocjene.skole.hr/course':  driver.close(); return self.loginFailed

        year_position = driver.find_element_by_xpath('//*[@id="class-administration-menu"]/div[1]/div/div[1]/span[2]')
        year = year_position.text
        driver.close()
        return year

    def getSchool(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(self.path, options=chrome_options)

        driver.get("https://ocjene.skole.hr/login")

        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        submit = driver.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()

        if driver.current_url != 'https://ocjene.skole.hr/course':  driver.close(); return self.loginFailed

        school_position = driver.find_element_by_xpath('//*[@id="class-administration-menu"]/div[1]/div/div[2]/div[1]/span[1]')
        school = school_position.text
        driver.close()
        return school

    def userInfo(self):
        information = []

        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(self.path, options=chrome_options)

        driver.get("https://ocjene.skole.hr/login")

        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        submit = driver.find_element_by_xpath('//input[@type="submit"]')

        username.send_keys(self.username)
        password.send_keys(self.password)
        submit.click()

        if driver.current_url != 'https://ocjene.skole.hr/course':  driver.close(); return self.loginFailed

        grade_position = driver.find_element_by_xpath('//*[@id="class-administration-menu"]/div[1]/div/div[1]/span[1]')
        grade = grade_position.text
        nameSurnamePosition = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/span')
        nameSurname = nameSurnamePosition.text
        name , surname = nameSurname.split()
        year_position = driver.find_element_by_xpath('//*[@id="class-administration-menu"]/div[1]/div/div[1]/span[2]')
        year = year_position.text
        school_position = driver.find_element_by_xpath('//*[@id="class-administration-menu"]/div[1]/div/div[2]/div[1]/span[1]')
        school = school_position.text
        driver.get("https://ocjene.skole.hr/personal_data")
        userNumberPosition = driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[4]/div/div[2]/span[2]')
        userNumber = userNumberPosition.text
        information.append(name)
        information.append(surname)
        information.append(grade)
        information.append(userNumber)
        information.append(year)
        information.append(school)
        driver.close()
        return information