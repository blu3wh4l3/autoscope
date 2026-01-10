from rich.console import Console
import os
from pathlib import Path

console = Console()
def run(domain,executor):
    project_dir = Path(__file__).resolve().parents[2]
    domains_output = project_dir / 'outputs' / domain / 'subdomains.txt'
    domains_output.parent.mkdir(exist_ok=True, parents=True)
    command = f"subfinder -d {domain}"
    with console.status("[bold green] Running subfinder..."):
        output = executor.run(command)
    with open(domains_output, "w",encoding="utf-8") as f:
        f.write(output)
    for line in output.splitlines():
        print(line)
