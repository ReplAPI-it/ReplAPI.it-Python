from .base import BaseClass


class Post(BaseClass):
  def __init__(self, id: int, **kwargs):
    self.vars = {**{"id": id}, **kwargs}
    self._query_args = {"$id": "Int!"}
    self._types = {
      "post(id: $id)": [
        "id",
        "title",
        "body",
        "showHosted",
        "voteCount",
        "commentCount",
        "isPinned",
        "isLocked",
        "timeCreated",
        "timeUpdated",
        "url",
        "isAnnouncement",
        "isAuthor",
        "canEdit",
        "canComment",
        "canVote",
        "canPin",
        "canSetType",
        "canChangeBoard",
        "canLock",
        "hasVoted",
        "canReport",
        "hasReported",
        "isAnswerable",
        "tutorialPages",
      ]
    }
