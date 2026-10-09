import requests
import time

url = 'https://www.random.org/integers/?num=5&min=1&max=6&col=1&base=10&format=plain&rnd=new' 

while True:
    response = requests.get(url)
    html_content = response.text
    randomNumList = [int(randomNum) for randomNum in html_content.split()]
    print(randomNumList)
    time.sleep(2)
