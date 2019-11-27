"""		
	ui-tests.lib.selenium		
	~~~~~~~~~~~~~~~~~~~~~		"		
	Common utilities for selenium-based testing		
"""		
			
from os import path, makedirs		
from time import sleep		
from selenium import webdriver		
from selenium.webdriver.remote.switch_to import SwitchTo		
from selenium.common.exceptions import NoSuchWindowException,UnexpectedAlertPresentException,TimeoutException,NoAlertPresentException		
from selenium.webdriver.common.by import By		
from selenium.webdriver.support import expected_conditions		
from selenium.webdriver.support.wait import WebDriverWait

DELAY = 5		
WAIT = 15		
LOADING_ELEMENT_CLASSNAME = "regionOverlay"		
def wait_for_correct_state(context):		
	"""		
	Utility method that tries to wait for correct state of web page		
			
	:param context: Behave context		
	"""
	sleep(1)		
	page_fully_loaded(context)		
			
			
def setup_browser(context, browser_name, remote, headless):		
	"""		
	Sets up correct selenium browser based on parameters		
			
	:param context: Behave context		
	:param browser_name: browser name		
	:param remote: remote web driver address		
	:param headless: if local web browser is started in headless mode or not		
	:returns: selenium browser		
	"""		
			
	browser = None		
			
	if remote:		
	    desired_capabilities = webdriver.DesiredCapabilities.CHROME
	    if browser_name == "chrome":		
	        desired_capabilities = webdriver.DesiredCapabilities.CHROME		
	    elif browser_name == "firefox":		
	        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX		
# 	        desired_capabilities["unexpectedAlertBehaviour"] = "ignore"		
# 	        desired_capabilities["UNEXPECTEDALERTBEHAVIOUR"] = "IGNORE"		
	    elif browser_name == "iexplore":		
	        desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER		
	    elif browser_name == "edge":		
	        desired_capabilities = webdriver.DesiredCapabilities.EDGE		
	    elif browser_name == "safari":		
	        desired_capabilities = webdriver.DesiredCapabilities.SAFARI		
			
	    browser = webdriver.Remote(command_executor=remote,desired_capabilities=desired_capabilities)		
	elif browser_name == "chrome":		
	    options = webdriver.ChromeOptions()		
	    options.headless = headless		
	    options.add_argument("disable-gpu")		
	    browser = webdriver.Chrome(options=options)		
	elif browser_name == "safari":		
	#        options = webdriver.SafariOptions() 		
	#        options.set_headless(headless)		
	#        options.add_argument("disable-gpu") 		
	    browser = webdriver.Safari()		
	elif browser_name == "firefox":		
	    options = webdriver.FirefoxOptions()		
	    options.headless = headless		
	    browser = webdriver.Firefox(options=options)		
	elif browser_name == "iexplore":		
	    browser = webdriver.Ie()		
	elif browser_name == "edge":		
	    browser = webdriver.Edge()		
		
	browser.implicitly_wait(DELAY)		
	browser.set_page_load_timeout(WAIT * 2)		
	context.browser = browser		
			
			
def page_fully_loaded(context, seconds=WAIT):		
	"""		
	Waits until page is fully loaded		
			
	:param context:  behave context		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	WebDriverWait(context.browser, float(seconds)).until(		
	        lambda browser: browser.execute_script("return document.readyState;") == "complete",		
	         "Page was not fully loaded in {} seconds".format(seconds))		
			
	WebDriverWait(context.browser, float(seconds)).until(		
	        expected_conditions.invisibility_of_element_located((By.CLASS_NAME, LOADING_ELEMENT_CLASSNAME)),		
	        "Page was still loading in {} seconds".format(seconds))		
			
			
def switch_to_tab(context, tab_index, seconds=WAIT):		
	"""		
	Switches to browser tab at `tab_index`		
			
	:param context: behave context		
	:param tab_index: tab index		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	def switched_to_tab(index):		
		def predicate(browser):
			handles = browser.window_handle
			tab_len = len(handles)		
			if tab_len <= index:
				return False		
				try:
					browser.switch_to_window(handles[index])
				except NoSuchWindowException:		
					return False
			else:
				return True		
		return predicate		
			
	wait_for_correct_state(context)		
	return WebDriverWait(context.browser, float(seconds)).until(		
	    switched_to_tab(tab_index),		
	    "Failed to switch to tab {} in {} seconds".format(tab_index, seconds))		
			
		
def flush_browser(context, tag, success):		
	"""		
	This method closes browser and saves screenshot in case of failure		
			
	:param context: behave context		
	:param tag: process tag		
	:param success: defines if process results was successful		
	"""		
			
	if not success:		
	    report_dir = path.join("reports", "failed_scenarios_screenshots")		

	    if not path.exists(report_dir):		
	        makedirs(report_dir)		
	    print("screenshot saved for failed", tag , "at :",report_dir)		
	    context.browser.save_screenshot(path.join(report_dir, tag + ".png"))		
			
	context.browser.quit()		
			
			
def open_url(context, url):		
	"""		
	Opens `url` in browser		
			
	:param context: Behave context		
	:param url: URL to navigate to		
	"""		
			
	context.browser.get(url)		
		
def check_title(context, title, seconds=WAIT):		
	"""		
	Checks if page title matches `title`		
			
	:param context: Behave context		
	:param title: Title to check for		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	wait_for_correct_state(context)		
	return WebDriverWait(context.browser, float(seconds)).until(		
#	    expected_conditions.title_is(title),
		expected_conditions.title_contains(title),
	    "Expected title '{}' was not set after waiting for {} seconds".format(title, seconds)		
	)		
			
			
def check_url(context, title, seconds=WAIT):		
	"""		
	Checks if page title matches `title`		
			
	:param context: Behave context		
	:param title: Title to check for		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	wait_for_correct_state(context)		
	return WebDriverWait(context.browser, float(seconds)).until(		
	    expected_conditions.url_contains(title),		
	    "Expected title '{}' was not set after waiting for {} seconds".format(title, seconds)		
	)		
			
			
def click_on(context, by_type, selector, seconds=WAIT):		
	"""		
	Clicks on element on `path` that is looked up using `by_type`		
			
	:param context: Behave context		
	:param by_type: Selenium element type		
	:param selector: Path to search for		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	try:		
	    test_element_clickable(context, by_type, selector, seconds).click()		
			
	except UnexpectedAlertPresentException:		
	    try:		
	        alerter = SwitchTo(context.browser).alert		
	        alerter.accept()		
	    #        alert.click() 		
	    except NoAlertPresentException:		
	        if context.browser == "chrome":		
	            return True		
	        else:		
	            return False		
	 #           return True 		
	else:		
	    return False		
			
def click_on_subsequent(context, by_type, selector, seconds=WAIT):		
	"""		
	Clicks on element on `path` that is looked up using `by_type`		
			
	:param context: Behave context		
	:param by_type: Selenium element type		
	:param selector: Path to search for		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	try:		
	    elements = context.find_elements_by_xpath("//*[@title='{}']".format(selector))
	    title = elements[1].find_elements_by_xpath("..//*[@class='icon-trash icon-small']")		
	    test_element_clickable(context, by_type, selector, seconds).moveto(selector)		
			
	except UnexpectedAlertPresentException:		
	    alerter = SwitchTo(context.browser).alert		
	    alerter.accept()		
	    #        alert.click() 		
	else:		
	    return False		
			
		
def enter_text(context, by_type, selector, text, seconds=WAIT):		
	"""		
	Enters `text` to element on `path` that is looked up using `by_type`		
			
	:param context: Behave context		
	:param by_type: Selenium element type		
	:param selector: Path to search for		
	:param text: Text to send to the element		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	test_element_visibility(context, by_type, selector, seconds).send_keys(text)		
			
			
def test_text_presence(context, by_type, selector, text, seconds=WAIT):		
	"""		
	Tests if `path` contains `text` in `seconds`, looked up using `by_type`		
			
	:param context: Behave context		
	:param by_type: Selenium element type		
	:param selector: Path to search for		
	:param text: Text to check for in element		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	wait_for_correct_state(context)		
	return WebDriverWait(context.browser, float(seconds)).until(		
	    expected_conditions.text_to_be_present_in_element(		
	        (by_type, selector),		
	        text),		
	    "Expected element '{}' did not contain text '{}' after waiting for {} seconds".format(selector, text, seconds)		
	)		
			
def test_value_presence(context, by_type, selector, value, seconds=WAIT):		
	"""		
	Tests if `path` contains `value` in `seconds`, looked up using `by_type`		
			
    :param context: Behave context		
	:param by_type: Selenium element type		
    :param selector: Path to search for		
	:param value: Value to check for in element		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	wait_for_correct_state(context)		
	return WebDriverWait(context.browser, float(seconds)).until(		
	    expected_conditions.text_to_be_present_in_element_value(		
	        (by_type, selector),		
	        value),		
	    "Expected element '{}' did not contain value '{}' after waiting for {} seconds".format(selector, value, seconds)		
	)		
			
			
def test_element_presence(context, by_type, selector, seconds=WAIT):		
	"""		
	Tests if `path` is present in tree in `seconds`, looked up using `by_type`		
			
	:param context: Behave context		
	:param by_type: Selenium element type		
	:param selector: Path to search for		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	wait_for_correct_state(context)		
	return WebDriverWait(context.browser, float(seconds)).until(		
	    expected_conditions.presence_of_element_located((by_type, selector)),		
	    "Expected element '{}' was not present after waiting for {} seconds".format(selector, seconds)		
	)		
			
			
def test_element_clickable(context, by_type, selector, seconds=WAIT):		
	"""		
	Tests if `path` is present in tree in `seconds`, looked up using `by_type`		
			
	:param context: Behave context		
	:param by_type: Selenium element type		
	:param selector: Path to search for		
	:param seconds: Seconds to wait until the condition fails		
	"""		
	#    print("values for by_type, selector and seconds is ",by_type ,"boom: ", selector  ,"boom: ", seconds) 		
	wait_for_correct_state(context)		
	return WebDriverWait(context.browser, float(seconds)).until(		
	    expected_conditions.element_to_be_clickable((by_type, selector)),		
	    "Expected element '{}' was not clickable after waiting for {} seconds".format(selector, seconds)		
	)		
			
def test_element_visibility(context, by_type, selector, seconds=WAIT):		
	"""		
	Tests if `path` is present in tree in `seconds`, looked up using `by_type`		
			
	:param context: Behave context		
	:param by_type: Selenium element type		
	:param selector: Path to search for		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	wait_for_correct_state(context)		
	return WebDriverWait(context.browser, float(seconds)).until(		
	    expected_conditions.visibility_of_element_located((by_type, selector)),		
	    "Expected element '{}' was not visible after waiting for {} seconds".format(selector, seconds)		
	)		
			
			
def test_element_invisibility(context, by_type, selector, seconds=WAIT):		
	"""		
	Tests if `path` is not present in tree in `seconds`, looked up using `by_type`		
			
	:param context: Behave context		
	:param by_type: Selenium element type		
	:param selector: Path to search for		
	:param seconds: Seconds to wait until the condition fails		
	"""		
			
	wait_for_correct_state(context)		
	return WebDriverWait(context.browser, float(seconds)).until(		
	    expected_conditions.invisibility_of_element_located((by_type, selector)),		
	    "Expected element '{}' is still present after waiting for {} seconds".format(selector, seconds)		
	)
