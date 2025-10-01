from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.tools import agent_tool
import yaml

# since adk web is invoked from parent folder, need to specify travel_agent/
with open('travel_agent/instructions.yaml', 'r') as file:
    instructions = yaml.safe_load(file)

# Access the specific instructions for each agent
IDEA_AGENT_DESCRIPTION = instructions['idea_agent']['description']
IDEA_AGENT_INSTRUCTION = instructions['idea_agent']['instruction']
REFINER_AGENT_DESCRIPTION = instructions['refiner_agent']['description']
REFINER_AGENT_INSTRUCTION = instructions['refiner_agent']['instruction']
ROOT_AGENT_DESCRIPTION = instructions['root_agent']['description']
ROOT_AGENT_INSTRUCTION = instructions['refiner_agent']['instruction']

# Pick the LLM model to be used
MODEL="gemini-2.0-flash"

idea_agent = LlmAgent(
    model=MODEL,
    name='IdeaAgent',
    description=IDEA_AGENT_DESCRIPTION,
    instruction=IDEA_AGENT_INSTRUCTION,
    tools=[google_search],
    disallow_transfer_to_peers=True,
)

refiner_agent = LlmAgent(
# root_agent = LlmAgent(
    model=MODEL,
    name='RefinerAgent',
    description=REFINER_AGENT_DESCRIPTION,
    instruction=REFINER_AGENT_INSTRUCTION,
    tools=[google_search],
    disallow_transfer_to_peers=True,
)

root_agent = LlmAgent(
    model=MODEL,
    name='PlannerAgent',
    description=ROOT_AGENT_DESCRIPTION,
    instruction=ROOT_AGENT_INSTRUCTION,
    # See https://github.com/google/adk-python/issues/53#issuecomment-2798906767 for context
    tools=[agent_tool.AgentTool(agent=idea_agent), agent_tool.AgentTool(agent=refiner_agent)]
)