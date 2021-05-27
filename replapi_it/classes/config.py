import json
import os

default = {"graphql_url": "https://staging.replit.com/graphql"}


def _config(filename: str = "replapi_it.json") -> dict:
  if os.path.isfile(filename):
    with open(filename, "rt") as fp:
      return json.load(fp)
  else:
    return {}


config = {**default, **_config()}
