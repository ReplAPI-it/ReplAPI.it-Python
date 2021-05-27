from . import classes

defaultInitVars = {"username": None}


class ReplAPI(object):
  """Base class for all ReplAPI-it features.
    Everything should be accessed through this class.
    Do not import anything else unless you know what you are doing."""

  def __init__(self, initVars: dict = {}):
    self.vars = {**defaultInitVars, **initVars}

    self.User = classes.User
    self.Post = classes.Post
