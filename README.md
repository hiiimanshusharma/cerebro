# 🧠 Cerebro: Agentic Pattern Orchestrator

Cerebro is an intelligent system designed to identify, synthesize, and replicate structural patterns across diverse codebases. Unlike traditional static analysis tools that rely solely on AST parsing, Cerebro employs an **Agentic Synthesis** approach to recognize "structural symmetry"—patterns that emerge across different programming languages and frameworks.

## 🚀 Core Philosophy: Agentic Synthesis

Cerebro treats pattern discovery as an orchestration problem. It doesn't just look for matching strings; it orchestrates "Study Agents" to analyze groups of files and extract the underlying intent, interface, and boilerplate structures that define a pattern.

**The Cerebro Workflow:**
1. **Discovery**: Scans the codebase for naming conventions and structural hints (e.g., `*Service`, `*Repository`).
2. **Orchestration**: Groups related files and generates a "Study Request" for an agent.
3. **Synthesis**: Processes agent findings to formalize a pattern template.
4. **Generation**: Leverages the synthesized pattern to generate new, consistent code artifacts.

## 🏗️ Architecture

Cerebro is organized into a core engine and a plugin-ready architecture:

- **`cerebro.core.analyzer`**: The Discovery Engine. It identifies potential patterns and orchestrates the study requests.
- **`cerebro.core.generator`**: The Synthesis Engine. It transforms synthesized patterns into concrete code.
- **`cerebro.core.validator`**: Ensures generated code adheres to the synthesized pattern constraints.
- **`cerebro.core.store`**: Manages the persistence of synthesized patterns.
- **`cerebro.cli`**: The primary interface for interacting with the orchestrator.

## 🛠️ Supported Patterns

By default, Cerebro recognizes the following architectural patterns:
- `Adapter`
- `Service`
- `Repository`
- `Handler`
- `Controller`

## 🌐 Language Support

Cerebro is designed for polyglot environments, scanning for patterns across:
- Python (`.py`)
- Rust (`.rs`)
- Ruby (`.rb`)
- Go (`.go`)
- TypeScript/React (`.ts`, `.tsx`)
