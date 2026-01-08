def build_arguments(action, target):
    if target["target_type"] == 'domain':
        return {
            "action": action["action"],
            "args": {
                "domain": target["value"]
            }
        }
    else:
        print("INVALID ARGUMENT")