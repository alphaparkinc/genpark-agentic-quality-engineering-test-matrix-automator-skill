from client import AgenticQualityEngineeringTestMatrixAutomatorClient

def main():
    client = AgenticQualityEngineeringTestMatrixAutomatorClient()
    spec = {"suite_name": "E-Commerce Checkout Flow", "scenarios_count": 24}
    res = client.execute_qe_matrix(spec, ["Chromium", "WebKit", "Firefox"])
    print(f"Pass Rate: {res['test_pass_rate_pct']}%")
    print(f"Healed Locators: {res['healed_locators_count']}")
    print(f"Matrix Score: {res['matrix_coverage_score']}/10")

if __name__ == "__main__":
    main()
