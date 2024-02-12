#!/usr/bin/python3
"""AirBnB clone - The console"""
import sys


class Console:
    """Command line interpreter for AirBnB clone"""

    def __init__(self):
        """Initialize the console"""
        self.prompt = "(hbnb) "

    def cmdloop(self):
        """Run the command loop"""
        while True:
            user_input = input(self.prompt)
            if user_input == "quit":
                break
            elif user_input == "help":
                print("Documented commands (type help <topic>):")
                print("========================================")
                print("EOF  help  quit")
            else:
                print("Invalid command. Type 'help' for assistance.")


def main():
    """Main entry point"""
    console = Console()
    console.cmdloop()


if __name__ == "__main__":
    main()
