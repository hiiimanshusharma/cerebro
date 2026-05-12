# Codebase Skill Template

A template for creating Agent Skills from an existing codebase. Use this to produce skills that let Claude (or any AI agent) add features to the codebase, or scaffold new codebases based on the same patterns.

---

## Directory Structure

```
your-skill-name/
├── SKILL.md                  # Entry point — loaded when skill triggers
├── ARCHITECTURE.md           # Layer 0-2: identity, structure, data flow
├── CONVENTIONS.md            # Layer 3: rules, patterns, anti-patterns
├── TEMPLATES.md              # Concrete file templates for the repeatable action
├── EXAMPLES.md               # One complete worked example (input → output)
└── scripts/                  # Optional: utility scripts Claude executes
    ├── scaffold.py           # Scaffold new files from templates
    └── validate.py           # Validate output correctness
```

All reference files are one level deep from SKILL.md (no nested chains).

---

## SKILL.md — The Entry Point

```markdown
---
name: your-skill-name
description: >
  [What it does] and [when to trigger it]. Write in third person.
  Include specific trigger terms the user might say.
  Max 1024 chars. Be precise — this is how Claude picks your skill
  from 100+ options.
---

# [Skill Title]

## What this skill does

[One paragraph. What repeatable action does this skill perform?
What is the input, what is the output? Who is this for?]

## When to use

- [Trigger condition 1 — e.g., "User asks to add a new adapter"]
- [Trigger condition 2 — e.g., "User asks to scaffold a service from this template"]

## Quick start

[The simplest possible invocation — 3-5 lines that show the
happy path. This is what Claude reads first and may be all it
needs for simple cases.]

```bash
# Example: scaffold a new adapter
python scripts/scaffold.py --type adapter --name redis
```

## Workflow

Copy this checklist and track progress:

```
Task Progress:
- [ ] Step 1: [Read context]
- [ ] Step 2: [Generate files]
- [ ] Step 3: [Integrate]
- [ ] Step 4: [Validate]
- [ ] Step 5: [Verify]
```

**Step 1: Read context**

Read [ARCHITECTURE.md](ARCHITECTURE.md) to understand where the new
code fits in the system. If this is a [specific task type], also
read [CONVENTIONS.md](CONVENTIONS.md) for patterns to follow.

**Step 2: Generate files**

Create the following files using templates from [TEMPLATES.md](TEMPLATES.md):

- `path/to/new_file.py` — [what it does]
- `path/to/test_file.py` — [what it tests]
- `path/to/config_entry` — [what it configures]

**Step 3: Integrate**

Register the new [component] in [registry/config location]:

[Minimal code showing the registration step]

**Step 4: Validate**

```bash
python scripts/validate.py path/to/new_file.py
```

If validation fails, fix the reported issues and re-run.

**Step 5: Verify**

```bash
[test command — e.g., pytest tests/ -k new_component]
```

## Decision points

**Creating new [component]?** → Follow Steps 1-5 above
**Modifying existing [component]?** → Read the existing file first,
apply changes following [CONVENTIONS.md](CONVENTIONS.md), then skip to Step 4
**Building a new project from this pattern?** → See "Scaffold mode" below

## Scaffold mode (new project from pattern)

For creating a new codebase based on the same architecture:

1. Read [ARCHITECTURE.md](ARCHITECTURE.md) — understand the three-layer
   structure and adapt the module names to the new domain
2. Use [TEMPLATES.md](TEMPLATES.md) — every template is parameterized;
   replace domain-specific names with the new project's terms
3. Validate the dependency direction: core ← adapters ← starters
   (dependencies point inward, never outward)

## Reference files

- **Architecture & structure**: [ARCHITECTURE.md](ARCHITECTURE.md)
- **Coding conventions & rules**: [CONVENTIONS.md](CONVENTIONS.md)
- **File templates**: [TEMPLATES.md](TEMPLATES.md)
- **Worked example**: [EXAMPLES.md](EXAMPLES.md)
```

---

## ARCHITECTURE.md — Layers 0-2

```markdown
# Architecture Reference

## Contents
- What is this system
- Major components
- How components connect
- Key data shapes

## What is this system

[Layer 0 — Identity. One paragraph: what the software does, who uses
it, why it exists. This orients every subsequent decision.]

Example:
> Agent Factory SDK is a three-package Python toolkit that lets
> pharma consulting teams build AI agent applications. ~200
> developers use it. It abstracts LLM providers, vector DBs, and
> data sources behind a unified adapter interface.

## Major components

[Layer 1 — Structure. The 4-7 top-level modules. One line each.
This is the box diagram.]

| Module | Purpose |
|--------|---------|
| `core/` | Runtime, base classes, config loading, lifecycle |
| `adapters/` | Wraps external services (LLM, storage, vector DB) behind standard interfaces |
| `starters/` | Project templates and CLI scaffolding |
| `cli/` | Developer entry point — scaffold, sync, ship commands |

Dependency direction: `starters → adapters → core` (never reversed).

## How components connect

[Layer 2 — Data flow. Which modules call which, what shapes
flow between them. Focus on boundaries.]

```
User runs CLI command
  → CLI reads config (YAML/env)
    → Starter template scaffolds project structure
      → Adapters are instantiated from config
        → Core runtime manages lifecycle
```

Key interfaces between layers:
- Core exposes `BaseAdapter` — all adapters extend this
- Adapters expose a `create()` factory — starters use this, never
  instantiate adapters directly
- Config schema is defined in core, consumed everywhere

## Key data shapes

[The Pydantic models / TypeScript interfaces / schemas that cross
boundaries. Read these before reading any logic.]

```python
# core/config.py
class AdapterConfig(BaseModel):
    adapter_type: str        # e.g., "openai", "redis", "opensearch"
    connection_params: dict  # adapter-specific connection details
    options: dict = {}       # optional tuning parameters
```
```

---

## CONVENTIONS.md — Layer 3

```markdown
# Coding Conventions

## Contents
- Naming rules
- File organization
- Pattern: how to write an adapter
- Pattern: how to write a test
- Anti-patterns (do NOT do these)

## Naming rules

- Files: `snake_case.py`
- Classes: `PascalCase`, suffixed by type (`StorageAdapter`, `LLMAdapter`)
- Config keys: `snake_case`, matching the adapter class name without suffix
- Tests: `test_<module_name>.py`, test functions `test_<behavior>()`

## File organization

Every adapter lives in `adapters/<category>/<name>/`:
```
adapters/
  storage/
    redis/
      __init__.py
      adapter.py        # The adapter implementation
      config.py         # Adapter-specific config schema
      exceptions.py     # Adapter-specific exceptions (if any)
  llm/
    openai/
      ...
```

## Pattern: how to write an adapter

[This is the core pattern — the reusable "how" that makes this a skill.]

1. Extend `BaseAdapter` from core
2. Implement all abstract methods (the base class enforces this)
3. Accept config via `__init__(self, config: AdapterConfig)`
4. Raise `AdapterError` subclasses for failures, never raw exceptions
5. Register in `adapters/__init__.py` ADAPTER_REGISTRY dict
6. Write one integration test and one unit test (mock the external service)

Degree of freedom: medium. The structure is fixed; the internal
implementation logic is yours to decide.

## Pattern: how to write a test

```python
# Minimal test template
class TestMyAdapter:
    def test_create_returns_instance(self, config):
        adapter = MyAdapter(config)
        assert isinstance(adapter, BaseAdapter)

    def test_required_method_works(self, config, mock_service):
        adapter = MyAdapter(config)
        result = adapter.do_thing(input_data)
        assert result.status == "success"
```

## Anti-patterns

- NEVER import from `starters/` into `core/` or `adapters/`
- NEVER hardcode connection strings; always use config
- NEVER catch and silently swallow exceptions
- NEVER add a dependency on `core` to an adapter's external package
- NEVER put business logic in the CLI layer; it belongs in core or adapters
```

---

## TEMPLATES.md — Parameterized File Templates

```markdown
# File Templates

## New adapter

### adapter.py

```python
"""
{AdapterName} adapter for {service_description}.
"""
from agent_factory_sdk_core.base import BaseAdapter, AdapterConfig

class {AdapterName}Adapter(BaseAdapter):
    """Wraps {service_name} behind the standard adapter interface."""

    def __init__(self, config: AdapterConfig):
        super().__init__(config)
        # Initialize {service_name} client here

    def connect(self) -> None:
        """Establish connection to {service_name}."""
        raise NotImplementedError

    def disconnect(self) -> None:
        """Tear down connection."""
        raise NotImplementedError

    def health_check(self) -> bool:
        """Return True if {service_name} is reachable."""
        raise NotImplementedError
```

### config.py

```python
from pydantic import BaseModel

class {AdapterName}Config(BaseModel):
    """Configuration for {AdapterName}Adapter."""
    host: str
    port: int = {default_port}
    # Add {service_name}-specific config fields
```

### test_adapter.py

```python
import pytest
from unittest.mock import MagicMock

class Test{AdapterName}Adapter:
    @pytest.fixture
    def config(self):
        return {AdapterName}Config(host="localhost", port={default_port})

    def test_instantiation(self, config):
        adapter = {AdapterName}Adapter(config)
        assert adapter is not None

    def test_health_check(self, config):
        adapter = {AdapterName}Adapter(config)
        # Mock the underlying client
        adapter._client = MagicMock()
        assert adapter.health_check() is True
```

### Registration entry

Add to `adapters/__init__.py`:
```python
ADAPTER_REGISTRY["{adapter_key}"] = "{AdapterName}Adapter"
```

## Template parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `{AdapterName}` | PascalCase adapter name | `Redis`, `OpenSearch` |
| `{adapter_key}` | snake_case registry key | `redis`, `open_search` |
| `{service_name}` | Human-readable service name | `Redis`, `OpenSearch` |
| `{service_description}` | Brief purpose | `in-memory key-value store` |
| `{default_port}` | Default port number | `6379`, `9200` |
```

---

## EXAMPLES.md — One Complete Worked Example

```markdown
# Worked Example: Adding the Redis Storage Adapter

This shows the complete output of running the "add adapter" skill
for a Redis storage adapter.

## Files created

### adapters/storage/redis/adapter.py

```python
"""
Redis adapter for in-memory key-value storage.
"""
from agent_factory_sdk_core.base import BaseAdapter, AdapterConfig
import redis

class RedisAdapter(BaseAdapter):
    def __init__(self, config: AdapterConfig):
        super().__init__(config)
        self._client = None

    def connect(self) -> None:
        self._client = redis.Redis(
            host=self.config.connection_params["host"],
            port=self.config.connection_params.get("port", 6379),
        )

    def disconnect(self) -> None:
        if self._client:
            self._client.close()

    def health_check(self) -> bool:
        try:
            return self._client.ping()
        except redis.ConnectionError:
            return False
```

### Registration diff

```diff
# adapters/__init__.py
 ADAPTER_REGISTRY = {
     "opensearch": "OpenSearchAdapter",
+    "redis": "RedisAdapter",
 }
```

### Test file

[Complete test file showing what "done" looks like]

## Why this example matters

- Shows the exact file structure and naming
- Shows how config flows from BaseAdapter
- Shows error handling pattern (catch service-specific, not generic)
- Shows the registration step that's easy to forget
```

---

## scripts/validate.py — Feedback Loop Script

```python
#!/usr/bin/env python3
"""
Validate a new adapter follows project conventions.

Usage: python scripts/validate.py adapters/storage/redis/adapter.py

Checks:
- Extends BaseAdapter
- Implements all required abstract methods
- Config uses Pydantic BaseModel
- Registered in ADAPTER_REGISTRY
- Has corresponding test file

Exit code 0 = pass, 1 = failures found.
"""
import ast
import sys
from pathlib import Path

REQUIRED_METHODS = ["connect", "disconnect", "health_check"]

def validate(adapter_path: str) -> list[str]:
    errors = []
    path = Path(adapter_path)

    if not path.exists():
        errors.append(f"File not found: {adapter_path}")
        return errors

    source = path.read_text()
    tree = ast.parse(source)

    # Check class extends BaseAdapter
    classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    adapter_classes = [
        c for c in classes
        if any("BaseAdapter" in ast.dump(b) for b in c.bases)
    ]
    if not adapter_classes:
        errors.append("No class extending BaseAdapter found")
        return errors

    # Check required methods
    cls = adapter_classes[0]
    methods = {n.name for n in cls.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
    for method in REQUIRED_METHODS:
        if method not in methods:
            errors.append(f"Missing required method: {method}")

    # Check test file exists
    test_path = path.parent / f"test_{path.name}"
    if not test_path.exists():
        # Also check tests/ directory
        alt_test = Path("tests") / path.parent.name / f"test_{path.name}"
        if not alt_test.exists():
            errors.append(f"No test file found at {test_path} or {alt_test}")

    return errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate.py <adapter_file.py>")
        sys.exit(1)

    errors = validate(sys.argv[1])
    if errors:
        print("Validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print("Validation passed.")
        sys.exit(0)
```

---

## How to Adapt This Template

### For "add feature to existing codebase" skills

1. **Identify the repeatable action** — look at your git log for PRs that follow the same pattern
2. **Trace one real instance** — list every file touched in a single PR
3. **Fill ARCHITECTURE.md** from your actual codebase's structure
4. **Fill CONVENTIONS.md** from your team's actual code review feedback
5. **Fill TEMPLATES.md** by parameterizing one real file from Step 2
6. **Fill EXAMPLES.md** with that same real instance, unparameterized
7. **Write validate.py** to catch the mistakes your team catches in review

### For "build new codebase from pattern" skills

1. Same as above, but abstract further in ARCHITECTURE.md — describe the *pattern* not the *instance*
2. In TEMPLATES.md, parameterize domain-specific terms (not just names)
3. In CONVENTIONS.md, separate universal rules from project-specific rules
4. Skip the registration steps (there's no existing registry to plug into)
5. Add a `scaffold.py` script that generates the full project skeleton

### Evaluation-driven refinement

Before writing extensive docs, test the skill:

1. Give Claude the skill + a fresh task ("add a MongoDB adapter")
2. Watch where it gets stuck or produces wrong output
3. Add to the skill only what fixes those specific failures
4. Repeat with 3+ different tasks

```json
{
  "skills": ["your-skill-name"],
  "query": "Add a new MongoDB storage adapter with connection pooling",
  "expected_behavior": [
    "Creates adapter.py extending BaseAdapter in correct directory",
    "Creates config.py with MongoDB-specific fields",
    "Registers in ADAPTER_REGISTRY",
    "Creates test file with at least 2 test cases",
    "Passes validate.py without errors"
  ]
}
```

---

## Checklist Before Shipping

- [ ] Description is third-person, specific, includes trigger terms
- [ ] SKILL.md body is under 500 lines
- [ ] Reference files are one level deep
- [ ] Workflow has numbered steps with a copyable checklist
- [ ] Validation/feedback loop is present
- [ ] One complete worked example in EXAMPLES.md
- [ ] Templates use consistent parameter naming
- [ ] Anti-patterns section covers real mistakes from code review history
- [ ] No time-sensitive information
- [ ] Consistent terminology throughout (one term per concept)
- [ ] Tested with a fresh Claude session on 3+ variations of the task
