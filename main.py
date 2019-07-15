import json

import requests
from bs4 import BeautifulSoup

COLOR_CODES_URL = "https://htmlcolorcodes.com/color-names/"

response = requests.get(COLOR_CODES_URL)
soup = BeautifulSoup(response.text, "html.parser")


def list_from_color_table(color_table):
    output_list = []
    for row in color_table:
        output_list.append(row.select_one("td.color-name h4").text)

    return output_list


color_info_dict = {
    section.get("id"): list_from_color_table(section.select("table tr.color"))
    for section in soup.select("article#names section")
    if section.select("table tr.color")
}


with open("COLORS.json", "w") as f:
    f.write(json.dumps(color_info_dict, indent=2))
