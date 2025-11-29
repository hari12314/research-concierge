# scripts/test_week2.py
from agent.coordinator_agent import CoordinatorAgent

session_id = "week2_test"
query = "Attention Is All You Need"

coordinator = CoordinatorAgent()
output = coordinator.process_paper(session_id, query)

print("\n=== Pipeline Output ===")
print(output)
