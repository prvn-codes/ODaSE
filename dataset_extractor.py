import requests

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}



sample = open("sample.txt",'w')

sample.write(requests.get(url="https://www.kaggle.com/datasets",headers=headers).text)