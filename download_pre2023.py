import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def WRITE_DATA(website,css_selector_dropdowns_list,css_selector_button,css_selector_table,csv_name):

    driver = webdriver.Chrome()
    driver.get(website)

    for css_selector_dropdown in css_selector_dropdowns_list:
        css_selector_trigger = css_selector_dropdown[0]
        css_selector_option = css_selector_dropdown[0] + " > div > ul > li:nth-child({})".format(css_selector_dropdown[1])
        myButton = driver.find_element(By.CSS_SELECTOR,css_selector_trigger)
        myButton.click()
        myOption = driver.find_element(By.CSS_SELECTOR,css_selector_option)
        myOption.click()

    myButton = driver.find_element(By.CSS_SELECTOR,css_selector_button)
    myButton.click()

    myTable = driver.find_element(By.CSS_SELECTOR,css_selector_table)

    with open(csv_name, 'w', newline='') as csvfile:
        wr = csv.writer(csvfile)
        for row in myTable.find_elements(By.CSS_SELECTOR,"tr"):
            wr.writerow([d.text for d in row.find_elements(By.CSS_SELECTOR,"td")])

    driver.quit()
    
    return()

print()

website = 'https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx'

css_selector_dropdowns_list = [
    ["#ctl00_ContentPlaceHolder1_ddlYear_chosen",8],
    ["#ctl00_ContentPlaceHolder1_ddlroundno_chosen",2],
    ["#ctl00_ContentPlaceHolder1_ddlInstype_chosen",2],
    ["#ctl00_ContentPlaceHolder1_ddlInstitute_chosen",2],
    ["#ctl00_ContentPlaceHolder1_ddlBranch_chosen",2],
    ["#ctl00_ContentPlaceHolder1_ddlSeatType_chosen",6]
]

css_selector_button = "#ctl00_ContentPlaceHolder1_btnSubmit"

css_selector_table = "#ctl00_ContentPlaceHolder1_GridView1"

# csv_name = "test.csv"

for i in range(7):

    year = 2016 + i
    year_option = 8-i
    css_selector_dropdowns_list[0][1] = year_option

    for j in range(6):

        round_name = j+1
        round_option = j+2
        css_selector_dropdowns_list[1][1] = round_option

        # print()
        # print(css_selector_dropdowns_list)
        # print()

        csv_name = "{}/round{}.csv".format(year,round_name)

        try:
            WRITE_DATA(website,css_selector_dropdowns_list,css_selector_button,css_selector_table,csv_name)
            print ("Saved for year {}, round {} ".format(year,round_name))
        except Exception as e:
            print ("\n Cannot save for year {}, round {} \n {} \n".format(year,round_name,e))

exit()