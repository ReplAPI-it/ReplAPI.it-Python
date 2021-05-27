from .base import BaseClass


class User(BaseClass):
  def __init__(self, username: str, **kwargs):
    self.vars = {**{"username": username}, **kwargs}
    self._query_args = {"$username": "String!"}
    self._types = {
      "userByUsername(username: $username)": [
        "id",
        "username",
        "firstName",
        "lastName",
        "bio",
        "isVerified",
        "displayName",
        "fullName",
        "url",
        "isLoggedIn",
        "isSubscribed",
        "timeCreated",
        "isBannedFromBoards",
        "karma",
        "isHacker",
        "image",
      ]
    }
