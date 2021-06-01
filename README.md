> **Notice:** Currently this project is just a framework. It does not work yet.
> If you wan't to get updated when 1.0.0 is released, then click Watch -> Custom -> Releases -> Apply

[![Contributors](https://img.shields.io/github/contributors/ReplAPI-it/ReplAPI.it-Python?style=for-the-badge)](https://github.com/ReplAPI-it/ReplAPI.it-Python/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/ReplAPI-it/ReplAPI.it-Python?style=for-the-badge)](https://github.com/ReplAPI-it/ReplAPI.it-Python/network/members)
[![Stargazers](https://img.shields.io/github/stars/ReplAPI-it/ReplAPI.it-Python?style=for-the-badge)](https://github.com/ReplAPI-it/ReplAPI.it-Python/stargazers)
[![Issues](https://img.shields.io/github/issues/ReplAPI-it/ReplAPI.it-Python?style=for-the-badge)](https://github.com/ReplAPI-it/ReplAPI.it-Python/issues)
[![License](https://img.shields.io/github/license/ReplAPI-it/ReplAPI.it-Python?style=for-the-badge)](https://github.com/ReplAPI-it/ReplAPI.it-Python/blob/master/LICENSE)
[![Downloads on PyPI](https://img.shields.io/pypi/dw/replapi-it?style=for-the-badge)](https://pypi.org/project/replapi-it/)
[![Ballad Test](https://img.shields.io/github/workflow/status/ReplAPI-it/ReplAPI.it-Python/Ballad%20Test?style=for-the-badge)](https://github.com/ReplAPI-it/ReplAPI.it-Python/actions/workflows/balladtest.yml)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/ReplAPI-it/ReplAPI.it-Python">
    <img src="images/logo.jpg" alt="Logo" width="600" height="200">
  </a>

  <h3 align="center">ReplAPI.it</h3>

  <p align="center">
    A Simple and Complete Replit API Package
    <br />
    <a href="https://replapi-it.js.org"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://pypi.org/project/replapi-it/">View Package on PyPI</a>
    ·
    <a href="https://github.com/ReplAPI-it/ReplAPI.it-Python/issues">Report Bug</a>
    ·
    <a href="https://github.com/ReplAPI-it/ReplAPI.it-Python/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Code Screenshot](images/screenshot.jpg)](https://replit.com/@ReplAPIit/Package) -->

The Replit GraphQL API is an extraordinary way to make projects unique and special, yet with the numerous packages available few such projects have been made. Why would that be? Most likely due to how complicated writing code can get and the limitations of their queries. My package, **ReplAPI.it**, changes that with a simple to use structure and many queries, some of which are:

* Queries for Data on Users (such as Profile, Posts, Comments)
* Queries for Data on Posts (such as Upvoters, Content)
* Queries for Data on Repls (such as Files, Comments)
* Mutations for Commenting, Reporting, and Posting
* Queries for Data on Leaderboard (with filters such as cycles since)
* and lots more!

This package is also simple to use with it's **class-based structure**. Simply create a new class for your User, Post, or whatever your heart desires and use built in functions with options to query data **your way**.

### Built With

* [Python](https://www.python.org/)

<!--
## Getting Started

I suggest requiring the ReplAPI.it module until ES imports in Python are stabilized.

### Prerequisites

If you have not already download npm:
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Install the latest version of the package
   ```sh
   $ npm install replapi-it
   ```
2. Require the package in your code
   ```js
   import ReplAPI from 'replapi-it';
   ``` 
3. Initilize the package
   ```js
   const replapi = ReplAPI({
      username: 'your-username-here'
   });
   ```

## Usage

Using ReplAPI.it is very simple! Let's create a simple user and ask for their cycles:
 ```js
 import ReplAPI from 'replapi-it';
 const replapi = ReplAPI({
   username: 'your-username-here'
 });
 
 const myUser = new replapi.User("RayhanADev");

 async function getCycles() {
   let info = await myUser.userGraphQLDataFull();
   let cycles = info.karma; // Yep, it's karma!
   console.log(`User Cycles: ${cycles}`)
 }
 
 getCycles()
 ```

Output:
 ```
 User Cycles: 1008
 ```


That was fun! Now how about getting a specific post? Let's create a simple post and ask for it's title:
 ```js
 import ReplAPI from 'replapi-it';
 const replapi = ReplAPI({
   username: 'your-username-here'
 });

 const myPost = new replapi.Post(78043);

 async function getTitle() {
   let info = await myPost.postDataFull();
   let title = info.title;
   console.log(`Post Title: ${title}`)
 }
 
 getTitle()
 ```
Output:
 ```
 Post Title: Presenting... 🤔 RayhanADev 🤔? (GraphQL Success!)
 ```

_For more examples, please refer to the [Documentation](https://replapi-it.js.org)_

## Roadmap

See the [open issues](https://github.com/RayhanADev/ReplAPI.it-Python/issues) for a list of proposed features (and known issues).

I'm considering adding in support for Crosis communications after they distribute developer keys again. Right now I'm experimenting with WSS and eval.repl.it for code execution!
-->

## Contributing

Contributions are **much appreciated**, and if you have a cool idea that feels right in this package then you should check out our [contributing](.github/CONTRIBUTING.md) page.

## License

Distributed under the GPL-3.0 License. See [`LICENSE`](https://github.com/ReplAPI-it/ReplAPI.it-Python/blob/master/LICENSE) for more information.

## Contact

- BD103 - [@BD103](https://replit.com/@BD103) - dont@stalk.me
- JBYT27 - [@JBYT27](https://replit.com/@JBYT27) - beol0127@gmail.com
- darkdarcool - [@Darkdarcool](https://replit.com/@darkdarcool) - darkdarcool@gmail.com
- RayhanADev - [@RayhanADev](https://replit.com/@RayhanADev) - rayhanadev@protonmail.com

Project Link: [https://github.com/ReplAPI-it/ReplAPI.it-Python](https://github.com/ReplAPI-it/ReplAPI.it-Python)

## Acknowledgements





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ReplAPI-it/ReplAPI.it-Python.svg?style=for-the-badge
[contributors-url]: https://github.com/ReplAPI-it/ReplAPI.it-Python/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ReplAPI-it/ReplAPI.it-Python.svg?style=for-the-badge
[forks-url]: https://github.com/ReplAPI-it/REPLAPI.it-Python/network/members
[stars-shield]: https://img.shields.io/github/stars/ReplAPI-it/ReplAPI.it-Python.svg?style=for-the-badge
[stars-url]: https://github.com/ReplAPI-it/ReplAPI.it-Python/stargazers
[issues-shield]: https://img.shields.io/github/issues/ReplAPI-it/ReplAPI.it-Python.svg?style=for-the-badge
[issues-url]: https://github.com/ReplAPI-it/ReplAPI.it-Python/issues
[license-shield]: https://img.shields.io/github/license/ReplAPI-it/ReplAPI.it-Python.svg?style=for-the-badge
[license-url]: https://github.com/ReplAPI-it/ReplAPI.it-Python/blob/master/LICENSE.txt
[downloads-shield]: https://img.shields.io/pypi/dw/replapi-it?style=for-the-badge
[downloads-url]: https://pypi.org/project/replapi-it/
