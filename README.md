![alt text](https://i.ibb.co/HV2x5P2/2022-04-17-16-06-08.png)
![alt text](https://i.ibb.co/McLwSyJ/2022-04-17-16-06-38.png)
![alt text](https://i.ibb.co/DK5SMKc/2022-04-17-16-06-23.png)


# Plotly Dash Flask 

Make Plotly Dash part of your Flask Application by following this example.

# Getting Started

Get set up locally in two steps:

### Environment Variables

Replace the values in **.env.example** with your values and rename this file to **.env**:

* `FLASK_APP`: Entry point of your application; should be `wsgi.py`.
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
$ git clone https://github.com/chigwell/dash-flask.git
$ cd plotlydash-flask
$ make deploy
``` 
or use docker:

### Docker
```shell
$ docker compose up
``` 

### Input file
The fields in the file will be separated by commas but each row will vary in length as described below.

A result will consist of:

1. A constituency
2. A repeating set of pairs with the party code and the votes cast

So for example:

    Cardiff West, 11014, C, 17803, L, 4923, UKIP, 2069, LD
    Islington South & Finsbury, 22547, L, 9389, C, 4829, LD, 3375, UKIP, 3371, G, 309, Ind

> **_NOTE:_** Constituency names containing a comma will be escaped as with '\\,'

We want to transform this into a standard API that shows, per constituency:

* the constituency name GET /api/constituencies
* translates the party code into a full name GET /api/party/<code>
* shows the total number of votes for each party GET /api/party/votes
* shows the share of the vote as a percentage of all the votes cast GET /api/votes/share
* shows who won the constituency GET /api/constituencies

One of the API endpoitns should show the results for the whole of the UK:
* number of total MPs per party GET /api/parliament-seats-per-party
* number of total votes per party GET /api/votes/share


### Codes

* C - Conservative
* L - Labour
* SNP - Scottish National Party
* LD - Liberal Democrats
* G - Green Party
* Ind - Independent



-----


