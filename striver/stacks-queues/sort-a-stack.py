def sortedInsert(stack, el):
    if not stack or stack[-1] < el:
        stack.append(el)
        return
    temp = stack.pop()
    sortedInsert(stack, el)
    stack.append(temp)

def sortStack(stack):
    if stack:
        # Remove the top item
        temp = stack.pop()

        # Sort the remaining elements in stack
        sortStack(stack)

        # Insert the top item back to sorted stack
        sortedInsert(stack, temp)
        
