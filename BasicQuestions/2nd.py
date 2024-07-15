# Sample collection
users = {'kundan': 'active', 'Trilok': 'inactive', 'kuldeep': 'active'}

# Create an empty dictionary to store active users
active_users = {}

# Iterate over a copy of users
for user, status in users.copy().items():
    if status == 'inactive':
        # Remove inactive users from the original dictionary
        del users[user]

# Iterate over the modified users dictionary
for user, status in users.items():
    if status == 'active':
        # Add active users to the active_users dictionary
        active_users[user] = status

# Print the original and active users
print("Original users:", users)
print("Active users:", active_users)
