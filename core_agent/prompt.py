import os

def load_prompt(fileName: str):
    promptPath = os.path.join((os.path.dirname(os.path.dirname(__file__))),"core_agent","prompts",fileName)
    with open(promptPath, mode="r", encoding="utf-8") as promptFile:
        return promptFile.read()

def render_prompt(promptTemplate:str, **kwargs):
    return promptTemplate.format(**kwargs)