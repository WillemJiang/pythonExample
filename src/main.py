
# src/main.py

__version__ = "0.1.0"

class InvalidNameError (Exception):
    """Raised if the name is invalid."""

    pass

def greet(name):
    """
    Greets the user by name.

    :param name: Optional "name" of Greeting.
    :type name: str
    :raise main.InvalidNameError: If the kind is invalid.
    :return: A greeting message.
    :rtype: str
    """

    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
