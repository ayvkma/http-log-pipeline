import random
import json
from datetime import datetime
from pathlib import Path
from utils import generate_logs, generate_iso_timestamps

class Generator:
    """
    This service generates logs in jsonl format and saves them to provided file.
    """
    def __init__(self, seed, file):
        self.seed = seed
        random.seed(seed)
        self.file = Path(file)
    
    def generate_and_save_logs(self, total_logs):
        """
        This method generates logs and saves them to a file.
        """
        timestamps = generate_iso_timestamps(total_logs)
        logs = generate_logs(total_logs)
        
        for log, timestamp in zip(logs, timestamps):
            log['timestamp'] = timestamp
            with open(self.file, 'a') as file:
                file.write(json.dumps(log) + '\n')
                
        
        