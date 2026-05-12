import argparse
from cerebro.core.governor import Governor
from cerebro.core.generator import PatternGenerator
from cerebro.core.validator import PatternValidator
from cerebro.core.store import PatternStore

def main():
    parser = argparse.ArgumentParser(description="Cerebro: Agentic Pattern Orchestrator")
    parser.add_argument("--root", type=str, default=".", help="Root directory to analyze")
    parser.add_argument("--target", type=str, help="Target name for generation")
    args = parser.parse_args()

    print("🚀 Starting Cerebro Governor...")

    # 1. Initialize the Governor
    governor = Governor(args.root)

    # 2. Orchestrate Discovery, Study, and Synthesis
    # The Governor manages the specialized agents internally
    synthesized_patterns = governor.orchestrate_pattern_discovery()

    if not synthesized_patterns:
        print("❌ No patterns discovered through agentic synthesis.")
        return

    for pattern_name, synthesis in synthesized_patterns.items():
        print(f"\n✅ Synthesized pattern group: [{pattern_name}]")

        # Store the formal synthesis
        store = PatternStore()
        store.save_pattern(pattern_name, synthesis)

        if args.target:
            print(f"🛠️ Generating {args.target} based on {pattern_name} synthesis...")
            generator = PatternGenerator()
            code = generator.generate(synthesis, args.target)

            validator = PatternValidator()
            if validator.validate(code, synthesis):
                print("\n--- Agentically Generated Code ---\n")
                print(code)
                print("\n----------------------------------")

if __name__ == "__main__":
    main()
