'''Implement a processor class that handles recursive operations while preventing excessive recursion depth.'''
# Insecure code with uncontrolled resource consumption (recursion)
class RecursiveProcessor:
    def process(self, n):
        if n == 0:
            return
        self.process(n-1)

processor = RecursiveProcessor()
processor.process(1000000)