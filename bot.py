import requests as r
from bs4 import BeautifulSoup as soup
import telegram
import telebot

bot_token = 'YOUR_TOKEN'
bot_chatID = '@YOUR_TELEGRAM_CHANNEL_NAME'
bot = telebot.TeleBot('YOUR_TOKEN')

def Scraping(Country):
 try:
    """Construct scraping algorithm which takes 'country' as an input."""

  # Insert a web address to scrape.
    url = 'https://www.worldometers.info/coronavirus/country/' + Country

  # Get data in the HTML format.
    page_data = r.get(url).text

  # Get your data neatly formatted.
    data = soup(page_data, 'html.parser')

  # Get number of new cases.
    new_date = data.findAll('div',{'class':'news_date'})
    new_case = data.findAll('li',{'class':'news_li'})
    new_cases = new_case[0].text.replace('[source]','')
    total = new_date[0].text + ': ' + new_cases

  # Close the source website.
    return total.strip()

 except:
 	return 'No results.'

msg = Scraping('COUNTRY_NAME')
status = bot.send_message(chat_id='@YOUR_TELEGRAM_CHANNEL_NAME', text=msg, parse_mode=telegram.ParseMode.HTML)
if status:
    print(status)
