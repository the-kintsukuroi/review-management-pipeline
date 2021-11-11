#reference - https://github.com/giuseppegambino/Scraping-TripAdvisor-with-Python-2020/blob/master/restaurants_scraper.py
import sys
import csv
from selenium import webdriver
import time

# default path to file to store data
path_to_file = "//Users/karshi/Documents/GitHub/review-management-pipeline/review-collection/reviews.csv"

# default tripadvisor website of restaurant
url = "https://www.tripadvisor.com/Hotel_Review-g60745-d94337-Reviews-XV_Beacon_Hotel-Boston_Massachusetts.html"

# if you pass the inputs
url = input("Enter a Tripadvisor page url:")

# Import the webdriver
driver = webdriver.Safari()
driver.get(url)

# Open the file to save the review
csvFile = open(path_to_file, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)

# expand the review 
# time.sleep(2)
# driver.find_element_by_xpath(".//span[@class='eljVo _S Z']").click()

containers = driver.find_elements_by_xpath("//div[@class='cWwQK MC R2 Gi z Z BB dXjiy']")
for container in containers:
    title = container.find_element_by_xpath(".//a[@class='fCitC']/span/span").text
    rating = container.find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3][:-1]
    review = container.find_element_by_xpath(".//q[@class='XllAv H4 _a']/span").text
    csvWriter.writerow([rating, title, review]) 

driver.close()
