# Cerebro: Agentic Pattern Orchestrator

Cerebro is a technical framework designed to identify, synthesize, and replicate structural patterns across diverse codebases. Unlike traditional static analysis tools that rely solely on Abstract Syntax Tree (AST) parsing, Cerebro employs an Agentic Synthesis approach to recognize structural symmetry—patterns that emerge across different programming languages and frameworks.

## Technical Approach: Agentic Synthesis

Cerebro treats pattern discovery as an orchestration problem. Rather than searching for matching strings, it orchestrates specialized Study Agents to analyze groups of files and extract the underlying intent, interface, and boilerplate structures that define a pattern.

### Operational Workflow:
1. **Discovery**: Scans the codebase for naming conventions and structural indicators (e.g., `*Service`, `*Repository`).
2. **Orchestration**: Groups related files and generates a Study Request for the agent.
3. **Synthesis**: Processes agent findings to formalize a pattern template.
4. **Generation**: Leverages the synthesized pattern to generate new, consistent code artifacts.

## Architecture

Cerebro is built upon a core engine with a plugin-ready architecture:

- **`cerebro.core.governor`**: The Central Orchestrator. Manages the full lifecycle from Discovery to Generation, coordinating `StudyAgent` and `SynthesisAgent` to perform agentic synthesis.
- **`cerebro.core.generator`**: The Synthesis Engine. Transforms formalized patterns into concrete code.
- **`cerebro.core.validator`**: Ensures generated code adheres to the synthesized pattern constraints.
- **`cerebro.core.store`**: Manages the persistence of synthesized patterns.
- **`cerebro.cli`**: The primary command-line interface for interacting with the Governor.

## Supported Patterns

By default, Cerebro recognizes the following architectural patterns:
- Adapter
- Service
- Repository
- Handler
- Controller

## Language Support

Cerebro is designed for polyglot environments, supporting pattern recognition across:
- Python (`.py`)
- Rust (`.rs`)
- Ruby (`.rb`)
- Go (`.go`)
- TypeScript/React (`.ts`, `.tsx`)
