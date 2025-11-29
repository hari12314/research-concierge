from agents.retriever_agent import RetrieverAgent
from agents.extractor_agent import ExtractorAgent
from agents.summarizer_agent import SummarizerAgent
from agents.evaluator_agent import EvaluatorAgent
from coordinator.logging import log_event
import uuid

class CoordinatorAgent:
    def __init__(self):
        log_event("Coordinator", "Initialized", "Coordinator agent ready")
        self.retriever = RetrieverAgent()
        self.extractor = ExtractorAgent()
        self.summarizer = SummarizerAgent()
        self.evaluator = EvaluatorAgent()

    def handle_query(self, query):
        log_event("Coordinator", "Handling Query", query)

        # Step 1: Retrieval
        msg = {
            "task_id": str(uuid.uuid4()),
            "from": "Coordinator",
            "to": "RetrieverAgent",
            "type": "search",
            "payload": query,
            "trace_id": str(uuid.uuid4())
        }
        retrieval_result = self.retriever.process(msg)

        # Step 2: Extraction
        msg = {
            "task_id": str(uuid.uuid4()),
            "from": "Coordinator",
            "to": "ExtractorAgent",
            "type": "extract",
            "payload": retrieval_result["payload"],
            "trace_id": str(uuid.uuid4())
        }
        extraction_result = self.extractor.process(msg)

        # Step 3: Summarization
        msg = {
            "task_id": str(uuid.uuid4()),
            "from": "Coordinator",
            "to": "SummarizerAgent",
            "type": "summarize",
            "payload": extraction_result["payload"],
            "trace_id": str(uuid.uuid4())
        }
        summary_result = self.summarizer.process(msg)

        # Step 4: Evaluation
        msg = {
            "task_id": str(uuid.uuid4()),
            "from": "Coordinator",
            "to": "EvaluatorAgent",
            "type": "evaluate",
            "payload": summary_result["payload"],
            "trace_id": str(uuid.uuid4())
        }
        evaluation_result = self.evaluator.process(msg)

        final_output = {
            "retrieval": retrieval_result,
            "extraction": extraction_result,
            "summary": summary_result,
            "evaluation": evaluation_result
        }

        return final_output
