class IntegerArray:
    def __init__(self):
        # Initialize the array as an empty list
        self.array = []

    def add(self, value):
        # Add a value to the array
        self.array.insert(0, value)  # Adds at the beginning
        print(f"Added {value} to the array at the beginning.")

    def append(self, value):
        # Append a value to the array
        self.array.append(value)
        print(f"Appended {value} to the array.")

    def remove(self, value):
        # Remove a value from the array, if it exists
        if value in self.array:
            self.array.remove(value)
            print(f"Removed {value} from the array.")
        else:
            print(f"{value} not found in the array.")

    def display(self):
        # Display the current array
        print(f"Current array: {self.array}")


# Example usage:
if __name__ == "__main__":
    # Initialize the array
    arr = IntegerArray()

    # Adding values to the array
    arr.add(10)
    arr.append(20)
    arr.append(30)

    # Displaying the current array
    arr.display()

    # Removing a value from the array
    arr.remove(20)
    
    # Displaying the updated array
    arr.display()

    # Trying to remove a non-existing value
    arr.remove(40)
