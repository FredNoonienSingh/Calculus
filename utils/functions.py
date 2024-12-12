
import math 
from IPython.display import display, Math


class Function():
    """ 
        Class representing a function
    """
    def __init__(self, terms:list) -> None:
        self.terms = terms
    
    def display_latex(self) -> str:
        s = " "
        function_string = s.join(self.terms)
        display(Math(f"f(x)={function_string}"))