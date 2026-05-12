import argparse
from cerebro.core.analyzer import PatternAnalyzer
from cerebro.core.generator import PatternGenerator
from cerebro.core.validator import PatternValidator
from cerebro.core.store import PatternStore

def main():
    parser = argparse.ArgumentParser(description="Cerebro: Agentic Pattern Orchestrator")
    parser.add_argument("--root", type=str, default=".", help="Root directory to analyze")
    parser.add_argument("--target", type=str, help="Target name for generation")
    args = parser.parse_args()

    print("🚀 Starting Cerebro Orchestrator...")

    # 1. Discovery & Orchestration
    analyzer = PatternAnalyzer(args.root)
    potential_patterns = analyzer.find_potential_patterns()

    if not potential_patterns:
        print("❌ No patterns discovered.")
        return

    for pattern_name, paths in potential_patterns.items():
        print(f"\n🔍 Analyzing {pattern_name} pattern group...")
        # This is where the "Agentic Synthesis" happens
        synthesis = analyzer.analyze_pattern_group(paths)

        # Store the result
        store = PatternStore()
        store.save_pattern(pattern_name, synthesis)

        if args.target:
            print(f"🛠️ Generating {args.target} based on {pattern_name} synthesis...")
            generator = PatternGenerator()
            code = generator.generate(synthesis, args.target)

            validator = PatternValidator()
            if validator.validate(code, synthesis):
                print("\n--- Generated Code ---\n")
                print(code)
                print("\n----------------------")

if __name__ == "__main__":
    main()
