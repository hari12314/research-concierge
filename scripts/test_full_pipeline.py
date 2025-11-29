from coordinator.coordinator_agent import CoordinatorAgent

if __name__ == "__main__":
    coord = CoordinatorAgent()

    final = coord.handle_query("Machine Learning papers 2025")
    print("\n========== FINAL OUTPUT ==========")
    print(final)
