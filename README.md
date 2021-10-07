# python-app-vote
It is a Voting Python App. You can create Poll, its option and enable users to vote for a particular option.
The code is self explanatory.

```
% /usr/local/bin/python3 /Users/parjun8840/Documents/My_Python/python-app-vote/app.py
Enter the DATABASE_URI value or leave empty to load from .env file: 
-- Menu --

1) Create new poll
2) List open polls
3) Vote on a poll
4) Show poll votes
5) Select a random winner from a poll option
6) Exit

Enter your choice: 2
-- Menu --

1) Create new poll
2) List open polls
3) Vote on a poll
4) Show poll votes
5) Select a random winner from a poll option
6) Exit

Enter your choice: 1
Enter poll title: Python Framework        
Enter poll owner: Arjun
Enter new option text (or leave empty to stop adding options): Django
Enter new option text (or leave empty to stop adding options): Flask
Enter new option text (or leave empty to stop adding options): Tornado
Enter new option text (or leave empty to stop adding options): Falcon 
Enter new option text (or leave empty to stop adding options): 
-- Menu --

1) Create new poll
2) List open polls
3) Vote on a poll
4) Show poll votes
5) Select a random winner from a poll option
6) Exit

Enter your choice: 2
1: Python Framework (created by Arjun)
-- Menu --

1) Create new poll
2) List open polls
3) Vote on a poll
4) Show poll votes
5) Select a random winner from a poll option
6) Exit

Enter your choice: 3
Below are the Poll ID's available:
1: Python Framework (created by Arjun)
Enter poll would you like to vote on: 1
1: Django
2: Flask
3: Tornado
4: Falcon
Enter option you'd like to vote for: 2
Enter the username you'd like to vote as: parjun8840
-- Menu --

1) Create new poll
2) List open polls
3) Vote on a poll
4) Show poll votes
5) Select a random winner from a poll option
6) Exit

Enter your choice: 4
Enter poll you would like to see votes for: 1
Django got 0 votes (0.00% of total)
Flask got 1 votes (100.00% of total)
Tornado got 0 votes (0.00% of total)
Falcon got 0 votes (0.00% of total)
-- Menu --

1) Create new poll
2) List open polls
3) Vote on a poll
4) Show poll votes
5) Select a random winner from a poll option
6) Exit

Enter your choice: 

```
