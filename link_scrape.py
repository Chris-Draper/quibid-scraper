'''
These methods feed the auction links into the queue. Links are pulled from the queue by threads

This is how you grab the first five links in the document
driver.find_elements_by_xpath("(//h5[@class='auction-item-title'])[position() <= 5]/a")
'''
from selenium import webdriver
from queue import Queue

def load_auction_links(driver, link_q):
    q_size = link_q.qsize()
    print("q_size should be 0 : {}".format(q_size))
    # grab all 20 links on the page
    link_list = driver.find_elements_by_xpath("(//h5[@class='auction-item-title'])/a") 
    link_count = 0  
    for link in link_list:
        link_count += 1
        link_string = link.get_attribute('href')
        print ("Added link {}".format(link_count))
        link_q.put(link_string)
    return link_q

def update_auction_links(driver, link_q):
    print("Adding new auction links to queue")
    q_size = link_q.qsize()
    q_size_string = str(q_size - 1)
    if q_size <= 10:
        # this was a little tricky, you need the parentheses when using position calls
        link_list = driver.find_elements_by_xpath("(//h5[@class='auction-item-title'])[position() >= last()-" + q_size_string + "]/a")
    link_count = 0
    for link in link_list:
        link_count += 1
        link_string = link.get_attribute('href')
        print ("Added link {}".format(link_count))
        link_q.put(link_string)
    return link_q
