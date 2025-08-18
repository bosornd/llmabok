from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """
    Add two numbers.
    """

    return a + b

print(type(add))
print(add.name)
print(add.description)
print(add.args)

@tool(parse_docstring=True)
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers.

    Args:
        a: the left operand.
        b: the right operand.

    Returns:
        The multiplication of the two operands.
    """
    return a * b

print(multiply.name)
print(multiply.description)
print(multiply.args)

print(add.invoke({"a": 2, "b": 3}))         # 5
print(multiply.invoke({"a": 2, "b": 3}))    # 6