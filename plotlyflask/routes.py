"""Routes for parent Flask app."""
import json
import pandas as pd
from flask import current_app as app
from flask import render_template, jsonify, make_response, redirect, request


@app.route("/")
def home():
    """Landing page."""
    return render_template(
        "index.jinja2",
        title="Elections",
        description="Elections.",
        template="home-template",
        body="This is a homepage served with Flask.",
    )


@app.route("/api/uploader", methods=['POST'])
def uploader():
    # TODO: check the uploaded file by the security
    f = request.files['file']
    f.save('data/input.csv')
    return redirect("/dashapp/", code=200)

# to get the winner

@app.route("/api/winner", methods=['GET'])
def get_winner():
    winner = pd.read_csv("data/winner.csv", sep=';')
    data = {
        'message': 'The winner is...',
        'status': 200,
        'data': json.loads(winner.to_json(orient = 'records'))
    }
    return make_response(jsonify(data))

# to get the constituencies
# shows who won the constituency

@app.route("/api/constituencies", methods=['GET'])
def get_constituencies():
    constituencies = pd.read_csv('data/constituencies.csv', sep=";")
    data = {
        'message': 'The list of constituencies',
        'status': 200,
        'data': json.loads(constituencies.to_json(orient = 'records'))
    }
    return make_response(jsonify(data))

# to get the party name by a code

@app.route("/api/party/<code>", methods=['GET'])
def get_party_full_name(code):
    parties = pd.read_csv('data/parties.csv', sep=";")
    party = parties.loc[parties['party_code'] == str(code)]
    data = {
        'message': 'The party full name by a code',
        'status': 200,
        'data': json.loads(party.to_json(orient = 'records'))
    }
    return make_response(jsonify(data))

# shows the total number of votes for each party

@app.route("/api/party/votes", methods=['GET'])
def get_party_votes():
    df_parties = pd.read_csv('data/parties.csv', sep=";")
    df_all_results = pd.read_csv("data/output.csv", parse_dates=["created"], sep=';')
    df_all_results['votes'] = df_all_results['votes'].astype('int')
    df_all_results = df_parties.merge(df_all_results, how='inner', on='party_code')
    df_all_results.rename(columns={'party_name_x': 'party_name'}, inplace=True)
    df_total_votes = df_all_results.groupby(['party_name', 'party_code'], as_index=False)[
        'votes'].sum()
    data = {
        'message': 'shows the total number of votes for each party ',
        'status': 200,
        'data': json.loads(df_total_votes.to_json(orient = 'records'))
    }
    return make_response(jsonify(data))

# shows the share of the vote as a percentage of all the votes cast

@app.route("/api/votes/share", methods=['GET'])
def get_votes_share():
    df_parties = pd.read_csv('data/parties.csv', sep=";")
    df_all_results = pd.read_csv("data/output.csv", parse_dates=["created"], sep=';')
    df_all_results['votes'] = df_all_results['votes'].astype('int')
    total_votes = df_all_results['votes'].sum()
    df_all_results = df_parties.merge(df_all_results, how='inner', on='party_code')
    df_all_results.rename(columns={'party_name_x': 'party_name'}, inplace=True)
    df_total_votes = df_all_results.groupby(['party_name', 'party_code'], as_index=False)[
        'votes'].sum()
    df_total_votes['percentage'] =  df_total_votes['votes'] * 100 / total_votes
    data = {
        'message': 'shows the total number of votes for each party ',
        'status': 200,
        'data': json.loads(df_total_votes.to_json(orient = 'records'))
    }
    return make_response(jsonify(data))

# number of total MPs per party

@app.route("/api/parliament-seats-per-party", methods=['GET'])
def get_parliament_seats_per_party():
    parties = pd.read_csv('data/parliament_seats.csv', sep=";")
    data = {
        'message': 'The number of total MPs per party',
        'status': 200,
        'data': json.loads(parties.to_json(orient = 'records'))
    }
    return make_response(jsonify(data))