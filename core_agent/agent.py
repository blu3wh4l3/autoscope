class Agent:
    def __init__(self,llm,router):
        self.llm = llm
        self.router = router
        
    def actionPlan(self, goal):
        # if "nmap" in goal.lower():
        #     print("[+] Running Nmap scan on the target....")
        #     command = "nmap -sV 192.168.206.129"

        # elif "whoami" in goal.lower():
        #     print("[+] Running whoami command on the target....")
        #     command = "whoami"
        if "subdomain" in goal.lower():
            action = "run_subfinder"
            targetDomain  = input("Enter the target domain: ")
            args = {"domain": self.targetDomain}
        else:
            print("[!] Invalid task: {goal}")
        output, error = self.commandExecutor.run(command)
        return output