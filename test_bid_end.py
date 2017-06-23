from selenium import webdriver

chromedriver_path = "C:/Users/chris/OneDrive/Documents/github/web-scrapers/chromedriver"
driver = webdriver.Chrome(chromedriver_path)  
driver.get("http://www.quibids.com/en/auction-957646803US-C1346-25-voucher-bids")

while True:
    is_sold = driver.find_elements_by_xpath("//div[@id='auction-left']/div/p/a[@class='buttons grey large']")
    print("Length : {}".format(len(is_sold)))
    if len(is_sold) > 0:
        print("Found that the bid has been closed")
        break

driver.quit()