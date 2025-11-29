from coordinator.coordinator_agent import CoordinatorAgent

def main():
    print("\n=== Research Concierge CLI ===")
    query = input("Enter your research query: ")

    coord = CoordinatorAgent()
    final_result = coord.handle_query(query)

    print("\n========== PIPELINE OUTPUT ==========")
    print("\n--- Retrieval ---")
    print(final_result["retrieval"]["payload"])

    print("\n--- Extraction ---")
    print(final_result["extraction"]["payload"])

    print("\n--- Summary ---")
    print(final_result["summary"]["payload"])

    print("\n--- Evaluation ---")
    print(final_result["evaluation"]["payload"])

if __name__ == "__main__":
    main()
