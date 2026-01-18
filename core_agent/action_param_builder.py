from core_agent.actions import ACTIONS
def build_action_params(action, target):
    if target["target_type"] in ACTIONS.get(action["action"]).get("allowed_targets"):
        return {
                "action": action["action"],
                "target": {
                    "type": target["target_type"],
                    "value": target["value"]
                },
                "params": {}
        }
    else:
        raise ValueError("Invalid target type and action")