# coordinator/logging.py

from datetime import datetime

def log_event(agent_name: str, event_type: str, message: str) -> None:
    """
    Logs an event with a timestamp, agent name, event type, and message.

    Parameters:
        agent_name (str): Name of the agent emitting the log.
        event_type (str): Type of the event (e.g., Initialized, Processing, Completed).
        message (str): Message describing the event.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [EVENT from {agent_name}] [{event_type}] {message}")
