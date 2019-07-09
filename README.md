# Named HTML Colors Scraper

For whatever reason I've always been enamored with all the HTML colors that have names.

Running `python main.py` (after installing requirements) gwill produce a JSON file containing data scraped from <https://htmlcolorcodes.com/color-names/>.

The JSON looks like this:

```json
{
  "gray": {
    "gainsboro": {
      "hex": "#DCDCDC",
      "rgb": "220, 220, 220",
      "hsl": "0, 0%, 86%"
    },
    "lightgray": {
      "hex": "#D3D3D3",
      "rgb": "211, 211, 211",
      "hsl": "0, 0%, 83%"
    }
  },
  "blue": {
    "aqua": {
      "hex": "#00FFFF",
      "rgb": "0, 255, 255",
      "hsl": "180, 100%, 50%"
    },
    "cyan": {
      "hex": "#00FFFF",
      "rgb": "0, 255, 255",
      "hsl": "180, 100%, 50%"
    }
  }
}
```