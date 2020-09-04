# Jellyworkz
Test assessment by Jellyworkz

## Running all the stuff
1. Clone repo: `git clone https://github.com/Kirom/Jellyworkz.git`
2. Create virtualenv, for example: `python3 -m venv venv` or `virtualenv -p python3 venv`
3. Activate it `source venv/bin/activate`
4. Install all the packages `pip install -r requirements.txt`
5. Change config in scrape.py: set your credentials for Database
6. Start scraping script `python scrape.py`
7. Change config in app.py: set your credentials for Database
8. Start the app itself `python app.py`