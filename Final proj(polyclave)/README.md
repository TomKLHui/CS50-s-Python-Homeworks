# Guess Who? A simple polyclave classifier
#### Video Demo:  <https://youtu.be/M34nZ5QtXK0>
#### Description:
This is a simple script that
1.Takes in the Guess who Excel info sheet as csv file
2.Choose one of the most informative characteristic to
3.Ask a yes/no question and does the filter (It’s okay to be unsure!); and finally
4.Output the final guess if your information is sufficient/ a list of possibilities if not

"Guess Who?" is a two-player board game in which players each guess the identity of the other's chosen character. The player who pinpoint opponent's identity with fewer questions wins.
The best way to *guarantee* fewest questions asked is to carefully ask questions which split the set of possibilities in half.

The reason is as follows:
Assume X is the proportion of characters fitting the criteria and 1-X the proportion of characters that does not fit.
After asking the question, the probability remove X of total characters is 1-X and the probability remove 1-X of total characters is X.
The expected removal of character as proportion=  X(1-X)+(1-X)X= 2X(1-X), which reaches its maximum when X=0.5

In short, overly specific question is too risky to ask and likely to be unhelpful.
So, in order to optimise the question asking, this script automatically selects the most efficient questions to ask, and allow the fleibility to be unsure which one the target should categorize into.
The main preparation of the input lies in the csv file which basically acts as a database, or model matrix, for the characters.
Each rows represent one character and each column represent one trait. The values of the trait can only be Yes/No. For traits that only have two possibilites (e.g wearing a mustache or not), only one column should be used as the truth table of positive and negative traits are complementary. For traits that have multiple possibilities n (e.g hair colour), n columns were used, and here we assume that we can not combine two traits into one for simplicity (Lets's say it's cheating to ask two questions linked into one!)

After feeding in the database/model matrix, this script will choose one of the traits that splits the set closest to half.
If the input is invalid, it will prompt for the same question.
If the input is Not sure, it will delete the trait from the set and ask another question
If the input is Yes/No, it will filter the character list accordingly, delete the trait from the set, and ask another question.
If fortunately the information is accurate and enough to pinpoint only 1 possibility, it will end with the guess.
In the unfortunate case that traits were exhausted before singling out the result, a list of possible outcome would be printed.

Apart from being an easy solution to a very niche game, it actually could be applied into any datasets that classify input into defined categories (e.g taxonomic assignment),
by choosing most efficient classifiers, the assignment of category could be much more efficient (like a sorting hat!)

#### Files:
project.py: The main script that does all things
GuessWho.csv: The 'database' in csv format, where each row denote one entry (characteristic and name of one person), and each column lists one characteristic.
test_project.py: test script for each function inside project.py
requirements.txt: list of pip installed prerequisites

#### Usage:
Main script:
'''
python project.py GuessWho.csv
'''

Test script:
'''
pytest test_project.py
'''
