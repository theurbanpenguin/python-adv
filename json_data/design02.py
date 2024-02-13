import pandas as pd

# Read the JSON file into a DataFrame
json_file = "states_data.json"
df = pd.read_json(json_file)

# Function to search for a state by its name
def search_state(state_name):
    state_info = df[df['State'].str.lower() == state_name.lower()]
    if not state_info.empty:
        print(state_info)
    else:
        print("State not found.")

# Main loop for user interaction
while True:
    user_input = input("Enter a state name (or 'exit' to quit): ").strip()
    if user_input.lower() == 'exit':
        break
    else:
        search_state(user_input)
