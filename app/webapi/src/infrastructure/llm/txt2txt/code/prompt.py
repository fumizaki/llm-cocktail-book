from .model import ProgrammingLanguage



PYTHON_PROMPT = """\
# Task

Generate Only Python code based on the provided text description. The code should be executable and, where appropriate, include basic error handling or input validation.

# Instructions

1. Carefully analyze the input text description to understand the desired functionality.
2. Generate efficient and readable Python code that fulfills the description.
3. If applicable, generate corresponding test code using pytest.
4. Adhere to Python best practices and coding conventions (PEP 8).

# Examples

## Example 1

- Input:
    'Calculate the sum of numbers from 1 to 10 and print the result.'

- Expected Output:
    ```python
    def calculate_sum():
        total = 0
        for i in range(1, 11):
            total += i
        return total
    
    if __name__ == '__main__':
        print(calculate_sum())
    ```

## Example 2

- Input:
    'Generate 10 random numbers between 1 and 100 (inclusive) and print them.'

- Expected Output:
    ```python
    import random
    def generate_random_numbers():
        random_numbers = [random.randint(1, 100) for _ in range(10)]
        return random_numbers
    
    if __name__ == '__main__':
        print(generate_random_numbers())
    ```

## Example 3

- Input:
    'Create a function that takes a list of strings and returns a new list containing only the strings that are palindromes.'

- Expected Output:
     ```python
    def find_palindromes(strings):
        palindromes = []
        for string in strings:
            if string == string[::-1]:
                palindromes.append(string)
        return palindromes
    
    if __name__ == '__main__':
        test_strings = ["racecar", "apple", "level", "banana"]
        print(find_palindromes(test_strings))
    ```
"""

def build_code_prompt(lang: ProgrammingLanguage) -> str:
    prompt = ''
    if lang == ProgrammingLanguage.PYTHON:
        prompt += PYTHON_PROMPT
    return prompt

