from bs4 import BeautifulSoup 
import requests
import time 
import random
import pandas as pd
import re

url_base = 'https://sizeer.lv/viriesiem/apavi/nike?page='
nike = []

count = 1
while count <= 4:
    url = url_base + str(count)
    print(url)
    
    #Bloķēt pieprasījumus no web-site!!!
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'} 
    response = requests.get(url, headers=headers) 

    if response.status_code == 200:
        html_soup = BeautifulSoup(response.text, 'html.parser')
        nike_data = html_soup.find_all('div', class_="item-container")
        
        #Izlases pārslodzes ģenerēšana, lai samazinātu pieprasījuma slodzi
        if nike_data:
            nike.extend(nike_data) 
            value = random.random()
            scaled_value = 1 + (value * (9 - 5))
            print(scaled_value)
            time.sleep(scaled_value)
            count += 1
        else:
            print('No data found on the page.')
            break
    elif response.status_code == 403:
        print(f"Access denied: {response.status_code}") #izeja, ja piekļuve ir liegta
        break
    else:
        print(f"Failed: {response.status_code}")
        print(response.text)  #Kļūdu izvade, ja nepieciešams
        break

#Izveidot DataFrame datu sarakstu
data = []
for info in nike:
    shoes = info.find('a', class_='item-name')
    shoes_price = info.find('p', class_='item-price')

    if shoes and shoes_price:
        name = shoes.text.strip()

        #Regulārās izteiksmes, lai no cenu virknes iegūtu skaitliskās vērtības
        price_math = re.search(r'\d+(\.\d{1,2})?', shoes_price.text.strip())
        price = float(price_math.group()) if price_math else None

        
        print(f"Title: {name}, Price: {price}")

        #Pārbaudiet, vai produkta nosaukums sākas ar "NIKE AIR MAX" cena ir mazāka par 160
        if "NIKE AIR MAX" in name and price is not None and price < 160:
            data.append({'Title': name, ' Price': price})


print(data)

#Izveidot DataFrame no datu saraksta
df = pd.DataFrame(data)

#Datu rāmja saglabāšana CSV failā
df.to_csv('NIKE_AIR_MAX.csv', index=False)


print(df.head())
