
* Requirements
* Chrome Driver [https://sites.google.com/a/chromium.org/chromedriver/home]
   environment.py creates webdriver instance using path to chromedriver
* chrome needs to be installed (version >= 61.0.3163.0)

for executing on firefox:
install geckodriver manually if not there already:
for mac installer command is: brew install geckodriver

for executing on safari on macOS:
goto Safari>Preferences>Advanced: click on "Show develop menu in menu bar"
goto Develop> click on "Allow remote Automation"
close all safari, do "safaridriver --enable"

* useful links :
** https://gist.github.com/carlosmmelo/0ca23e212dcd98028baa
** https://help.crossbrowsertesting.com/selenium-testing/frameworks/behave/


pre-requisite:

install python3 

sudo python3 setup.py install

chromedriver inside $PATH for chrome
geckodriver inside $PATH for firefox


sample command
/usr/local/bin/behave -Dbrowser=chrome uitests/features/base.feature -Durl=facebook.com -Dheadless=n
behave -Dbrowser=chrome uitests/features/base.feature -Dheadless=n
behave -Dbrowser=firefox uitests/features/base.feature -Dheadless=n