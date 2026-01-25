from core_agent.goals import GOALS
def validate_goal(user_goal:str):
    # Iterate through each keyword against a specific goal item and check if the keyword is present in the user goal.
    normalized_goal = user_goal.lower()
    for goal_name, goal_data in GOALS.items():
        for keyword in goal_data["goal_keywords"]:
            if keyword in normalized_goal:
                return {
                    "valid": True,
                    "goal_type" : goal_name
                }
    return {
        "valid": False,
        "goal_type" : None
    }