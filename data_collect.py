import requests
from pathlib import Path
import json

MCGILL_SUBREDDIT = "https://www.reddit.com/r/mcgill/"
CONCORDIA_SUBREDDIT = "https://www.reddit.com/r/Concordia/"

def get_data(url, output_file):
    endpoint = url + "new.json"

    response = requests.get(endpoint, headers={'User-agent': 'your bot 0.1'})

    if not Path("data").exists():
        Path("data").mkdir()

    output_path = "data/" + output_file

    with open(output_path, "w") as output:
        json.dump(response.json(), output, indent=4)


get_data(MCGILL_SUBREDDIT, "mcgill.json")
get_data(CONCORDIA_SUBREDDIT, "concordia.json")

