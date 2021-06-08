import json

import requests
from jinja2 import Template

from .config import config

_query_template = """
query Main({% for i in query_args %}{{ i }}: {{ query_args[i] }}, {% endfor %}) {
  {% for i in types %}
  {{ i }} {
    {% for field in types[i] %}
    {{ field }}
    {% endfor %}
  }
  {% endfor %}
}
""".strip()

_default_headers = {
  "X-Requested-With": "ReplAPI-It-Python",
  "referrer": config["graphql_url"],
}


class BaseClass(object):
  def __init__(self, vars: dict = {}, **kwargs):
    self.vars = {**vars, **kwargs}
    self._query_args = {"$username": "String!"}
    self._types = {"userByUsername(username: $username)": ["fullName", "karma"]}

  @property
  def config(self) -> dict:
    return config

  def query(self) -> str:
    tm = Template(_query_template)

    return tm.render(query_args=self._query_args, types=self._types)

  def collect_raw(self):
    req = requests.post(
      self.config["graphql_url"],
      data={"query": self.query(), "variables": json.dumps(self.vars)},
      headers=_default_headers,
    )

    return req.text

  def collect(self):
    return json.loads(self.collect_json())
