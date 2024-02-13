from my_states import StateSearch, CapitalSearch

# Create an instance of StateSearch or CapitalSearch based on user input
if __name__ == "__main__":
    json_file = "states_data.json"
    while True:
        user_input = input("Enter a search term (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            break
        search_type = input("Enter the type of search (state/capital): ").strip()
        if search_type.lower() not in ['state', 'capital']:
            print("Invalid search type. Please choose 'state' or 'capital'.")
            continue
        if search_type.lower() == 'state':
            search = StateSearch(json_file)
        else:
            search = CapitalSearch(json_file)
        search.search(user_input)
