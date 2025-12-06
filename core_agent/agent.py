class Agent:
    def __init__(self,commandExecutor):
        self.commandExecutor = commandExecutor
        
    def runTask(self, goal):
        if "nmap" in goal.lower():
            print("[+] Running Nmap scan on the target....")
            command = "nmap -sV 192.168.206.129"

        elif "whoami" in goal.lower():
            print("[+] Running whoami command on the target....")
            command = "whoami"
        elif "subdomain" in goal.lower():
            action = "run_subfinder"
            aegs
            #Call subdomain skill and ask for the domain from the user.
        else:
            print("[!] Invalid task: {goal}")
        output, error = self.commandExecutor.run(command)
        return output