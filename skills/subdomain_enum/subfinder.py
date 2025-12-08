def run(executor,domain):
    command = f"subfinder -d {domain}"
    output = executor.run(command)
    print(output)
