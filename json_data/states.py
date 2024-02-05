import json

# Define the State class to represent state information
class State:
    def __init__(self, state, capital, population):
        self.state = state
        self.capital = capital
        self.population = population


    def __str__(self):
        formatted_population = "{:,}".format(self.population)  # Format population with commas
        return f"State: {self.state}, Capital: {self.capital}, Population: {formatted_population}"

# Function to load JSON data and create State objects
def load_states_from_json(json_file):
    states = []
    with open(json_file, 'r') as file:
        data = json.load(file)
        for item in data:
            state = State(item["State"], item["Capital"], item["Population"])
            states.append(state)
    return states

# Function to sort states by state name
def sort_states_by_state_name(states):
    return sorted(states, key=lambda x: x.state)

# Function to sort states by capital name
def sort_states_by_capital_name(states):
    return sorted(states, key=lambda x: x.capital)

# Function to sort states by population
def sort_states_by_population(states):
    return sorted(states, key=lambda x: x.population, reverse=True)

# Example usage
if __name__ == "__main__":
    json_file = "states_data.json"  # Replace with your JSON file path
    states = load_states_from_json(json_file)

    # print("States sorted by state name:")
    # for state in sort_states_by_state_name(states):
    #     print(state)

    # print("\nStates sorted by capital name:")
    # for state in sort_states_by_capital_name(states):
    #     print(state)

    print("\nStates sorted by population:")
    for state in sort_states_by_population(states):
        print(state)

