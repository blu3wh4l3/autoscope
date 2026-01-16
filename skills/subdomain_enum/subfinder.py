from rich.console import Console
from pathlib import Path
from core_agent.normalizers.subfinder import normalize_subfinder_output

console = Console()
def run(domain,executor):
    project_dir = Path(__file__).resolve().parents[2]
    domains_output = project_dir / 'outputs' / domain / 'raw' / 'subdomains.txt'
    domains_output.parent.mkdir(exist_ok=True, parents=True)
    command = f"subfinder -d {domain}"
    output = executor.run(command)
    with open(domains_output, "w",encoding="utf-8") as f:
        f.write(output)
    normalize_subfinder_output(domain, output)