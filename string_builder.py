class StringBuilder:

    def __init__(self, start_string:str = "") -> None:
        """
        Initialize a new StringBuilder
        
        Sets to empty string is so value is set.
        """
        self.active_string:list[str] = list(start_string)
        self.index = 0

    def append(self, value:str) -> None:
        """Adds value to the end of the string"""

        self.active_string.extend(list(value))

    def insert(self, value:str, index:int) -> None:
        """Inserts value at a index"""
        self.active_string = (self.active_string[:index] 
                              + list(value) + self.active_string[index:])

    def delete(self, start_index:int, end_index:int) -> str:
        """Deletes part of the string at a given start index to end index
        
        Returns the removed string
        """
        return_list = (self.active_string[start_index:end_index])

        self.active_string = (self.active_string[:start_index] 
                                + self.active_string[end_index:])
        
        return "".join(return_list)

    def replace(self, start_index:int, end_index:int, replacement:str) -> None:
        """Replace part of the string at a given start index to end index"""
        self.active_string = (self.active_string[:start_index] + list(replacement)
                                + self.active_string[end_index:]) 

    # Dunder Methods
    def __iter__(self):
        return iter(self.active_string)
    
    def __next__(self):
        if self.index >= len(self.active_string):
            self.index = 0
            raise StopIteration
        current_element = self.active_string[self.index]
        self.index += 1
        return current_element

    def __contains__(self, value:str) -> bool:
        return value in self.active_string
    
    def __getitem__(self, index:str) -> str:
        return self.active_string[index]

    def __len__(self) -> int:
        return len(self.active_string)

    def __str__(self) -> str:
        return "".join(self.active_string)
    
    def __repr__(self) -> str:
        return "".join(self.active_string)