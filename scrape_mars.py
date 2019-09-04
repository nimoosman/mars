#!/usr/bin/env python
# coding: utf-8

# Mission to Mars
# Step 1

# In[1]:


# Dependencies
import os
from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd
import splinter
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from selenium import webdriver
import shutil
from IPython.display import Image


# In[2]:


executable_path = {"executable_path": "C:/Users/Lenovo_7/Desktop/Class_Folders/Web_Scraping/chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)


# In[3]:


# URL of page to be scraped
news_url ="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(news_url)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# NASA Mars News
# 
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# In[5]:


articles = soup.find("div", class_="list_text")
news_p = articles.find("div", class_="article_teaser_body").text
titles = articles.find("div", class_="content_title").text
dates = articles.find("div", class_="list_date").text
print(news_p)
print(dates)
print(titles)


# In[ ]:





# JPL Mars Space Images - Featured Image
# 
# Visit the url for JPL Featured Space Image here.
# 
# Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
# 
# Make sure to find the image url to the full size .jpg image.
# 
# Make sure to save a complete url string for this image.

# In[6]:


jpl_url = "https://jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(jpl_url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')
image = soup.find("img", class_="thumb")["src"]
img_url = "https://jpl.nasa.gov"+image

featured_image_url = img_url
response = requests.get(img_url, stream=True)
with open('img.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)

Image(url='img.jpg')


# In[ ]:





# Mars Weather
# 
# Visit the Mars Weather twitter account here and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.

# In[7]:


executable_path = {"executable_path": "C:/Users/Lenovo_7/Desktop/Class_Folders/Web_Scraping/chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)
tweet_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(tweet_url)


# In[8]:


html = browser.html
mars_weather_soup = BeautifulSoup(html, "html.parser")


# In[9]:


tweet = mars_weather_soup.find("div", class_="js-tweet-text-container")


# In[10]:


weather = tweet.find("p", "tweet-text").get_text()
print(weather)


# Mars Facts
# 
# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# 
# Use Pandas to convert the data to a HTML table string.

# In[11]:


facts = "http://space-facts.com/mars/"
browser.visit(facts)

facts_todf=pd.read_html(facts)
data=pd.DataFrame(facts_todf[0])
data.columns=["Mars-Earth Comparison","Mars", "Earth"]
table=data.set_index("Mars")
html_data = table.to_html(classes='html_data')
html_data=html_data.replace('\n', ' ')
html_data


# Mars Hemispheres
# 
# Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# 
# You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# 
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# 
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

# In[12]:


executable_path = {"executable_path": "C:/Users/Lenovo_7/Desktop/Class_Folders/Web_Scraping/chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless=False)
astro_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(astro_url)


# In[13]:


image_urls = []

links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    mars_hemispheres = {}
    
    browser.find_by_css("a.product-item h3")[item].click()
    element = browser.find_link_by_text("Sample").first
    mars_hemispheres["img_url"] = element["href"]
    
    mars_hemispheres["title"] = browser.find_by_css("h2.title").text
    image_urls.append(mars_hemispheres)
    browser.back()


# In[14]:


image_urls


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




