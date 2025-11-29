import uuid
from coordinator.logging import log_event

def make_message(sender, receiver, msg_type, payload):
    msg = {
        "task_id": str(uuid.uuid4()),
        "from": sender,
        "to": receiver,
        "type": msg_type,
        "payload": payload,
        "trace_id": str(uuid.uuid4())
    }
    log_event(sender, "Message Created", msg)
    return msg

# Simple in-memory router
message_queue = []

def send_message(message):
    message_queue.append(message)
    log_event(message["from"], "Message Sent", message)

def receive_messages(receiver):
    msgs_for_receiver = [m for m in message_queue if m["to"] == receiver]
    for m in msgs_for_receiver:
        message_queue.remove(m)
        log_event(receiver, "Message Received", m)
    return msgs_for_receiver
