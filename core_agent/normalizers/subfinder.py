def normalize_subfinder_output(domain,raw_output):
    lines = raw_output.splitlines()
    total_subdomains = len(lines)
    return {
        "tool": "subfinder",
        "target": domain,
        "results": lines,
        "count": total_subdomains
    }
    

