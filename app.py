import os
import psycopg2
from psycopg2.errors import DivisionByZero
from dotenv import load_dotenv
import db

DATABASE_PROMPT = "Enter the DATABASE_URI value or leave empty to load from .env file: "
MENU_PROMPT = """-- Menu --

1) Create new poll
2) List open polls
3) Vote on a poll
4) Show poll votes
5) Select a random winner from a poll option
6) Exit

Enter your choice: """

NEW_OPTION_PROMPT = "Enter new option text (or leave empty to stop adding options): "

def prompt_create_poll(connection):# Create Poll
    poll_title = input("Enter poll title: ")
    poll_owner = input("Enter poll owner: ")
    options = []

    while (new_option := input(NEW_OPTION_PROMPT)):
        options.append(new_option)
    db.create_poll(connection, poll_title, poll_owner, options)


def list_open_polls(connection):# Select * from polls
    polls = db.get_polls(connection)
    for poll in polls:
        print(f"{poll[0]}: {poll[1]} (created by {poll[2]})")


def prompt_vote_poll(connection):
    print(f"Below are the Poll ID's available:") 
    list_open_polls(connection)
    poll_id = int(input("Enter poll would you like to vote on: "))

    poll_options = db.get_poll_details(connection, poll_id)
    for option in poll_options:# From the Join we need only columns related to options- id, option_text 
        print(f"{option[3]}: {option[4]}")

    option_id = int(input("Enter option you'd like to vote for: "))
    username = input("Enter the username you'd like to vote as: ")
    db.add_poll_vote(connection, username, option_id)


def show_poll_votes(connection):
    poll_id = int(input("Enter poll you would like to see votes for: "))
    try:
        poll_and_votes = db.get_poll_and_vote_results(connection, poll_id)
    except DivisionByZero:
        print("No votes yet cast for this poll.")
    else:
        for result in poll_and_votes:
            print(f"{result[1]} got {result[2]} votes ({result[3]:.2f}% of total)")


MENU_OPTIONS = {
    "1": prompt_create_poll,
    "2": list_open_polls,
    "3": prompt_vote_poll,
    "4": show_poll_votes,
    #"5": randomize_poll_winner
}


def menu():
    database_uri = input(DATABASE_PROMPT)
    if not database_uri:
        load_dotenv()
        database_uri = os.environ["DATABASE_URI"]
        
    connection = psycopg2.connect(database_uri)
    db.create_tables(connection)

    while (selection := input(MENU_PROMPT)) != "6":
        try:
            MENU_OPTIONS[selection](connection)
        except KeyError:
            print("Invalid input selected. Please try again.")


menu()