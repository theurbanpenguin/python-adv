import pandas as pd

# Specify the path to the /etc/passwd file
passwd_file_path = '/etc/passwd'

# Use Pandas to read the file. Specify the correct delimiter and column names
df = pd.read_csv(passwd_file_path,
                 sep=':', header=None,
                 names=['username', 'password', 'UID', 'GID',
                        'user_info', 'home_directory', 'shell'])

# print(df)
grouped_by_shell = df.groupby('shell')
# Count the number of users per shell
users_per_shell = grouped_by_shell.size()

# Alternatively, if you're interested in more detailed aggregations,
# like the minimum UID for each shell:
min_uid_per_shell = grouped_by_shell['UID'].min()

# print(users_per_shell)
# print(min_uid_per_shell)
for shell, group in grouped_by_shell:
    print(f"Shell: {shell}")
    print("Users:")
    for username in group['username']:
        print(f'  {username}')
    print("\n")  # Adds a newline for better readability between groups
