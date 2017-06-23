from selenium import webdriver
from queue import Queue
import datetime
import random
import time

def get_auction_data(link):
	# open new chrome browser window
	chromedriver_path = "C:/Users/chris/OneDrive/Documents/github/web-scrapers/chromedriver"
	driver = webdriver.Chrome(chromedriver_path)  
	driver.get(link)
	# scrape title and set-up variables
	auc_title = driver.find_element_by_xpath("//h1[@id='product_title']").text
	new_max_price = 0
	old_max_price = 0
	bids_array = []

	# check that we are watching the beginning of the auction and can scrape complete data
	cur_auc_price_string = driver.find_element_by_xpath("//div[@id='auction-left']/div/p/span[@class='price']").text
	cur_auc_price = float(cur_auc_price_string[1:])
	if not cur_auc_price < 0.07:
		driver.quit()
		return None
	
	# scrape in a loop if bid is live
	while True:
		# check if the grey ended button is being displayed on the screen
		button_check = driver.find_elements_by_xpath("//div[@id='auction-left']/div/p/a[@class='buttons grey large']")
		if len(button_check) > 0:
			button_string = button_check[0].text
			if button_string == "Ended":
				print("Auction has ended")
				break
		try :
			# usually something goes wrong because in the middle of the try block the auction ends
			# using a try and then empty except block is just a really hacky way of fixing the problem
			bid_list = driver.find_elements_by_xpath("//table[@id='bid-history']/tbody/tr")
			if bid_list[0].find_element_by_xpath("td[@class='username']").text != " ":
				max_price_string = bid_list[0].find_element_by_xpath("td[@class='amount']").text
				new_max_price = float(max_price_string[1:])
				if new_max_price > old_max_price :
					for bid in bid_list:
						bid_price_string = bid.find_element_by_xpath("td[@class='amount']").text
						if bid_price_string != " ":
							bid_price = float(bid_price_string[1:])
							if bid_price > old_max_price:
								bid_username = bid.find_element_by_xpath("td[@class='username']").text
								bid_type =  bid.find_element_by_xpath("td[@class='bid-type']").text
								bid_data = (bid_username, bid_price, bid_type)
								bids_array.append(bid_data)
								print(bid_data)
				old_max_price = new_max_price
				handle_timeout(driver)
		except: 
			pass

	# wrap everything up in an auction object
	driver.quit()
	auc_data = None
	auc_time_raw = datetime.datetime.now()
	auc_time_format = datetime.datetime.strftime(auc_time_raw, '%Y-%m-%d %H:%M:%S')
	bids_array.sort(key=lambda tup: tup[1])  # sorts in place by bid price
	if len(bids_array) > 0:
		auc_winner = bids_array[-1][0]
		auc_end_price = bids_array[-1][1]
		auc_data = (auc_title, auc_time_format, auc_end_price, auc_winner, bids_array)	
		print("Auction Data:\n{}".format(auc_data))
		return auc_data
	else: 
		# if there are no bids in the data collected, an error occurred
		# return none and don't store bad data in db
		return None

def handle_timeout(driver):
	timeout_button = driver.find_elements_by_xpath("//a[contains(@onclick, 'location.reload(true);')]")
	if len(timeout_button) > 0:
		end_wait = random.randint(1, 60)
		start_wait = time.time()
		duration_wait = 0
		while end_wait > duration_wait:
			duration_wait = time.time() - start_wait
		timeout_button[0].click()

# this code allows for manual testing of method by copying / pasting links
if __name__ == '__main__':
	get_auction_data("http://www.quibids.com/en/auction-698134313US-C1593-15-voucher-bids")
