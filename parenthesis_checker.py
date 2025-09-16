def is_balanced(expression):
    stack = []

    for char in expression:
        if char == '(':
            stack.append('(')
        elif char == '[':
            stack.append('[')
        elif char == '{':
            stack.append('{')

        # Handle closing parentheses
        elif char == ')':
            if not stack:
                return False  # No matching opening
            top = stack.pop()
            if top != '(':
                return False  # Mismatched pair

        elif char == ']':
            if not stack:
                return False
            top = stack.pop()
            if top != '[':
                return False

        elif char == '}':
            if not stack:
                return False
            top = stack.pop()
            if top != '{':
                return False

    # After the loop, if the stack is empty, all brackets matched
    if not stack:
        return True
    else:
        return False

# -------- Test Cases --------
if __name__ == "__main__":
    test_cases = [
        "(a + b) * c",             # Balanced
        "{[()()]}",                # Balanced
        "((())",                   # Not balanced
        "{[()]}",                  # Balanced
        "{[(])}",                  # Not balanced
        "(()[]{}())",              # Balanced
        "[(])",                    # Not balanced
    ]

    for expr in test_cases:
        result = is_balanced(expr)
        print(f"{expr} -> {'Balanced' if result else 'Not Balanced'}")
        print("Hello")
