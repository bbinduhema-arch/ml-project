import os
import requests
from bs4 import BeautifulSoup
import datetime
from flask import Blueprint, render_template
from urllib.parse import urljoin

price_app = Blueprint('price', __name__)
pdf_dir = './static/pdf'
MARKET_URL = 'https://sericulture.karnataka.gov.in/info-4/Daily+Cocoon+Rates/Commercial+Cocoons+Rates/en'

def download_weekly_pdfs():
    """Scrapes the market website and downloads PDF reports for the current week."""
    print("Checking for new PDF files to download...")
    os.makedirs(pdf_dir, exist_ok=True)

    try:
        response = requests.get(MARKET_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        today = datetime.date.today()
        start_of_week = today - datetime.timedelta(days=today.weekday())
        
        dates_this_week = set()
        def safe_strftime(dt, fmt):
            try:
                return dt.strftime(fmt)
            except Exception:
                return None

        for i in range(7):
            current_day = start_of_week + datetime.timedelta(days=i)
            # The website uses date formats like 'DD-M-YY'. Try common variants,
            # but some platforms (Windows vs Unix) don't support all strftime flags.
            for fmt in ('%d-%m-%y', '%d-%#m-%y', '%d-%-m-%y'):
                s = safe_strftime(current_day, fmt)
                if s:
                    dates_this_week.add(s)

        for link in soup.find_all('a', href=True):
            href = link['href']
            if not href.endswith('.pdf'):
                continue

            if any(date_str in href for date_str in dates_this_week):
                pdf_url = urljoin(MARKET_URL, href)
                filename = os.path.basename(pdf_url.split("?")[0])
                filepath = os.path.join(pdf_dir, filename)

                if not os.path.exists(filepath):
                    print(f"Downloading {filename}...")
                    pdf_response = requests.get(pdf_url)
                    if pdf_response.status_code == 200:
                        with open(filepath, 'wb') as f:
                            f.write(pdf_response.content)
                        print(f"Successfully downloaded {filename}")
                    else:
                        print(f"Failed to download {filename}. Status: {pdf_response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing market website: {e}")

@price_app.route('/price')
def index():
    download_weekly_pdfs()

    # Get a list of all downloaded PDF files and their corresponding dates
    pdf_files = []
    if os.path.exists(pdf_dir):
        for pdf_filename in sorted(os.listdir(pdf_dir), reverse=True):
            try:
                date_part = pdf_filename.split('.')[0]
                # Handle different date formats like 'DD-M-YY' or 'DD-MM-YY'
                dt_obj = datetime.datetime.strptime(date_part, '%d-%m-%y')
                pdf_date = dt_obj.strftime('%d-%m-%Y')
                pdf_files.append((pdf_date, pdf_filename))
            except ValueError:
                print(f"Could not parse date from filename: {pdf_filename}. Skipping.")

    # Render the template with the list of PDF files
    return render_template('price.html', pdf_files=pdf_files)
