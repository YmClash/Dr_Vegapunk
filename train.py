import os
import pprint
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
my_api_key = os.getenv('CUSTUM_SEARCH_API_KEY')
my_cs_id = os.getenv('CUSTUM_SEARCH_ID')



def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'stackoverflow site:en.wikipedia.org', my_api_key, my_cs_id, num=10)
for result in results:
    pprint.pprint(result)