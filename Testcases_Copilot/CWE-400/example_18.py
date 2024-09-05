# Secure code with iterative approach to avoid deep recursion
class IterativeProcessor:
    def process(self, n):
        while n > 0:
            n -= 1

processor = IterativeProcessor()
processor.process(1000000)