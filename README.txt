#LinkChecker
LinkChecker is a Python 3.8 Selenium-based script used to save screenshots
and check redirection from web pages.

In order to use LinkChecker, you need to do the following:
1. Make sure you have Python 3.8 and Selenium library installed.
2. Fill in the "setup.txt" document with your own starting link, desired browser
(Chrome/Firefox) and time for the script to wait for the pages' downloads.
3. Fill in the "links.txt" document with the names of the buttons you wish to check,
their CSS-selectors, and string for the script to look for in the titles/urls of the
web pages.

REMARK: the above files are already prefilled with the settings necessary to check
links of the open-source frontend client of n.exchange. The users can change 
the data according to their needs.

[*] LinkChecker maintains an error log and screenshots with timestamps in order
to ease the debugging.