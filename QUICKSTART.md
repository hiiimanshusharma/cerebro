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

1. **Scan**: Cerebro looks for files ending in common suffixes like `Service`, `Repository`, or `Controller`.
2. **Analyze**: It groups these files and creates a "Study Request" specifying extraction goals (e.g., shared method signatures, boilerplate).
3. **Synthesize**: It simulates the findings of a Study Agent to create a formalized pattern.
4. **Generate**: If a `--target` is provided, it uses the synthesis to produce a new code snippet that matches the existing architectural symmetry of your project.
