from PyInquirer import prompt
import csv

all_users = []

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        'choices' : all_users
    },

]



def new_expense(*args):
    # Init User list 
    all_users = []

    # Get all users from csv
    with open('users.csv', newline='') as csvfile:
        fcc_data = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for user in fcc_data:
            all_users.append(''.join(user))
        csvfile.close()
    infos = prompt(expense_questions)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    # True, so did it here:
    with open('expense_report.csv', 'a', newline='') as csvfile:
        fieldnames = ['amount', 'label', 'spender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writerow({'amount': infos['amount'], 'label':infos['label'], 'spender':infos['spender']})
        csvfile.close()
        
    return True


