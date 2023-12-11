users = [
    (1, 'Rharamys', 'rharamys@email.com', True),
    (2, 'user2', 'user2@email.com', True),
    (3, 'Inactive', 'inactive@email.com', False),
]

formatted_users = {user[1]: user[2] for user in users if user[3]}

print(formatted_users)