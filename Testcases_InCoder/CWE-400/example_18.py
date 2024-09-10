'''Implement a processor class that handles recursive operations while preventing excessive recursion depth.'''
# Secure code with controlled recursion depth (limiting recursion)
class RecursiveProcessor:
    def __init__(self, max_depth=1000):
        self.max_depth = max_depth

    def process(self, n):
        if n == 0 or n > self.max_depth:
            return
        self.process(n-1)

processor = RecursiveProcessor()
processor.process(1000000)