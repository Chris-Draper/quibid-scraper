def handle_page_timeout(driver):
	timeout_button = driver.find_elements_by_xpath("//a[contains(@onclick, 'location.reload(true);')]")
	if len(timeout_button) > 0:
		end_wait = random.randint(1, 60)
		start_wait = time.time()
		duration_wait = 0
		while end_wait > duration_wait:
			duration_wait = time.time() - start_wait
		timeout_button[0].click()