# Dasboard - AI

![Python](https://img.shields.io/badge/Python-^3.9-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Flask](https://img.shields.io/badge/Flask^2.2.3-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Flask-Assets](https://img.shields.io/badge/Flask--Assets-v2.0-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Pandas](https://img.shields.io/badge/Pandas-v^2.0.0-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Dash](https://img.shields.io/badge/Dash-v^2.9.3-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![Plotly](https://img.shields.io/badge/Plotly-v^5.14.1-blue.svg?longCache=true&logo=python&longCache=true&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c)
[![GitHub Issues](https://img.shields.io/github/issues/DeibydCarranza/Dashboard-AI.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/DeibydCarranza/Dashboard-AI/issues)
[![GitHub Stars](https://img.shields.io/github/stars/DeibydCarranza/Dashboard-AI.svg?style=flat-square&colorB=ebcb8b&colorA=4c566a)](https://github.com/DeibydCarranza/Dashboard-AI/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/DeibydCarranza/Dashboard-AI.svg?style=flat-square&colorA=4c566a&colorB=ebcb8b)](https://github.com/DeibydCarranza/Dashboard-AI/network)


<p align="center">
  <img src="./.github/logo.jpg" width="200px">
</p>

Dashboard made from the Python framework called Dash for graphs.

Using Python for BackEnd interpretation and JS, CSS3 & HTML for FrontEnd configuration.

![Panel](./.github/dash@2x.jpg?raw=true)

# Getting Started

Get set up locally in two steps:

### Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `FLASK_ENV`: The environment in which to run your application; either `development` or `production`.
* `SECRET_KEY`: Randomly generated string of characters used to encrypt your app's data.
* `LESS_BIN` *(optional for static assets)*: Path to your local LESS installation via `which lessc`.
* `ASSETS_DEBUG` *(optional)*: Debug asset creation and bundling in `development`.
* `LESS_RUN_IN_DEBUG` *(optional)*: Debug LESS while in `development`.
* `COMPRESSOR_DEBUG` *(optional)*: Debug asset compression while in `development`.


*Remember never to commit secrets saved in .env files to Github.*

### Installation

Get up and running with `make deploy`:

```shell
$ git clone https://github.com/DeibydCarranza/Dashboard-AI.git
$ cd Dashboard-AI
$ make deploy
``` 

-----

### Prerequisites to modify

```shell
$ sudo apt-get install python3-pip
$ sudo apt install npm
$ sudo npm install -g less
$ pip install lesscpy
$ export PATH=$PATH:/usr/local/bin/lessc

``` 
* **Tutorial**: https://hackersandslackers.com/plotly-dash-with-flask/