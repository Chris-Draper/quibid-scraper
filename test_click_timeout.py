from selenium import webdriver
import random
import time

def click_timeout_button():
	chromedriver_path = "C:/Users/chris/OneDrive/Documents/github/web-scrapers/chromedriver"
	driver = webdriver.Chrome(chromedriver_path)  
	driver.get("http://www.quibids.com/en/category-12-vouchers-and-limit-busters/")
	start_time = time.time()
	bench_mark_time = 300
	print("Starting button time out loop")

	while True:
		current_time = time.time()
		run_time = current_time - start_time
		if run_time > bench_mark_time:
			print("Hit bench mark time {} minutes".format(bench_mark_time / 60))
			bench_mark_time += 300

		timeout_button = driver.find_elements_by_xpath("//a[contains(@onclick, 'location.reload(true);')]")
		if len(timeout_button) > 0:
			input("Found timeout button. To auto click the button after a random number of seconds press enter")
			end_wait = random.randint(1, 60)
			start_wait = time.time()
			duration_wait = 0
			print("Random wait time is {} seconds".format(end_wait))
			while end_wait > duration_wait:
				duration_wait = time.time() - start_wait
			timeout_button[0].click()
			print("Timeout button was clicked")

if __name__ == '__main__':
	click_timeout_button()

"""
This is the element I want to be clicking

<div class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-draggable" tabindex="-1" role="dialog" aria-labelledby="ui-dialog-title-popupModal" style="display: block; z-index: 1002; outline: 0px; height: auto; width: 300px; top: 424px; left: 465.5px;">
<div class="ui-dialog-titlebar ui-widget-header ui-corner-all ui-helper-clearfix">
<span class="ui-dialog-title" id="ui-dialog-title-popupModal">QuiBids Inactivity</span>
<a href="#" class="ui-dialog-titlebar-close ui-corner-all" role="button"><span class="ui-icon ui-icon-closethick">close</span></a></div>
<div id="popupModal" style="width: auto; min-height: 0px; height: 127px;" class="ui-dialog-content ui-widget-content" scrolltop="0" scrollleft="0">
<strong>You have not had any activity in 30 minutes, are you still here?</strong><br><br><div style="float:right;margin-top:10px;">

<a href="#" class="buttons orange" onclick="location.reload(true);">
<font color="white">I'm back</font></a>

</div><br>&nbsp;<br></div></div>

"""

