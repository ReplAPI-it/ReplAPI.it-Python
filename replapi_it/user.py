# -*- coding: utf-8 -*-
import json

import requests

getCyclesQuery = """
  karma
"""
headers = {
  "X-Requested-With": "ReplAPI-IT Team",
  "Referrer": "https://staging.replit.com/",
}
url = "https://staging.replit.com/graphql"


class _User(object):
  def __init__(self, username: str):
    """Get user data."""
    self.username = username

  def userGraphQLDataFull(self) -> dict:
    # example = {"karma": 102}
    # return example
    pass

  def getCycles(self) -> int:
    # Make body
    body = {
      "query": 'query UserData { userByUsername(username: "'
      + self.username
      + '") { '
      + getCyclesQuery
      + " } }"
    }
    # Get Data from graphql
    self.res = json.loads(requests.post(url, body, headers=headers).text)
    returnData = self.res
    # Check if user exists
    f = returnData
    f = f["data"]["userByUsername"]
    if f is None:
      # Error if user doesn't exist
      print("We couldn't fine the user that you were looking for! ")
      print("The username we revieved was: " + self.username)
      exit(0)
    del f  # Delete f because we don't need it
    returnData = returnData["data"]["userByUsername"]["karma"]  # Make data
    return returnData  # Return it!
