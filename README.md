# Bitly url shortener
This code lets you get shortened link through bit.ly api and count clicks from this shortened link.

## How to install

Python3 should be already installed. Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

`pip install -r requirements.txt`


##How to use

Don't forget to create .env file with string like

`BITLY_TOKEN=<YOUR BITLY API TOKEN>`

Type full link (http://...) to shorten it.
```
python main.py http://biocad.ru
Битлинк bit.ly/3bnGgQy
```

Type shortened link to get count of clicks.

```
python main.py bit.ly/3bnGgQy
Количество переходов по данной ссылке: 2
```
## Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.