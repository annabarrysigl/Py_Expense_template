from PyInquirer import prompt
import csv

all_users = []
ppl_involved = []

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

added_questions = [
    {
        "type":"checkbox",
        "name":"involved",
        "message":"Thanks for your generosity, your friends 💖 you \n - Who was involved in the expense ? : ",
        'choices' : ppl_involved
    }
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
    
    infos = prompt(expense_questions)

    # While amount isn't numeric, ask for question again
    while not infos['amount'].isnumeric():
        print("🚨ERROR🚨: Sorry love the amount needs to be a number, try again ❤️‍🔥")
        infos = prompt(expense_questions)

    # Ask for People involved
    # Get all users but the spender from csv
    with open('users.csv', newline='') as csvfile:
        fcc_data = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for user in fcc_data:
            user_name = ''.join(user)
            if user_name != infos['spender']:
                ppl_involved.append(''.join(user))
        csvfile.close()
    ppl = prompt(added_questions)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    # True, so did it here:
    with open('expense_report.csv', 'a', newline='') as csvfile:
        fieldnames = ['amount', 'label', 'spender', 'involved']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writerow({'amount': infos['amount'], 'label':infos['label'], 'spender':infos['spender'], 'involved': ppl['involved']})
        csvfile.close()

    return True


