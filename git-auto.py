import time
import os
import sys

from selenium import webdriver


url = 'https://github.com/login'
github_username = 'your_GitHub_username'
github_password = 'your_GitHub_password'


# create a folder for project
path = sys.argv[1]
project_name = sys.argv[2]

os.chdir(path)
os.mkdir(project_name)
os.chdir(project_name)


# going on GitHub to create repository
browser = webdriver.Chrome('path/to/your/webdriver')
browser.get(url)

# login on GitHub
time.sleep(1)
browser.find_element_by_xpath('//*[@id="login_field"]').send_keys(github_username)
browser.find_element_by_xpath('//*[@id="password"]').send_keys(github_password)
browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]').click()

# create new repository on GitHub
time.sleep(1)
browser.find_element_by_xpath('//*[@id="repos-container"]/h2/a').click()
browser.find_element_by_xpath('//*[@id="repository_name"]').send_keys(project_name)
browser.find_element_by_css_selector('button.first-in-line').submit()
browser.quit()


# create README.md, git remote and commit
os.system('echo ' + '# ' + project_name + ' > README.md')
os.system('git init')
os.system('git add README.md')
os.system('git commit -m "initial commit"')
os.system('git branch -M main')
os.system('git remote add origin https://github.com/' + github_username + '/' + project_name + '.git')
os.system('git push -u origin main')
