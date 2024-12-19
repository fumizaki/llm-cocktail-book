PYTHON_PROMPT = """\
# Steps

1. Carefully analyze the text.
2. Proceed to generate the text into Python.

# Examples

- Example Input:
    '1から10までの数を足し算し、結果を出力する'

- Example Output:
    ```python
    sum = 0
    for i in range(1, 11):
        sum += i
    print(sum)
    ```
"""