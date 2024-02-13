import pandas as pd

class StateSearch:
    def __init__(self, json_file: str, state_name: str):
        self.df = pd.read_json(json_file)
        self.state_name = state_name

    def search_state(self) -> None:
        state_info = self.df[self.df['State'].str.lower() == self.state_name.lower()]
        if not state_info.empty:
            print(state_info)
        else:
            print("State not found.")

# Create an instance of StateSearch with the state name to search for
if __name__ == "__main__":
    json_file: str = "states_data.json"
    while True:
        user_input: str = input("Enter a state name (or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            break
        else:
            state_search = StateSearch(json_file, user_input)
            state_search.search_state()
