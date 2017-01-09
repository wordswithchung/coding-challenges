def is_balanced_brackets(str):

    closers_and_openers = {'}': '{', ']': '[', ')': '('}
    openers = closers_and_openers.values()
    opener_stack = []

    for char in str:
        if char in openers:
            opener_stack.append(char)
        elif char in closers_and_openers:
            if closers_and_openers[char] != opener_stack[-1]:
            	return False
            else:
                opener_stack.pop()

    return opener_stack == []
