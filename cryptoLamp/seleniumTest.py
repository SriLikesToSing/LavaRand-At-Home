import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import random
from threading import Timer
import time
import randomGenerator


print(randomGenerator.generateNumber(0, 10, 100, 1))
print("successful")


'''
current problems:
    - ads
        - add an add blocker **CHECK
    - add input**CHECK

    TODO:
        - add arduino interfacing
            - pyserial?

        - find out what way you will be harmed
            - thing at the back of my head that punches the side of my face.
'''

class lavaLampTrader():

    def __init__(self):
        self.sellCryptos = ["https://cryptospaniards.com/simulator/trade/btc/usd"]
        self.buyCryptos = ["https://cryptospaniards.com/simulator/trade/usd/btc"]
        self.totalPrice = 10000
        self.n = randomGenerator.load_seed()

    def loginSequence(self):
        #adding addblocker
        chop = webdriver.ChromeOptions()
        chop.add_extension('./extension_4_42_0_0.crx')

        #initializing webdriver
        self.driver = webdriver.Chrome('./chromedriver.exe', chrome_options = chop)
        self.driver.get('https://cryptospaniards.com/simulator/login')

        #login sequence
        emailAddress = self.driver.find_element_by_name('email')
        password = self.driver.find_element_by_name('password')
        loginBox = self.driver.find_element_by_css_selector(".btn")
        emailAddress.send_keys("srilikestoscience@gmail.com")
        password.send_keys("")
        loginBox.click()

        return self.driver

    def returnPrice(self, driver):
        driver.get("https://cryptospaniards.com/simulator/dashboard")
        balance = driver.find_element_by_xpath('//div[@class="numbers"]').text
        balance = balance[23:-3]
        balance = int(balance.replace(',', ''))
        print("THIS IS THE PRICE")
        print(balance)

        return balance

    def beginTradeSequence(self):
        #asks the user if trading should commence
        print("Shall we commence the trading?")
        print("Y/N")
        i = input()
        if i == ("Y"):
            return True
        else:
            return False

    def randomCompanies(self):
        #first pick random number to choose how many cryptos there will be
        #talk to the crypto lamp
#        randAmount = randomGenerator.generateNumber(0, 1, 1, randomGenerator.load_seed())
        randomGenerator.boink()

        #choose out of a list of cryptos random indices
        randomIndices = randomGenerator.generateNumber(0, len(self.buyCryptos), 1, randomGenerator.load_seed())
        randomGenerator.boink()

        #return indices of the cryptos such that the purchase can be done
        print("randomIndices")
        print(randomIndices)
        
        return randomIndices 

    def randomPercentages(self, totalPrice, numCompanies):
        list =[]
        for x in range(numCompanies):
            list.append(randomGenerator.generateNumber(0, 100, 1, randomGenerator.load_seed())[0])
            randomGenerator.boink()

        list.insert(0, 0)
        list.insert(len(list), 100)
        list.sort()
        newDecimal = []

        for x in range(1, len(list)):
            newDecimal.append(((list[x] - list[x-1]))/100.0)

        return newDecimal

    def buyIndividual(self, companyIndex, totalPrice, percentages, driver):
        #buying
        print("BUYING BRO::::")
        driver.get(self.buyCryptos[companyIndex])
        amount = self.driver.find_element_by_id('from-amount')
        amount.clear()
        amount.send_keys("10")
        loginBox = self.driver.find_element_by_id("submit")
        loginBox.click()

    def sell(self, driver):
        #selling
        for x in self.sellCryptos:
            driver.get(x)
            amount = self.driver.find_element_by_id('from-amount')
            amount.clear()
            amount.send_keys("10")
            submitBox = self.driver.find_element_by_id("submit")
            submitBox.click()

    def buySequence(self, driver):
        ranCompanies = self.randomCompanies()
        randomPrice = randomGenerator.generateNumber(len(ranCompanies), self.totalPrice, 1, randomGenerator.load_seed())
        randomPercentages = self.randomPercentages(randomPrice, len(ranCompanies))

        print(randomPrice)
        print(randomPercentages)

        for x in range(0, len(ranCompanies)):
            self.buyIndividual(ranCompanies[x], randomPrice, randomPercentages[x], driver)

    def isMoneyLost(self, driver):

        newPrice = self.returnPrice(driver)

        if self.totalPrice-newPrice < 0:
           print("YOUR BROKE LOLLL")
        else:
            print("you got extremely lucky, and you will never see similar success again")
            return

        self.totalPrice = self.newPrice
        return

    def randomTrade(self):
        driver = self.loginSequence()
        self.returnPrice(driver)

        if self.beginTradeSequence() == False:
            #quit the program
            driver.close()

        endItAll = False
        while endItAll == False:
            self.buySequence(driver)
            time.sleep(5)
            self.sell(driver)
            self.isMoneyLost(driver)
            break

            if endItAll:
                print("THANKS FOR DESTROYING YOUR SOCIOECONOMIC STATUS YOU DUMB FUCK!")
                self.saveN(self.n)
                driver.close()
                return

        print("--END OF PROGRAM--")

s = lavaLampTrader()
s.randomTrade()








