# src/main.py

def greet(name):
    """
    Greets the user by name.

    Args:
        name (str): The name of the user.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
