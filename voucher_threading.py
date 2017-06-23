'''
This is from https://www.tutorialspoint.com/python/python_multithreading.htm
Copy and pasted from the last block of code

If you remove the Queue lock on lines 29 - 35 you may complete things from the queue out of order
'''
from link_scrape import load_auction_links, update_auction_links
from auction_scrape import get_auction_data
from store_auction_data import store_auction_data
# everything above is imported from project files
from selenium import webdriver
from msvcrt import getch # for detecting esc key press to end the program
import os # for grabbing the chrome_driver file path
import queue
import threading
import time


exitFlag = 0 # don't forget this is a global var
relative_dir = os.getcwd()
chromedriver_path = relative_dir + '\chromedriver'
queueLock = threading.Lock()
link_q = queue.Queue()
link_driver = webdriver.Chrome(chromedriver_path)
# visited links list was for testing only
visited_links = []

class myThread(threading.Thread):
   
    def __init__(self, tName, link_q):

        threading.Thread.__init__(self)
        self.tName = tName
        self.link_q = link_q
   
    def run(self):

        print("Starting " + self.tName)
        open_auction(self.name, self.link_q)
        print("Exiting " + self.tName)

def open_auction(threadName, link_q):
    
    while not exitFlag:
        print("Exit Flag is {}".format(exitFlag))
        queueLock.acquire() # queueLock runs this synchronously for this code only
        if not link_q.empty():
            auction_link = link_q.get()
            visited_links.append(auction_link)
            print("Link_q Size : {}".format(link_q.qsize()))
            if link_q.qsize() <= 10:
                print("---------- Adding new links into queue")
                refill_link_q()
            queueLock.release()

            print("Thread {} will open link {}".format(threadName, auction_link))
            # open driver and begin scraping
            auction_data = get_auction_data(auction_link)
            # store the auction data in the data base if there were no errors
            if auction_data is not None:
                store_auction_data(auction_data)
        else:
            queueLock.release()
        time.sleep(1)

def refill_link_q():
    global link_q
    link_q = update_auction_links(link_driver, link_q)

def run_scraper():
    global link_q # get initial link queue from global variable
    
    print("Initializing driver and loading voucher page")
    link_driver.get("http://www.quibids.com/en/category-12-vouchers-and-limit-busters/")

    print("Fetching initial auction links")
    link_q = load_auction_links(link_driver, link_q)

    print("Number of links is : {}".format(link_q.qsize()))

    threadList = ["Thread-1", "Thread-2", "Thread-3"]
    threads = []

    # Create new threads
    for tName in threadList:
        thread = myThread(tName, link_q)
        thread.start()
        threads.append(thread)

    # Press esc key to stop scraping and exit threads
    while True:
        key = ord(getch())
        if key == 27: # ESC key
            break

    print("ESC key pressed. Setting exit flag and closing threads")

    # Notify threads it's time to exit
    global exitFlag # do this globally
    exitFlag = 1

    # Wait for all threads to complete
    for t in threads:
        t.join()
    print("Exiting Main Thread")
    link_driver.quit()
    print("Visited Links:")
    for link in visited_links:
        print(link)

if __name__ == '__main__':
    run_scraper()
