from bs4 import BeautifulSoup
import requests
import json

list_app_data = []
list_utilities = []
list_devops = []
list_b_tools = []

data = {
        "Application and Data" : list_app_data,
        "Utilities":list_utilities,
        "DevOps":list_devops,
        "Business Tools":list_b_tools
        }


def techinside(company):
    try:
        html_doc = requests.get("https://stackshare.io/"+company).text
        soup = BeautifulSoup(html_doc, 'html.parser')
        outer_div = soup.find(id="all-tools")
        all_divs = soup.find_all("div", {"class": "show-layer-d"})
        for div in all_divs:
            if "Application and Data" in div.text:
                app_data = div
            elif "Utilities" in div.text:
                utilities = div
            elif "DevOps" in div.text:
                devops = div
            elif "Business Tools" in div.text:
                b_tools = div

        for a in app_data.find_all('a'):
            try:
                list_app_data.append(a['data-hint'])
            except:
                pass
        for a in utilities.find_all('a'):
            try:
                list_utilities.append(a['data-hint'])
            except:
                pass
        for a in devops.find_all('a'):
            try:
                list_devops.append(a['data-hint'])
            except:
                pass
        for a in b_tools.find_all('a'):
            try:
                list_b_tools.append(a['data-hint'])
            except:
                pass
        return json.dumps(data)
    except:
        return 'n/a'
