class _User(object):
  def __init__(self, username: str):
    """Get user data."""
    self.username = username

  def userGraphQLDataFull(self) -> dict:
    # Grab data, return info
    example = {"karma": 102}
    return example
