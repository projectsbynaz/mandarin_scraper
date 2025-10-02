# mandarin_scraper  
A hands-on learning project using Scrapy to understand web scraping through building a structured Mandarin phrase dataset.

## Project Description  
I started this project because I wanted to learn Python by actually building something useful. Instead of just reading tutorials, I decided to try web scraping Mandarin phrases from a website to create my own phrase dataset.

Along the way, I learned a lot about Scrapy, which is a tool I had not used before. I moved from Google Colab and BeautifulSoup to using Scrapy on VSCode because Colab couldn't handle the setup well (mainly around running spiders and saving files).

One big takeaway was how important it is to **inspect** web pages carefully. Using browser developer tools to understand HTML structure and tags helped me figure out exactly what to scrape. It made the process clearer and saved a lot of trial and error.

---

## Files Included  
- **`topics_spider.py`**: This is the main Scrapy spider script I wrote to scrape Mandarin phrases. It navigates the website, finds the right data, and extracts it.  
- **`convert_to_csv.py`**: A simple Python script I used to clean the scraped data and convert it into a neat CSV file. It helps organise the Mandarin phrases, their Pinyin, and English translations.  
- **`phrases_cleaned.csv`**: The final CSV file with the cleaned, structured dataset I created from the scraping process.

---

## What I Learned  
- How to use **Scrapy** for web scraping, which felt more efficient and versatile than BeautifulSoup for bigger projects.  
- The importance of using **inspection tools** to understand the HTML structure, which is key to getting the right data.  
- How to clean and organise data into a usable format like CSV.  
- How to troubleshoot issues like running scraping scripts in different environments (moving from Colab to VSCode helped me learn about working locally).  
- The value of learning by doing. Trying, failing, and figuring things out as I go.

---
