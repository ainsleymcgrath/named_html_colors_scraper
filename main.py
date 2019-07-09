import json

import requests
from bs4 import BeautifulSoup

COLOR_CODES_URL = "https://htmlcolorcodes.com/color-names/"

response = requests.get(COLOR_CODES_URL)
soup = BeautifulSoup(response.text, "html.parser")


def get_attr_from_color_row(attr, row):
    return row.select_one("td.color-swatch div").get(attr)


color_info_dict = {
    section.get("id"): {
        color_row.select_one("td.color-name h4").text.lower(): {
            "hex": get_attr_from_color_row("data-hex", color_row),
            "rgb": get_attr_from_color_row("data-rgb", color_row),
            "hsl": get_attr_from_color_row("data-hsl", color_row),
        }
        for color_row in section.select("table tr.color")
    }
    for section in soup.select("article#names section")
    if section.select("table tr.color")
}


with open("COLORS.json", "w") as f:
    f.write(json.dumps(color_info_dict, indent=2))
