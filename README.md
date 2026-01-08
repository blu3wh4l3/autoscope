## Install Paramiko
sudo apt install python3-paramiko
## SSH Key Generation
ssh-keygen -t ed25519    # accept defaults
ssh-copy-id username@192.168.1.42   # if ssh-copy-id available
# or manually copy ~/.ssh/id_ed25519.pub into Kali's ~/.ssh/authorized_keys

# PROJECT STRUCTURE

autoscope/
│
├── core/
│   ├── agent.py              # The main agent loop
│   ├── state.py              # Recon session state
│   ├── llm.py                # Ollama/OpenAI wrapper
│   ├── router.py             # Action → correct skill mapping
│   ├── prompts.py            # Action planner, reasoning prompts
│   ├── summarizer.py         # Summaries from raw output
│   └── executor.py           # <-- NEW: abstract executor interface
│
├── executors/
│   ├── ssh_executor.py       # <-- NEW: runs commands on Kali VM via SSH
│   └── local_executor.py     # optional: run tools locally on WSL later
│
├── skills/
│   ├── subdomains/
│   │     ├── subfinder.py
│   │     ├── amass.py
│   │     ├── crtsh.py
│   │     ├── merger.py
│   │     └── google_dorker.py
│   ├── ports/
│   │     └── nmap.py
│   ├── webdirs/
│   │     └── feroxbuster.py
│   └── screenshots/
│         └── gowitness.py
│
├── memory/
│   ├── chroma_store.py
│   ├── raw_store.py
│   └── schemas.py
│
├── data/
│   └── example.com/
│         ├── subfinder_raw.txt
│         ├── amass_raw.txt
│         ├── merged.json
│         └── summary.json
│
├── utils/
│   ├── logger.py
│   ├── config.py            # SSH credentials, paths, etc.
│   └── helpers.py
│
├── tests/
│
└── main.py


# Phase 1 — Rule-Based Routing

Your router maps actions manually:

"run_subfinder" -> subfinder.run
"run_amass"     -> amass.run
"run_merge"     -> merger.merge


And the Agent uses simple logic like:

if “subdomain” in user_input:
    action = "run_subfinder"



# Action Planner
Action planner - Future scope after setting up rule based routing to tools for performing actions based on user goal.
1. What is the Action Planner Prompt?

It's a prompt given to the LLM that tells it:
What tasks exist (your available skills)
What state the recon is currently in
What the user’s goal is
What actions it can choose from
How to return the decision in JSON


# SYSTEM PROMPT
You are AutoScope, an autonomous cybersecurity reconnaissance agent.

Your responsibilities:
- Plan the next best reconnaissance step.
- Use ONLY the allowed actions listed below.
- Follow the recon workflow rules strictly.
- Produce valid JSON output that the router can understand.

# Available Actions:

1. run_subfinder(domain)
   - Perform passive subdomain enumeration.

2. run_amass_passive(domain)
   - Perform deeper passive enumeration.

3. run_merge()
   - Merge all collected subdomains.

4. run_httpx(subdomains)
   - Probe subdomains to find live hosts.

5. run_nmap(target)
   - Run port scan on a live host.

6. summarize_subdomains()
   - Summarize the subdomain findings.

7. finish()
   - Use when recon is complete or no valid action remains.

Recon Workflow Rules:
- Start with passive enumeration (subfinder → amass).
- Merge before probing.
- Probe live hosts before scanning ports.
- Do not repeat completed steps (based on state).
- Never guess values or fabricate output.

Output Rules:
- Always return valid JSON with keys: "action" and "args".
- Never include explanations or text outside the JSON.
- Example:

{
  "action": "run_subfinder",
  "args": { "domain": "example.com" }
}

Behavior Constraints:
- Use only facts provided via state, memory, or user.
- No hallucinations.
- No assumptions.
- No commentary.

# ROUTER DEFINITION
class Router:
    - stores tool mapping internally
    - stores executor instance
    - has an execute(action, args) method
    - validates action exists
    - calls the correct skill
    - handles exceptions
    - logs what was run


self.tools = {
    "run_subfinder": subfinder.run,
    "run_amass_passive": amass.run_passive,
    "merge_subdomains": merger.merge,
    "probe_live_hosts": httpx.run,
    "scan_ports": nmap.run,
    "summarize_subdomains": summarizer.summarize,
    "finish": lambda: None
}


# main()
def main():

    # 1. Choose execution environment
    if user chooses local:
        executor = LocalExecutor()
    else:
        executor = SSHExecutor(host, user, password)

    # 2. Initialize LLM
    llm = LLM(provider="ollama", model="llama3.1:8b")

    # 3. Initialize Router with executor
    router = Router(executor)

    # 4. Initialize State Manager
    state = ReconState()

    # 5. Initialize Agent with llm, router, and state
    agent = Agent(llm, router, state)

    # 6. Start interactive loop
    while True:
        goal = input("Enter goal: ")
        result = agent.handle(goal)
        print(result)

# ORGANIZING PROMPTS
prompts/
   system/
      agent_system_prompt.txt
      action_planner_prompt.txt
      summarizer_prompt.txt
   user/
      goal_template.txt
   skills/
      subdomain_prompt.txt
      amass_prompt.txt

# PROMPT TEMPLATE SETUP


### System prompt
You are AUTO-SCOPE, an autonomous cybersecurity reconnaissance agent.

Your job is:
1. Understand the user's recon goal.
2. Decide the correct next action.
3. Output only in the required format.
4. Never hallucinate tools or steps.
5. If unsure, ask the user for clarification.

Available actions:
- run_subfinder
- run_amass_passive
- run_dns_bruteforce
- run_httpx
- summarize_results
- stop

Rules:
- You must ALWAYS output valid JSON.
- Never include explanations unless asked.
- Never invent subdomains or hostnames.
- Choose only one action at a time.

Your output format:
{
  "action": "<action_name>",
  "args": {
      ... arguments for that action ...
  }
}




### Action planner
prompts/system/action_planner_prompt.txt
You are the AutoScope Recon Planning Agent.

Your job is to decide the next best action.

User Goal:
{goal}

Current Recon State:
{state}

Previous Tool Output:
{last_output}

Available Actions:
{actions}

Output rules:
- Always respond in JSON.
- Use this exact structure:

{
  "action": "<action_name>",
  "args": {
      ... any required arguments ...
  }
}

Do not include explanations.
Do not include extra text.
Respond with ONLY JSON.

template = load_prompt("prompts/system/action_planner_prompt.txt")

prompt = template.format(
    goal=user_goal,
    state=current_state,
    last_output=previous_output,
    actions=json.dumps(available_actions)
)


# Improvements
1. If Kali VM is not running, handle the executor output splitlines method error.