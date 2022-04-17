from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import json
from sasta_ai import sasta_ai


xpaths=json.load(open("./xpaths.json"))
data=open("./exps.txt").read().split("\n")
row=1
c="True"        #boolean exp, starts with True
x=''        #possible expression        


def solver(data:list,value:int):
    #algorithm responsible for determining a possible expression based on the hints/conditions
    global x,norepeat,c
    for expression in data:
        try:
            if eval(expression)==value:
                print("testing:",expression)
                data.remove(expression)
                x=expression
                if eval(c)==True:
                    break
        except:
            pass

def getstate():
    #algorithm responsible for getting hints
    global row
    blocks=xpaths["rows"][str(row)]
    state={}
    for i in blocks:
        attribute=driver.find_element(by=By.XPATH,value=i).get_attribute("class")
        if "bg-green" in attribute:
            state[blocks.index(i)]=["green",x[blocks.index(i)]]
        elif "bg-slate" in attribute:
            state[blocks.index(i)]=["slate",x[blocks.index(i)]]
        elif "bg-yellow" in attribute:
            state[blocks.index(i)]=["yellow",x[blocks.index(i)]]
        else:
            return None
    row+=1
    return state

def main():
    global c,norepeat,x,row,driver
    op = webdriver.ChromeOptions()
    op.add_argument('log-level=3')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=op)
    actions = ActionChains(driver)
    driver.set_window_size(800,600)
    driver.get("https://www.mathler.com/")
    actions.move_to_element(driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div/div/div[2]/div[2]/div/div")).move_by_offset(200,0).click().perform()
    problem=int(driver.find_element(by=By.XPATH,value="/html/body/div/div/div[2]/h2").get_attribute("innerHTML").split()[-1])
    while True:
        solver(data=data,value=problem)
        print("Attempting:",x)
        for i in x:
            driver.find_element(by=By.XPATH,value="/html/body").send_keys(i)
        driver.find_element(by=By.XPATH,value="/html/body").send_keys(Keys.ENTER)
        c+=' and '+sasta_ai(getstate())     
        
        
try:
    main()
except:
    print("Success!!")
    while True:
        pass
