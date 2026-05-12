# 🚀 Quickstart: Cerebro

Get started with Cerebro, the Agentic Pattern Orchestrator, in just a few steps.

## 📦 Installation

Cerebro is designed to run as a Python module. Ensure you have Python 3.8+ installed.

```bash
# Clone the repository
git clone <your-repo-url>
cd saac

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate
```

## 🛠️ Basic Usage

### 1. Discover Patterns
To scan your current directory for structural patterns (Services, Repositories, etc.) and synthesize them:

```bash
python3 -m cerebro.cli --root .
```

### 2. Discover and Generate
To find patterns and then use one of them to generate a new target artifact:

```bash
python3 -m cerebro.cli --root . --target "UserPaymentService"
```

## 📖 Command Line Options

| Option | Description | Default |
| :--- | :--- | :--- |
| `--root` | The root directory to analyze for patterns | `.` |
| `--target` | The name of the artifact to generate based on synthesized patterns | N/A |

## 🔍 How it Works

1. **Scan**: The Governor looks for files ending in common suffixes like `Service`, `Repository`, or `Controller`.
2. **Orchestrate**: The Governor delegates a study request to a **Study Agent** to extract structural traits and cross-language symmetry.
3. **Synthesize**: A **Synthesis Agent** formalizes the raw findings into a pattern definition with core constraints.
4. **Generate**: If a `--target` is provided, it uses the formalized synthesis to produce a new code snippet that matches the existing architectural symmetry of your project.
