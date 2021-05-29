# Contributing

> This is a quick guide to contributing. If you want more information on developing this project, then check out the [Wiki](https://github.com/ReplAPI-it/ReplAPI.it-Python/wiki).

Contributing is open and welcome here are ReplAPI.it-Python, but there are a few rules below to follow! You are planning to contribute, there are a few preparations and rules to follow that are below, please take time to read them!

To contribute, first fork and clone.

```sh
$ git clone https://github.com/ReplAPI-it/ReplAPI.it-Python.git
```

Install the dependencies next.

```sh
$ poetry install
```

Edit the code, then lint and test.

```sh
$ black .
$ isort .
$ flake8
```

Create your PR is all the checks pass! All commits should follow [Conventional Commits](https://www.conventionalcommits.org). (Look at the commit history for examples.) Thanks for helping!
