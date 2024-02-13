import pandas as pd
from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self, json_file: str):
        self.df = pd.read_json(json_file)

    @abstractmethod
    def search(self, search_term: str) -> None:
        pass

class StateSearch(State):
    def search(self, search_term: str) -> None:
        result = self.df[self.df['State'].str.lower() == search_term.lower()]
        if not result.empty:
            print(result)
        else:
            print("No matching state found for", search_term)

class CapitalSearch(State):
    def search(self, search_term: str) -> None:
        result = self.df[self.df['Capital'].str.lower() == search_term.lower()]
        if not result.empty:
            print(result)
        else:
            print("No matching capital found for", search_term)
