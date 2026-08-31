class MinStack:

    def __init__(self):
        self.min_num_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        
        if len(self.min_num_stack) == 0:
            self.min_num_stack.append(val)
        else:
            self.min_num_stack.append(min(self.min_num_stack[-1],val))


    def pop(self) -> None:
        self.min_stack.pop()
        self.min_num_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.min_num_stack[-1]
