def string_operations():
    # 1. Creating strings
    str1 = "Hello, "
    str2 = "World!"

    # 2. Concatenation
    concatenated = str1 + str2
    print("Concatenated String:", concatenated)

    # 3. Repetition
    repeated = str1 * 3
    print("Repeated String:", repeated)

    # 4. String length
    length = len(concatenated)
    print("Length of Concatenated String:", length)

    # 5. Accessing characters
    first_char = concatenated[0]
    last_char = concatenated[-1]
    print("First Character:", first_char)
    print("Last Character:", last_char)

    # 6. Slicing
    substring = concatenated[7:12]
    print("Substring (7 to 12):", substring)

    # 7. Finding substrings
    index = concatenated.find("World")
    print("Index of 'World':", index)

    # 8. Replacing substrings
    replaced = concatenated.replace("World", "Python")
    print("Replaced String:", replaced)

    # 9. Converting to uppercase
    uppercase = concatenated.upper()
    print("Uppercase String:", uppercase)

    # 10. Converting to lowercase
    lowercase = concatenated.lower()
    print("Lowercase String:", lowercase)

    # 11. Splitting strings
    split_str = concatenated.split(", ")
    print("Split String:", split_str)

    # 12. Joining strings
    joined_str = " and ".join(split_str)
    print("Joined String:", joined_str)

    # 13. Stripping whitespace
    str_with_whitespace = "   Hello, World!   "
    stripped_str = str_with_whitespace.strip()
    print("Stripped String:", stripped_str)

    # 14. Checking if string starts or ends with a substring
    starts_with_hello = concatenated.startswith("Hello")
    ends_with_exclamation = concatenated.endswith("!")
    print("Starts with 'Hello':", starts_with_hello)
    print("Ends with '!':", ends_with_exclamation)

# Call the function to see the output
string_operations()
