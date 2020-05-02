import requests
import os
import argparse
import sys
from dotenv import load_dotenv
load_dotenv()


def createParser():
  parser = argparse.ArgumentParser()
  parser.add_argument('link')
  return parser

def shorten_link(token_bitly, long_link):
  url = 'https://api-ssl.bitly.com/v4/bitlinks'
  response = requests.post(url, headers = token_bitly, json = {'long_url': long_link})
  return response.json()['id']

def count_clicks(token_bitly, short_link):
  url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(short_link)
  response = requests.get(url, headers = token_bitly, params = {'units': -1})
  return response.json()['total_clicks']

if __name__ == "__main__":
  header_bitly = {'Authorization': 'Bearer {}'.format(os.getenv('BITLY_TOKEN'))}

  parser = createParser()
  namespace = parser.parse_args(sys.argv[1:])
  link = namespace.link

  if link.startswith('http'):
    try:
      short_link = shorten_link(header_bitly, link)
    except requests.exceptions.HTTPError:
      print('Похоже, Вы ошиблись в формате ссылки.')
    print('Битлинк ' + short_link)
  else:
    try:
      click_counts = count_clicks(header_bitly, link)
    except requests.exceptions.HTTPError:
      print('Похоже, Вы ошиблись в формате ссылки.')
    print('Количество переходов по данной ссылке: ' + str(click_counts))

