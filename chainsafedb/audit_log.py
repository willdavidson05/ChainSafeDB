from datetime import datetime
import hashlib
import json

class AuditLogger:
    def __init__(self, blockchain_logger=None):
        self.events = []
        self.blockchain_logger = blockchain_logger

    def record_event(self, action_type, user, record_id, record_data):
        timestamp = datetime.utcnow().isoformat()
        event = {
            "timestamp": timestamp,
            "action": action_type,
            "user": user,
            "record_id": record_id,
        }

        fingerprint = hashlib.sha256(json.dumps(record_data, sort_keys=True).encode()).hexdigest()
        event["fingerprint"] = fingerprint

        self.events.append(event)

        if self.blockchain_logger:
            self.blockchain_logger.log_hash(fingerprint)

        print(f"Logged: {event}")
        return event
