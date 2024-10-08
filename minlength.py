def minimum_length(s: str) -> int:
    stack = []
    
    for char in s:
        stack.append(char)
        # Check if the last two characters form "AB" or "CD"
        if len(stack) >= 2:
            if (stack[-2] == 'A' and stack[-1] == 'B') or (stack[-2] == 'C' and stack[-1] == 'D'):
                print(stack)
                stack.pop()  # Remove the last character
                stack.pop()  # Remove the second last character
                print(stack)
    #return len(stack)


# Example usage
print(minimum_length("ABFCACDB"))  # Output: 2
print(minimum_length("ACBBD"))     # Output: 5

