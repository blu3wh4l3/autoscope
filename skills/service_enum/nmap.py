from rich.console import Console
from pathlib import Path

console = Console()
def run(ip,executor):
    project_dir = Path(__file__).resolve().parents[2]
    output_dir = project_dir / 'outputs' / ip / 'raw' / 'ports_services.txt'
    output_dir.parent.mkdir(exist_ok=True, parents=True)
    command = f"nmap -sV -sC {ip}"
    output = executor.run(command)
    with open(output_dir, "w",encoding="utf-8") as f:
        f.write(output)
    return output