from PyInquirer import prompt
import csv

# Questions to be asked when user selects "New User"
user_questions = [
{
    'type': 'input',
    'name': 'name',
    'message': '👋🏻 Welcome new user, \n What is your name ?'
}
]

# Function that makes sure that name isn't already taken in db
def is_user_new(name):
    # Import csv that holds all the information on users 
    with open('users.csv', newline='') as csvfile:
        fcc_data = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for user in fcc_data:
            user_name = ''.join(user)
            if user_name == name['name']:
                return False
        csvfile.close()
    return True

def add_user():
    # This function should create a new user, asking for its name
    name = prompt(user_questions)

    # Continues to ask for user's name whilst it's already taken
    while not is_user_new(name):
        print("🚨ERROR🚨: This name is already taken sorry darling, chose another one")
        name = prompt(user_questions)

    # Add to csv
    with open('users.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        print('Name is: ', name['name'])
        writer.writerow([name['name']])
        csvfile.close()
   
    return True