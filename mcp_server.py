from mcp.server.fastmcp import FastMCP
import math


mcp = FastMCP("Programming Tutor")


@mcp.tool()
def check_palindrome(text: str) -> str:
    """
    Check whether a word, phrase, or sentence is a palindrome.
    Ignores spaces, punctuation, and capitalization.
    """
    cleaned = "".join(
        character.lower()
        for character in text
        if character.isalnum()
    )

    if not cleaned:
        return "Error: please provide some text."

    if cleaned == cleaned[::-1]:
        return (
            f"'{text}' is a palindrome.\n"
            f"Normalized text: '{cleaned}'"
        )

    return (
        f"'{text}' is not a palindrome.\n"
        f"Normalized text: '{cleaned}'"
    )


@mcp.tool()
def check_armstrong(number: int) -> str:
    """Check whether a number is an Armstrong number."""
    if number < 0:
        return f"{number} is not an Armstrong number."

    digits = str(number)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    calculation = " + ".join(f"{digit}^{power}" for digit in digits)

    if total == number:
        return (
            f"{number} is an Armstrong number.\n"
            f"Calculation: {calculation} = {total}"
        )

    return (
        f"{number} is not an Armstrong number.\n"
        f"Calculation: {calculation} = {total}"
    )


@mcp.tool()
def fibonacci(n: int) -> str:
    """
    Return the nth Fibonacci number using zero-based indexing.
    Sequence: 0, 1, 1, 2, 3, 5, 8...
    """
    if n < 0:
        return "Error: n must be greater than or equal to 0."

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b

    return f"Fibonacci({n}) = {a}"


@mcp.tool()
def check_prime(number: int) -> str:
    """Check whether a number is prime."""
    if number < 2:
        return f"{number} is not a prime number."

    for divisor in range(2, math.isqrt(number) + 1):
        if number % divisor == 0:
            return (
                f"{number} is not a prime number.\n"
                f"Reason: it is divisible by {divisor}."
            )

    return f"{number} is a prime number."


@mcp.tool()
def factorial(number: int) -> str:
    """Calculate the factorial of a non-negative integer."""
    if number < 0:
        return "Error: factorial is not defined for negative numbers."

    return f"{number}! = {math.factorial(number)}"


@mcp.tool()
def reverse_string(text: str) -> str:
    """Reverse the supplied text."""
    if not text:
        return "Error: please provide some text."

    return f"Original: '{text}'\nReversed: '{text[::-1]}'"


@mcp.tool()
def check_even_odd(number: int) -> str:
    """Check whether a number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even."
    return f"{number} is odd."


@mcp.tool()
def sum_of_digits(number: int) -> str:
    """Calculate the sum of all digits in a number."""
    digits = str(abs(number))
    total = sum(int(digit) for digit in digits)
    return f"Sum of digits of {number} = {total}"


@mcp.tool()
def gcd(a: int, b: int) -> str:
    """Calculate the greatest common divisor of two integers."""
    return f"GCD of {a} and {b} = {math.gcd(a, b)}"


@mcp.tool()
def lcm(a: int, b: int) -> str:
    """Calculate the least common multiple of two integers."""
    if a == 0 or b == 0:
        return f"LCM of {a} and {b} = 0"

    result = abs(a * b) // math.gcd(a, b)
    return f"LCM of {a} and {b} = {result}"


@mcp.tool()
def check_leap_year(year: int) -> str:
    """Check whether a year is a leap year."""
    if year % 400 == 0:
        return f"{year} is a leap year."
    if year % 100 == 0:
        return f"{year} is not a leap year."
    if year % 4 == 0:
        return f"{year} is a leap year."
    return f"{year} is not a leap year."


@mcp.tool()
def count_vowels(text: str) -> str:
    """Count the vowels in a string."""
    vowels = "aeiou"
    count = sum(1 for character in text.lower() if character in vowels)
    return f"'{text}' contains {count} vowel(s)."


@mcp.tool()
def check_anagram(first: str, second: str) -> str:
    """
    Check whether two words or phrases are anagrams.
    Ignores spaces, punctuation, and capitalization.
    """
    first_cleaned = "".join(
        character.lower() for character in first if character.isalnum()
    )
    second_cleaned = "".join(
        character.lower() for character in second if character.isalnum()
    )

    if not first_cleaned or not second_cleaned:
        return "Error: both inputs must contain text."

    if sorted(first_cleaned) == sorted(second_cleaned):
        return f"'{first}' and '{second}' are anagrams."

    return f"'{first}' and '{second}' are not anagrams."


if __name__ == "__main__":
    mcp.run()
