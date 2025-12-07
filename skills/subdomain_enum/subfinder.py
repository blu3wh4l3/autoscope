def run(executor,domain):
    command = f"subfinder -d {args.domain}"
    output = executor.exec(command)
    print(output)
