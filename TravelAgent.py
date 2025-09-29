from google.adk.agents import LlmAgent
from google.adk.tools import google_search

# API key from apistudio.google.com; GCP project spenzomatic (river-device-457314-r0)
# GOOGLE_API_KEY='AIzaSyBvHKFLwCwCQ5qQWRPZRh_1umh1Q4uz5Ew'


# API key from GCP playground project spenz-experimental
GOOGLE_API_KEY='AIzaSyDXdM7GN1nZSa6hmDzTIVYHqphGqWKB1fM'


MODEL='gemini-2.5-flash-001'
print(MODEL)


root_agent = LlmAgent(
   model=MODEL,
   name="IdeaAgent",
   description=f"""Brainstorms creative and exciting weekend travle ideas based on user
   preferences or requests.
   """,
   instruction=f"""You are a creative travel agent. Use the tool to
   brainstorm and respond to the user with 3 exciting weekend trip ideas
   based on the user's request.""",
   tools=[google_search],
   disallow_transfer_to_peers=True,
   api_key=GOOGLE_API_KEY,
)
