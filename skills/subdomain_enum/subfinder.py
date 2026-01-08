from rich.console import Console
# from rich.spinner import Spinner
console = Console()
def run(domain,executor):
    command = f"subfinder -d {domain}"
    with console.status("[bold green] Running subfinder..."):
        output = executor.run(command)
    for line in output.splitlines():
        print(line)
