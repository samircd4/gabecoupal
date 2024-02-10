import pandas as pd
import json
import requests
from rich import print
from datetime import datetime, timedelta



def get_data(date):
    cookies = {
        'GCLB': 'CJfK1e6O38W09gE',
        'tr-plan-id': '0',
        'tr-plan-name': 'free',
        'tr-experiments-version': '1.14',
        'tipranks-experiments': '%7b%22Experiments%22%3a%5b%7b%22Name%22%3a%22general_A%22%2c%22Variant%22%3a%22v2%22%2c%22SendAnalytics%22%3afalse%7d%2c%7b%22Name%22%3a%22general_B%22%2c%22Variant%22%3a%22v3%22%2c%22SendAnalytics%22%3afalse%7d%5d%7d',
        'tipranks-experiments-slim': 'general_A%3av2%7cgeneral_B%3av3',
        'rbzid': 'C+IbOQhZX4S7SSTGnC/ZB4PrQ+/aJzkeWtGC5BrH9xdCEwHLoqPO8n8ABEA3z9kwfsr8OpsA9TqvPJRVtaBds+aIPBSSPA/wUlEJbqRoszqcdbFtioiUNWdf4UF08Uz14Op/I64JJY5wAlWeMKqu2bGU7UyoOemQ/SIpELICCNtcDJ+g7OeZWbgcJPBA1q/NKnXj020oBsqxBqs1Way0PGcCIIq6v3zn35VM1Pog4AGKmgAQc2hQ5MuU5ZwNVjhsaHb4/INeoS3vlJIARUtTHA==',
        'rbzsessionid': '176f49350fcf74f47e79b83d780d2137',
        'FPAU': '1.2.398134983.1707500665',
        '_gcl_au': '1.1.7277293.1707500661',
        '_gid': 'GA1.2.1351930360.1707500661',
        '_fbp': 'fb.2.1707500660078.797420682',
        'prism_90278194': 'e19f2ddc-0479-4969-8cc5-f3846d9a1f63',
        '_ce.irv': 'new',
        'cebs': '1',
        '_ce.clock_event': '1',
        '_ce.clock_data': '-3854%2C118.179.97.193%2C1%2C9fea701a627a57d0c458db2e1cb60d62',
        '_fbp': 'fb.2.1707500660078.797420682',
        'DontShowNewScreenerPopup': 'true',
        '_ga': 'GA1.1.1393155927.1707500661',
        'x-ms-routing-name': 'self',
        'TiPMix': '69.33533060696546',
        'cebsp_': '11',
        'g_state': '{"i_p":1707602733980,"i_l":2}',
        '_ce.s': 'v~a7f17d47ce05ad4aa689fd3149fe031f39e5e998~lcw~1707516491036~lva~1707500663762~vpv~0~v11.cs~435987~v11.s~de833470-c791-11ee-a025-b72e08ef8828~v11.sla~1707516491631~lcw~1707516491632',
        '_ga_FFX3CZN1WY': 'GS1.1.1707516313.4.1.1707516491.0.0.0',
    }

    headers = {
        'authority': 'www.tipranks.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
        # 'cookie': 'GCLB=CJfK1e6O38W09gE; tr-plan-id=0; tr-plan-name=free; tr-experiments-version=1.14; tipranks-experiments=%7b%22Experiments%22%3a%5b%7b%22Name%22%3a%22general_A%22%2c%22Variant%22%3a%22v2%22%2c%22SendAnalytics%22%3afalse%7d%2c%7b%22Name%22%3a%22general_B%22%2c%22Variant%22%3a%22v3%22%2c%22SendAnalytics%22%3afalse%7d%5d%7d; tipranks-experiments-slim=general_A%3av2%7cgeneral_B%3av3; rbzid=C+IbOQhZX4S7SSTGnC/ZB4PrQ+/aJzkeWtGC5BrH9xdCEwHLoqPO8n8ABEA3z9kwfsr8OpsA9TqvPJRVtaBds+aIPBSSPA/wUlEJbqRoszqcdbFtioiUNWdf4UF08Uz14Op/I64JJY5wAlWeMKqu2bGU7UyoOemQ/SIpELICCNtcDJ+g7OeZWbgcJPBA1q/NKnXj020oBsqxBqs1Way0PGcCIIq6v3zn35VM1Pog4AGKmgAQc2hQ5MuU5ZwNVjhsaHb4/INeoS3vlJIARUtTHA==; rbzsessionid=176f49350fcf74f47e79b83d780d2137; FPAU=1.2.398134983.1707500665; _gcl_au=1.1.7277293.1707500661; _gid=GA1.2.1351930360.1707500661; _fbp=fb.2.1707500660078.797420682; prism_90278194=e19f2ddc-0479-4969-8cc5-f3846d9a1f63; _ce.irv=new; cebs=1; _ce.clock_event=1; _ce.clock_data=-3854%2C118.179.97.193%2C1%2C9fea701a627a57d0c458db2e1cb60d62; _fbp=fb.2.1707500660078.797420682; DontShowNewScreenerPopup=true; _ga=GA1.1.1393155927.1707500661; x-ms-routing-name=self; TiPMix=69.33533060696546; cebsp_=11; g_state={"i_p":1707602733980,"i_l":2}; _ce.s=v~a7f17d47ce05ad4aa689fd3149fe031f39e5e998~lcw~1707516491036~lva~1707500663762~vpv~0~v11.cs~435987~v11.s~de833470-c791-11ee-a025-b72e08ef8828~v11.sla~1707516491631~lcw~1707516491632; _ga_FFX3CZN1WY=GS1.1.1707516313.4.1.1707516491.0.0.0',
        'referer': 'https://www.tipranks.com/calendars/dividends/2024-02-02/canada',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    response = requests.get(
        f'https://www.tipranks.com/calendars/dividends/{date}/canada/payload.json',
        cookies=cookies,
        headers=headers,
    )
    try:
        data = json.loads(response.text)['data']['tableData']
        items = []
        for d in data:
            item = {}
            ticker = d['ticker']
            date_string = d['nextDividend']['executionDate']
            # Convert string to datetime object
            date_object = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
            # Format datetime object to desired format
            formatted_date = date_object.strftime('%d-%b-%y')
            yield_r = float(d['nextDividend']['yield']) if d['nextDividend']['yield'] != None else 0
            
            item['ticker'] = ticker
            item['ex_date'] = formatted_date
            item['yield'] = round(yield_r*100,2)
            print(item)
            items.append(item)
        print(f'{date} data has been added!')
        return items
    except TypeError as e:
        print(f'{date} has no data!')
        return None

if __name__ == "__main__":
    # date = '2024-02-15'
    today = datetime.today().date()
    # Convert the string to a datetime object
    date_obj = datetime.strptime(str(today), '%Y-%m-%d')

    # Calculate the end date after adding 7 days
    end_date = date_obj + timedelta(days=30)

    # Initialize the current date with the start date
    current_date = date_obj
    # Loop through and get data for each date
    data = []
    while current_date <= end_date:
        s_data = get_data(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
        if s_data != None:
            for s in s_data:
                data.append(s)
    
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)