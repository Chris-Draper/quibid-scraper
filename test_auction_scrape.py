from selenium import webdriver
import time

auction_link_list = []

def get_auctions_displayed():
    chromedriver_path = "C:/Users/chris/OneDrive/Documents/github/web-scrapers/chromedriver"
    driver = webdriver.Chrome(chromedriver_path)  
    driver.get("http://www.quibids.com/en/category-12-vouchers-and-limit-busters/")
    start_time = time.time()
    end_time = time.time()
    # grab all 20 links on the page
    while (end_time - start_time) < 3500:
        link_list = driver.find_elements_by_xpath("(//h5[@class='auction-item-title'])/a") 
        for link in link_list:
            link_string = link.get_attribute('href')
            if link_string not in auction_link_list:
                auction_link_list.append(link_string)
        time.sleep(1800)
        end_time = time.time()

    print("Scanned quibids website for 1 hour. These are the auctions seen.")
    for link in auction_link_list:
        print(link)

if __name__ == '__main__':
    get_auctions_displayed()