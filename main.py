import json
from collections import ChainMap

import requests
from bs4 import BeautifulSoup

COLOR_CODES_URL = "https://htmlcolorcodes.com/color-names/"

response = requests.get(COLOR_CODES_URL)
soup = BeautifulSoup(response.text, "html.parser")

color_groups = soup.select("article#names section")


def get_attr_from_color_row(attr, row):
    return row.select_one("td.color-swatch div").get(attr)


def color_info_dict_generator(color_sections):
    for section in color_sections:
        if section.select("table tr.color"):
            yield {
                section.get("id"): {
                    color_row.select_one("td.color-name h4").text.lower(): {
                        "hex": get_attr_from_color_row("data-hex", color_row),
                        "rgb": get_attr_from_color_row("data-rgb", color_row),
                        "hsl": get_attr_from_color_row("data-hsl", color_row),
                    }
                    for color_row in section.select("table tr.color")
                }
            }


merged_dict_of_color_info = dict(ChainMap(*color_info_dict_generator(color_groups)))

with open("COLORS.json", "w") as f:
    f.write(json.dumps(merged_dict_of_color_info, indent=2))
