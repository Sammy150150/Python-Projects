import urllib.request

webUrl=urllib.request.urlopen('https://www.python.org/')

print("result: "+str(webUrl.getCode()))