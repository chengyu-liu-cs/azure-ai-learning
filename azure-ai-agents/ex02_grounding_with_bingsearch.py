# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""

DESCRIPTION:
    This sample demonstrates how to use agent operations with the Grounding with Bing Search tool from
    the Azure Agents service using a synchronous client.

USAGE:
    python sample_agents_bing_grounding.py

    Before running the sample:

    pip install azure.ai.projects azure-identity

    Set these environment variables with your own values:
    AZURE_AI_FOUNDRY_PROJECT_ENDPOINT - the Azure AI Project endpoint, as found in your AI Studio Project.
    BING_CONNECTION_ID - the connection ID for the Bing Grounding tool.
    AZURE_AI_FOUNDRY_MODEL_DEPLOYMENT_NAME - the deployment name of the AI model.

Findings & Open questions:

    In the GroundingwithBingTool, when I checked the run information from AI Foundry Playground, somehow "market" is set to sv-SE, which is not the value specified in the instantiated.
        bing = BingGroundingTool(connection_id=bing_conn_id, freshness="day", count=5, set_lang="en", market="us")
        This is the output I got from the Playground:
            bing_grounding: {
                requesturl: "https://api.bing.microsoft.com/v7.0/search?q=search(query: "latest Microsoft news June 2025 significant business impact")"
                response_metadata: "{'market': 'sv-SE', 'num_docs_retrieved': 5, 'num_docs_actually_used': 5}"
            }

    Not sure how to specify query parameters. User query to the agent is re-fomulated to a Bing search query (requesturl: "https://api.bing.microsoft.com/v7.0/search?q=search(query: "......").
"""

# Import necessary libraries and modules
import os
from azure.identity import DefaultAzureCredential
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import MessageRole, BingGroundingTool

from dotenv import load_dotenv
load_dotenv()

# Retrieve endpoint, connection ID, and model deployment name from environment variables
project_endpoint = os.environ["AZURE_AI_FOUNDRY_PROJECT_ENDPOINT"]  # Ensure the PROJECT_ENDPOINT environment variable is set
# Ensure the BING_CONNECTION_ID environment variable is set, following the format:
#"/subscriptions/<sub-id>/resourceGroups/<your-rg-name>/providers/Microsoft.CognitiveServices/accounts/<your-ai-services-name>/projects/<your-project-name>/connections/<your-bing-connection-name>"
bing_conn_id = os.environ["BING_CONNECTION_ID"]  
model_deployment_name = os.environ["AZURE_AI_FOUNDRY_MODEL_DEPLOYMENT_NAME"]  # Ensure the MODEL_DEPLOYMENT_NAME environment variable is set

agent_id = os.environ["AZURE_AI_AGENTS_AGENT_ID"]  
thread_id = os.environ["AZURE_AI_AGENTS_THREAD_ID"]  


"""
I don't see too much value of the azure.ai.projects.AIProjectClient
# Initialize the AIProjectClient with the endpoint and credentials
project_client = AIProjectClient(
    endpoint=project_endpoint,
    credential=DefaultAzureCredential(),  # Use Azure Default Credential for authentication
    api_version="2025-05-15-preview", # "latest" is not a valid value for api_version, so specify a specific version
)
"""


agents_client = AgentsClient(
    endpoint=os.environ["AZURE_AI_FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
# [END create_project_client]


with agents_client:
    # Initialize agent bing tool and add the connection id
    bing = BingGroundingTool(connection_id=bing_conn_id, freshness="day", count=5, set_lang="en", market="us")

    for agent in agents_client.list_agents(limit=100):
        print(agent.id, agent.name)

    agent = agents_client.create_agent(
        model=model_deployment_name,
        name="agent-with-bing-grounding",
        instructions="You are a helpful agent",
        tools=bing.definitions,
    )

    print(f"Created agent, ID: {agent.id}")
    agent = agents_client.get_agent(agent.id)
    print(f"Created agent, ID: {agent.id}")


    # Create thread for communication
    thread = agents_client.threads.create()
    print(f"Created thread, ID: {thread.id}")
    thread = agents_client.threads.get(thread.id)
    print(f"Created thread, ID: {thread.id}")

    # Create message to thread
    message = agents_client.messages.create(
        thread_id=thread.id,
        role=MessageRole.USER,
        content="What is the latest news of Microsoft? Give me top 3 news articles with their summaries. Importantly, do analyze business impacts or implications of these news articles, show me only significant news articles that have business impacts.",
    )
    print(f"Created message, ID: {message.id}")

    # Create and process agent run in thread with tools
    run = agents_client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)
    print(f"Run finished with status: {run.status}")

    if run.status == "failed":
        print(f"Run failed: {run.last_error}")

    # Fetch run steps to get the details of the agent run
    run_steps = agents_client.run_steps.list(thread_id=thread.id, run_id=run.id)
    for step in run_steps:
        print(f"Step {step['id']} status: {step['status']}")
        step_details = step.get("step_details", {})
        tool_calls = step_details.get("tool_calls", [])
        
        if tool_calls:
            print("  Tool calls:")
            for call in tool_calls:
                print(f"    Tool Call ID: {call.get('id')}")
                print(f"    Type: {call.get('type')}")

                bing_grounding_details = call.get("bing_grounding", {})
                if bing_grounding_details:
                    print(f"    Bing Grounding ID: {bing_grounding_details.get('requesturl')}")
        else:
            print("  No tool calls found in this step.")
            print(step_details)
        print()  # add an extra newline between steps

    # Delete the agent when done
    #agents_client.delete_agent(agent.id)
    print("Deleted agent")

    # Print the Agent's response message with optional citation
    response_message = agents_client.messages.get_last_message_by_role(thread_id=thread.id, role=MessageRole.AGENT)
    if response_message:
        for text_message in response_message.text_messages:
            print(f"Agent response: {text_message.text.value}")
        for annotation in response_message.url_citation_annotations:
            print(f"URL Citation: [{annotation.url_citation.title}]({annotation.url_citation.url})")
