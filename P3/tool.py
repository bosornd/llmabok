from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

print(add.name)         # add
print(add.description)  # Add two numbers.
print(add.args)         # {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}

@tool(parse_docstring=True)
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.

    Args:
        a: the left operand.
        b: the right operand.
    """
    return a * b

print(multiply.name)         # multiply
print(multiply.description)  # Multiply two numbers.
print(multiply.args)         # {'a': {'description': 'the left operand.', 'title': 'A', 'type': 'integer'}, 'b': {'description': 'the right operand.', 'title': 'B', 'type': 'integer'}}

print(add.invoke({"a": 2, "b": 3}))         # 5
print(multiply.invoke({"a": 2, "b": 3}))    # 6
