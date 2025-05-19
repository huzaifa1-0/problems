users = [
    {'name': 'Huzaifa', 'email': 'huzaifaras10@gmail.com','age': 21},
    {'name': 'sikandar', 'email': 'sikandar10@gmail.com','age': 21},
    {'name': 'rana khurram', 'email': 'rana10@gmailcom','age': 21},
    {'name': 'abdullah', 'email': 'huzaifa10gmail.com','age': 11},
    {'name': 'fawad', 'email': 'huzaifaras10gmail.com','age': 31},
    {'name': 'afraz', 'email': 'huzaifaras10gmail.com','age': 19},
    {'name': 'ahad', 'email': 'huzaifaras10gmail.com','age': 20}
]


def filter_user(users):
    return [
        user for user in users
        if '@' in user['email'] and '.' in user['email'] and user['age'] >= 18
    ]

filered_users = filter_user(users)
print(filered_users)