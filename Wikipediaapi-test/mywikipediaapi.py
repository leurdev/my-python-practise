import wikipediaapi
import sys
import pandas as pd

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
)

wiki_result = wiki_wiki.page("alien")


print(wiki_result.text)
