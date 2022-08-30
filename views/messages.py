from rich.console import Console

console = Console(width=75)


class Error:
    def __init__(self, message):
        self.message = message
        console.print(message, style="bold red")


class Information:
    def __init__(self, message):
        self.message = message
        console.print(message, style="bold blue")
