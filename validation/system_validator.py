"""
=========================================================
QUANT ULTRA
System Validator
=========================================================
"""

import importlib
import os
import sys

# Ensure project root is in sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# Ensure UTF-8 console output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


class SystemValidator:

    def __init__(self):

        self.results = []

    # -------------------------------------------------

    def check(self, name, module):

        try:

            importlib.import_module(module)

            self.results.append(

                (name, True)

            )

        except Exception as e:

            self.results.append(

                (

                    name,

                    False,

                    str(e),

                )

            )

    # -------------------------------------------------

    def validate(self):

        print()

        print("=" * 70)

        print("🔍 QUANT ULTRA SYSTEM VALIDATION")

        print("=" * 70)

        modules = [

            ("Configuration", "config.settings"),

            ("Historical", "market.historical"),

            ("WebSocket", "market.websocket_manager"),

            ("Scanner", "scanner.multi_symbol_scanner"),

            ("Analyzer", "engine.live_analyzer"),

            ("Risk", "risk.risk_manager"),

            ("Decision", "decision.engine"),

            ("Order Manager", "orders.order_manager"),

            ("Paper Trader", "paper.paper_trader"),

            ("Dashboard", "dashboard.dashboard"),

            ("Reports", "reports.report_generator"),

            ("Database", "database.database"),

            ("Pipeline", "pipeline.integration_engine"),

        ]

        for name, module in modules:

            self.check(

                name,

                module,

            )

        passed = 0

        failed = 0

        print()

        for result in self.results:

            if result[1]:

                passed += 1

                print(

                    f"✅ {result[0]}"

                )

            else:

                failed += 1

                print(

                    f"❌ {result[0]}"

                )

                print(

                    f"   {result[2]}"

                )

        print()

        print("=" * 70)

        print(f"Passed : {passed}")

        print(f"Failed : {failed}")

        print("=" * 70)

        return failed == 0


# ---------------------------------------------------------

if __name__ == "__main__":

    validator = SystemValidator()

    validator.validate()