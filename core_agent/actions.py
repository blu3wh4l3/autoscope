from skills.subdomain_enum import subfinder
from skills.service_enum import nmap
from core_agent.normalizers.subfinder import normalize_subfinder_output

ACTIONS = {
    "run_subfinder" : {
        "label": "Subdomain enumeration",
        "allowed_targets" : ["domain", "ip"],
        "action": subfinder.run,
        "normalizer": normalize_subfinder_output


    },
    "run_nmap":{
        "label": "Nmap scan",
        "allowed_targets" : ["domain", "ip"],
        "action": nmap.run,
    }
}