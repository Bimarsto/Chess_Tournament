from rich.console import Console

console = Console(width=75)


class Error:
    def __init__(self, message):
        self.message = message

    def __call__(self):
        console.print(self.message, style="bold red")