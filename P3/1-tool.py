from langchain_core.tools import tool

@tool
def add(a: int, b: int) -> int:
    """
    Add two numbers.

    Args:
        a (int): the left operand.
        b (int): the right operand.

    Returns:
        The sum of the two operands.
    """

    return a + b

print(type(add))
print(add.name)
print(add.description)
print(add.args)

response = add.invoke({"a": 2, "b": 3})
print(response)
