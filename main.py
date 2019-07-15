import json

import requests
from bs4 import BeautifulSoup

COLOR_CODES_URL = "https://htmlcolorcodes.com/color-names/"

response = requests.get(COLOR_CODES_URL)
soup = BeautifulSoup(response.text, "html.parser")

sections_with_color_codes = soup.select("article#names section")
color_info_dict = {}


def list_from_color_table(color_table):
    output_list = []
    for row in color_table:
        output_list.append(row.select_one("td.color-name h4").text)

    return output_list


for section in sections_with_color_codes:
    color_table = section.select("table tr.color")

    if color_table is not None:
        color_group_name = section.get("id")
        color_info_dict[color_group_name] = list_from_color_table(color_table)


with open("COLORS.json", "w") as f:
    f.write(json.dumps(color_info_dict, indent=2))
