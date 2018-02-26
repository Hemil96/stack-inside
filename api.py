from bs4 import BeautifulSoup
import requests
import json

list_app_data = []
list_utilities = []
list_devops = []
list_b_tools = []

dic = {}


def techinside(company):
    del list_app_data[:]
    del list_utilities[:]
    del list_devops[:]
    del list_b_tools[:]
    dic.clear()
    try: #exception handling
        #getting html data into a variable named soup
        html_doc = requests.get("https://stackshare.io/"+company).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        try:
             #searching for particular div
             all_divs = soup.find_all("div", {"class": "show-layer-d"})
        except:
             return ("N/A")

        #categorizing data
        for div in all_divs:
            if "Application and Data" in div.text:
                app_data = div
                for a in app_data.find_all('a',{"data-hint":True}):
                    list_app_data.append(a['data-hint'])
            elif "Utilities" in div.text:
                utilities = div
                for a in utilities.find_all('a',{"data-hint":True}):
                    list_utilities.append(a['data-hint'])

            elif "DevOps" in div.text:
                devops = div
                for a in devops.find_all('a',{"data-hint":True}):
                    list_devops.append(a['data-hint'])

            elif "Business Tools" in div.text:
                b_tools = div
                for a in b_tools.find_all('a',{"data-hint":True}):
                    list_b_tools.append(a['data-hint'])

        #making response dict
        if len(list_app_data)!=0:dic["app_data"] = list_app_data
        if len(list_utilities)!=0:dic["utilitites"] = list_utilities
        if len(list_devops)!=0:dic["devops"] = list_devops
        if len(list_b_tools)!=0:dic["b_tools"] = list_b_tools
        if len(dic)!= 0: 
            print dic 
            return json.dumps(dic)
        else:
            return ("N/A")
    except:
        return ("N/A")

techinside("apple")