def build_arguments(action, target):
    if target["target_type"] == 'domain':
        return {
            "action": action["action"],
            "target_type": target["target_type"],
            "args": {
                "domain": target["value"]
            }
        }
    elif target["target_type"] == 'ip':
        return {
            "action": action["action"],
            "target_type": target["target_type"],
            "args": {
                "ip": target["value"]
            }
        }
    else:
        raise ValueError("Invalid target type and action")