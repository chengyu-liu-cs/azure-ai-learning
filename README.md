> this repo is used for document learnings and findings for catching up technology progress.

# Azure AI Learning Notes
## Auzre AI Foundry 

### Update announcement 
- [2025-05-27 Introducing New Tools and Features in the Responses API in Azure AI Foundry](https://devblogs.microsoft.com/foundry/introducing-new-tools-and-features-in-the-responses-api-in-azure-ai-foundry/)
]
- [2025-05-27 Azure AI Foundry MCP Server May 2025 Update: Adding Models, Knowledge & Evaluation](https://devblogs.microsoft.com/foundry/azure-ai-foundry-mcp-server-may-2025/)


## MCP
### Interesting blogs, repos and Azure documentation:
- [AI Automation in Azure Foundry through turnkey MCP Integration and Computer Use Agent Models](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/ai-automation-in-azure-foundry-through-turnkey-mcp-integration-and-computer-use-/4424098)
- [Fashion Trends Compiler Agent with Azure OpenAI Responses API](https://github.com/MSFT-Innovation-Hub-India/CUA-Trends-Compiler)
- [Azure MCP Server](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/overview)
  - [Azure MCP Server Github repo](https://github.com/Azure/azure-mcp)
  - [Azure Multi MCP Starter](https://github.com/delynchoong/azure-openai-agent-multi-mcp-starter)
- [MCP tool bindings for Azure Functions overview](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-mcp?pivots=programming-language-python)
-[]()

### MCP + Azure API Management
- [AI gateway capabilities in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)
- [Expose REST API in API Management as an MCP server](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Register and discover remote MCP servers in your API inventory](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [APIM ❤️ AI Agents
Model Context Protocol (MCP) Registry lab](https://github.com/Azure-Samples/AI-Gateway/blob/main/labs/mcp-registry-apic/mcp-registry-apic.ipynb)
- [Azure API Management Your Auth Gateway For MCP Servers]https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
## Public Repositories

### [Solution Accelerators](https://github.com/microsoft/solution-accelerators)
### [Templates in AI Foundry](https://ai.azure.com/code)
### [Content processing solution accelerator](https://github.com/microsoft/content-processing-solution-accelerator/tree/main)
### Azure AI Agent Service-enterprise-demo

This sample demonstrates how to build a streaming enterprise agent using Azure AI Agent Service. The agent can answer questions in real time using local HR and company policy documents, integrate external context via Bing, using gpt-4o-2024-05-13.

https://github.com/Azure-Samples/azure-ai-agent-service-enterprise-demo/tree/main

#### Features

This demo teaches developers how to:
- **Create or Reuse Agents Programmatically**  

- **Incorporate Vector Stores for Enterprise Data**  
  **Optional:** If the default file search tool isn’t available, the notebook automatically attempts direct Azure AI Search integration via environment variables.

- **Integrate Server-Side Tools**  

- **Extend Functionality with Azure Logic Apps**  

- **Stream Real-Time Agent Responses**  

- **Build an Interactive Gradio UI**  
![gif demo](https://github.com/Azure-Samples/azure-ai-agent-service-enterprise-demo/blob/main/assets/demo-short-3-2.gif?raw=true)

### [AI Gateway Labs with Azure API Management](https://github.com/Azure-Samples/AI-Gateway/tree/main)
#### Features
See labs below to try out new and exciting features:
 
➕ **Realtime API (Audio and Text) with Azure OpenAI 🔥** experiments with the [**AOAI Realtime**](labs/realtime-audio/realtime-audio.ipynb)  
➕ **Realtime API (Audio and Text) with Azure OpenAI + MCP tools 🔥** experiments with the [**AOAI Realtime + MCP**](labs/realtime-mcp-agents/realtime-mcp-agents.ipynb)  
➕ **Model Context Protocol (MCP) ⚙️** experiments with the [**client authorization flow**](labs/mcp-client-authorization/mcp-client-authorization.ipynb)  
➕ the [**FinOps Framework**](labs/finops-framework/finops-framework.ipynb) lab to manage AI budgets effectively 💰  
➕ **Agentic ✨** experiments with [**Model Context Protocol (MCP)**](labs/model-context-protocol/model-context-protocol.ipynb).  
➕ **Agentic ✨** experiments with [**OpenAI Agents SDK**](labs/openai-agents/openai-agents.ipynb).  
➕ **Agentic ✨** experiments with [**AI Agent Service**](labs/ai-agent-service/ai-agent-service.ipynb) from [Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-foundry).  
➕ the [**AI Foundry Deepseek**](labs/ai-foundry-deepseek/ai-foundry-deepseek.ipynb) lab with Deepseek R1 model from [Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-foundry).  
➕ the [**Zero-to-Production**](labs/zero-to-production/zero-to-production.ipynb) lab with an iterative policy exploration to fine-tune the optimal production configuration.  
➕ the [**Terraform flavor  of backend pool load balancing**](labs/backend-pool-load-balancing-tf/backend-pool-load-balancing-tf.ipynb) lab.  
➕ the [**AI Foundry SDK**](labs/ai-foundry-sdk/ai-foundry-sdk.ipynb) lab.  
➕ the [**Content filtering**](labs/content-filtering/content-filtering.ipynb) and [**Prompt shielding**](labs/content-filtering/prompt-shielding.ipynb) labs.  
➕ the [**Model routing**](labs/model-routing/model-routing.ipynb) lab with OpenAI model based routing.  
➕ the [**Prompt flow**](labs/prompt-flow/prompt-flow.ipynb) lab to try the [Azure AI Studio Prompt Flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) with Azure API Management.  
➕ `priority` and `weight` parameters to the [**Backend pool load balancing**](labs/backend-pool-load-balancing/backend-pool-load-balancing.ipynb) lab.  
➕ the [**Streaming**](streaming.ipynb) tool to test OpenAI streaming with Azure API Management.  
➕ the [**Tracing**](tools/tracing.ipynb) tool to debug and troubleshoot OpenAI APIs using [Azure API Management tracing capability](https://learn.microsoft.com/azure/api-management/api-management-howto-api-inspector).  
➕ image processing to the [**GPT-4o inferencing**](labs/GPT-4o-inferencing/GPT-4o-inferencing.ipynb) lab.  
➕ the [**Function calling**](labs/function-calling/function-calling.ipynb) lab with a sample API on Azure Functions.