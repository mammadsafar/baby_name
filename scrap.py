# import requests
# from bs4 import BeautifulSoup
# import json
# import time

# def extract_english_name(text):
#     start = text.find("(انگلیسی: ") + len("(انگلیسی: ")
#     end = text.find(")", start)
#     return text[start:end] if start != -1 and end != -1 else ""

# with open('names-1.json', 'r', encoding='utf-8') as f:
#     names = json.load(f)

# updated_names = []

# try:
#     while names:
#         name_info = names.pop(0)
#         link = name_info['link']
#         response = requests.get(link)
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         article = soup.find('article')
#         if article:
#             text = article.get_text()
#             english_name = extract_english_name(text)
#             name_info['english_name'] = english_name
#             print(f"Updated {name_info['name']} with English name: {english_name}")
        
#         updated_names.append(name_info)
        
#         with open('names_updated-1.json', 'w', encoding='utf-8') as f:
#             json.dump(updated_names, f, ensure_ascii=False, indent=4)
        
#         with open('names-1.json', 'w', encoding='utf-8') as f:
#             json.dump(names, f, ensure_ascii=False, indent=4)
        
#         time.sleep(3)

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     # ذخیره داده‌های نهایی در فایل‌های JSON
#     with open('names_updated-1.json', 'w', encoding='utf-8') as f:
#         json.dump(updated_names, f, ensure_ascii=False, indent=4)
#     with open('names-1.json', 'w', encoding='utf-8') as f:
#         json.dump(names, f, ensure_ascii=False, indent=4)
#     print("Data saved to names_updated-1.json and names-1.json")




# import requests
# from bs4 import BeautifulSoup
# import json
# import time
# import random

# def extract_english_name(text):
#     start = text.find("(انگلیسی: ") + len("(انگلیسی: ")
#     end = text.find(")", start)
#     return text[start:end] if start != -1 and end != -1 else ""

# def get_random_user_agent():
#     user_agents = [
#         'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
#         'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
#         'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#         'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
#     ]
#     return random.choice(user_agents)

# with open('names.json', 'r', encoding='utf-8') as f:
#     names = json.load(f)

# updated_names = []

# try:
#     while names:
#         name_info = names.pop(0)
#         link = name_info['link']
        
#         while True:
#             headers = {'User-Agent': get_random_user_agent()}
#             response = requests.get(link, headers=headers)
            
#             if response.status_code != 200:
#                 print(f"error: {response.status_code}. 1 min.")
#                 time.sleep(60) 
#                 continue

#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             if "صفحه مورد نظر قفل شده است. لطفا لحظاتی بعد مراجعه کنید." in soup.text:
#                 print("صفحه قفل شده است، 10 دقیقه صبر می‌کنیم.")
#                 time.sleep(600)  
#             else:
#                 break
        
#         article = soup.find('article')
#         if article:
#             text = article.get_text()
#             english_name = extract_english_name(text)
#             name_info['english_name'] = english_name
#             print(f"Updated {name_info['name']} with English name: {english_name}")
        
#         updated_names.append(name_info)
        
#         with open('names_updated-1.json', 'w', encoding='utf-8') as f:
#             json.dump(updated_names, f, ensure_ascii=False, indent=4)
        
#         with open('names.json', 'w', encoding='utf-8') as f:
#             json.dump(names, f, ensure_ascii=False, indent=4)
        
#         sleep_time = random.randint(5, 10)
#         sleep_time = sleep_time / 2
#         print(f"time slepp {sleep_time} sec.")
#         time.sleep(sleep_time)

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     with open('names_updated-1.json', 'w', encoding='utf-8') as f:
#         json.dump(updated_names, f, ensure_ascii=False, indent=4)
#     with open('names.json', 'w', encoding='utf-8') as f:
#         json.dump(names, f, ensure_ascii=False, indent=4)
#     print("Data saved to names_updated-1.json and names-1.json")

import requests
from bs4 import BeautifulSoup
import json
import time
import random


def random_sleep(number1, number2):
    return random.randint(number1, number2)

def extract_english_name(text):
    start = text.find("(انگلیسی: ") + len("(انگلیسی: ")
    end = text.find(")", start)
    return text[start:end] if start != -1 and end != -1 else ""

def get_random_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1'
    ]
    return random.choice(user_agents)
updated_names1 = 8
while True:
    updated_names1  = updated_names1 + 1
    with open('names-3.json', 'r', encoding='utf-8') as f:
        names = json.load(f)

    try:
        with open(f'names_updated-{updated_names1}.json', 'r', encoding='utf-8') as f:
            updated_names = json.load(f)
    except FileNotFoundError:
        updated_names = []

    request_counter = 0
    found_count = 0
    not_found_count = 0

    try:
        while names:
            name_info = names.pop(0)
            link = name_info['link']
            
            while True:
                headers = {'User-Agent': get_random_user_agent()}
                response = requests.get(link, headers=headers)
                
                if response.status_code != 200:
                    print(f"Error: {response.status_code}. Waiting 1 minute.")
                    time.sleep(60)
                    continue

                soup = BeautifulSoup(response.text, 'html.parser')
                
                if "صفحه مورد نظر قفل شده است. لطفا لحظاتی بعد مراجعه کنید." in soup.text:
                    print("Page locked. Waiting 10 minutes.")
                    time.sleep(600)
                else:
                    break
            
            article = soup.find('article')
            if article:
                text = article.get_text()
                english_name = extract_english_name(text)
                if english_name:
                    name_info['english_name'] = english_name
                    found_count += 1
                    print(f"Updated {name_info['name']} with English name: {english_name}, found count: {found_count}, not found count: {not_found_count}")
                else:
                    not_found_count += 1
                    print(f"English name not found for {name_info['name']}")
            else:
                not_found_count += 1
                print(f"No article found for {name_info['name']}")
            
            updated_names.append(name_info)
            
            with open(f'names_updated-{updated_names1}.json', 'w', encoding='utf-8') as f:
                json.dump(updated_names, f, ensure_ascii=False, indent=4)
            
            with open('names.json', 'w', encoding='utf-8') as f:
                json.dump(names, f, ensure_ascii=False, indent=4)
            
            request_counter += 1
            if request_counter == 40:
                print("Max requests (40) reached. Sleeping for 10-15 minutes.")
                sleep_time = random_sleep(600, 900)
                print(f"Sleeping for {sleep_time} seconds.")
                time.sleep(sleep_time)
                request_counter = 0 
            
            sleep_time = random_sleep(5, 10)
            print(f"Sleeping for {sleep_time} seconds.")
            time.sleep(sleep_time)

    except Exception as e:
        print(f" error : {e}")

    finally:
        new_names = []
        for name_info in names:
            if name_info not in updated_names:
                new_names.append(name_info)
        
        names = new_names
        
        with open(f'names_updated-{updated_names1}.json', 'w', encoding='utf-8') as f:
            json.dump(updated_names, f, ensure_ascii=False, indent=4)
        with open('names.json', 'w', encoding='utf-8') as f:
            json.dump(names, f, ensure_ascii=False, indent=4)
        print("Data saved to names_updated-1.json and names.json")


