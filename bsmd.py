from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# start the web driver
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless=new")
driver = webdriver.Chrome(options=chrome_options)

# prompts for fiction/non-fiction template & goodreads url
t = input("f/nf?: ")    
url = input("link: ")
driver.get(url)

# finds book title & author from url
title_header_element = driver.find_element(By.CLASS_NAME, "BookPageTitleSection__title")
title_element = title_header_element.find_element(By.TAG_NAME, 'h1')
title = title_element.text

author_element = driver.find_element(By.CLASS_NAME, "ContributorLink__name")
author = author_element.text

# book description string for md file
d_str = "# " + title + "\n\nAuthor: " + author + "\nDate Started:\nDate Ended:\nRating:\n\n"

# non-fiction template
nf_str = "# the book in 3 sentences\n\n# impressions\n\n# who should read it?\n\n# how the book changed me\n\n# my top 3 quotes\n\n# summary + notes\n"
# fiction template
f_str = "# summary\n\n# how i discovered it\n\n# thoughts\n\n# who would like it?\n"

# writes to file   
with open(title + '.md', 'w') as f:
    f.write(d_str)
    if (t == 'f'):
        f.write(f_str)
    elif (t == 'nf'):
        f.write(nf_str)
    

