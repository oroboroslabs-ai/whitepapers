# Oroboros Orchestrator OS: The Inference Router

## Core Function
To abstract the inference backend (API or Local) from the application logic, providing a unified RPC interface for agent deployment.

## Technical Architecture

### Unified Inference Gateway
Instead of vendor-specific SDKs, the Orchestrator exposes a single gRPC/REST endpoint (`/v1/inference`). It accepts a standardized payload (Prompt, Context, Model Constraints) and intelligently routes it to the appropriate backend (OpenAI, Anthropic, Local Ollama, vLLM) based on a cost-latency heuristic table.

### Skill Contract System
"Skills" are not vague concepts; they are Dockerized microservices defined by Protobuf contracts. Every skill must expose `ValidateInput()`, `Execute()`, and `FormatOutput()` methods. This ensures type safety and composability.

### Declarative YAML Pipeline
Agent logic is defined in YAML, which is compiled into a Directed Acyclic Graph (DAG) at runtime. The Orchestrator traverses this DAG to execute skill chains, handling memory passing between nodes via shared Redis streams.

## Tech Spec 1001

- **Protocol**: gRPC streaming for real-time token delivery
- **State Management**: Externalized state via Redis (or SQLite for edge), allowing the Orchestrator to restart without losing context
- **Vendor Agnosticism**: Implemented via a Strategy Pattern in the core router class