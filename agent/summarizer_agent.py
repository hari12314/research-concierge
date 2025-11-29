import uuid
from coordinator.logging import log_event

class SummarizerAgent:
    def __init__(self):
        self.name = "SummarizerAgent"
        log_event(self.name, "Initialized", "Summarizer agent ready")

    def process(self, message):
        log_event(self.name, "Message Received", message)

        payload = message["payload"]
        summary = f"Summary of '{payload['title']}':\nThis paper explores modern developments in ML. It covers key innovations and their applications."

        response = {
            "task_id": message["task_id"],
            "from": self.name,
            "to": "Coordinator",
            "type": "summarized_text",
            "payload": {"summary": summary},
            "trace_id": str(uuid.uuid4())
        }

        log_event(self.name, "Message Sent", response)
        return response
