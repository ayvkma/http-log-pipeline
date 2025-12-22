import uuid
import random
from datetime import datetime, timedelta
from typing import List

# starting time for logs
today = datetime.now()
NOW = datetime(year=today.year, month=today.month, day=today.day, hour=0, minute=0, second=0)

def timestamps_in_range(start, end) -> List:
    """
    Generate timestamps within a given time range.

    :param start: The start time.
    :param end: The end time.
    :returns: A list of timestamps within the given range.
    :rtype: List
    """
    global NOW
    start = round(start)
    end = round(end)
    
    now = NOW
    
    timestamps = []
    
    windows = ['NORMAL', 'NORMAL', 'NORMAL', 'SPARSE', 'DENSE', 'NORMAL', 'SPARSE', 'NORMAL', 'SPARSE', 'NORMAL', 'DENSE', 'NORMAL']
    window = windows[random.randint(0, len(windows) - 1)]
    
    
    for i in range(start, end):
        interval = None
        if window == 'NORMAL':
            interval = timedelta(milliseconds=random.randint(10, 200))
        elif window == 'SPARSE':
            interval = timedelta(minutes=random.randint(1, 5))
        else:
            interval = timedelta(milliseconds=random.randint(1, 5))
        timestamp = now + interval
        now = timestamp
        timestamps.append(timestamp.isoformat())
        
    NOW = now
    return timestamps

def generate_iso_timestamps(number_of_logs) -> List:
    """
    Generate variable incrementing timestamps with varying duration between requests.
    
    :param number_of_logs: Number of Logs
    :returns: A list containing timestamps equal to number of logs.
    :rtype: List
    """
    timestamps = []
    
    timestamps_from_zero_to_ten_percent = timestamps_in_range(0, 0.1 * number_of_logs)    
    timestamps_from_ten_to_thirty_percent = timestamps_in_range(0.1 * number_of_logs, 0.3 * number_of_logs)    
    timestamps_from_thirty_to_forty_percent = timestamps_in_range(0.3 * number_of_logs, 0.4 * number_of_logs)    
    timestamps_from_forty_to_seventy_percent = timestamps_in_range(0.4 * number_of_logs, 0.7 * number_of_logs)    
    timestamps_from_seventy_to_eighty_percent = timestamps_in_range(0.7 * number_of_logs, 0.8 * number_of_logs)    
    timestamps_from_eighty_to_ninety_percent = timestamps_in_range(0.8 * number_of_logs, 0.9 * number_of_logs)    
    timestamps_from_ninety_to_hundred_percent = timestamps_in_range(0.9 * number_of_logs, number_of_logs)    
    
    timestamps.extend(timestamps_from_zero_to_ten_percent)
    timestamps.extend(timestamps_from_ten_to_thirty_percent)
    timestamps.extend(timestamps_from_thirty_to_forty_percent)
    timestamps.extend(timestamps_from_forty_to_seventy_percent)
    timestamps.extend(timestamps_from_seventy_to_eighty_percent)
    timestamps.extend(timestamps_from_eighty_to_ninety_percent)
    timestamps.extend(timestamps_from_ninety_to_hundred_percent)
    
    return timestamps

def generate_ip():
    """
    Generate a random ip from the stock list of IPs.
    
    :returns: A random IP
    :rtype: str
    """
    ips = [
    "23.91.184.12",
    "45.77.203.89",
    "103.82.156.44",
    "142.250.72.198",
    "54.179.33.7",
    "18.216.94.61",
    "8.34.67.221",
    "91.198.174.192",
    "66.249.64.87",
    "157.240.12.35"
    ]

    return ips[random.randint(0, len(ips) - 1)]

def generate_http_log():
    """
    Generate a random http request from stock requests based on a randomly generated method from stock methods.
    
    :returns: A HTTP Request
    :rtype: str
    """
    methods = ['GET', 'POST', 'PUT', 'DELETE']
    method = methods[random.randint(0, len(methods) - 1)]
    
    get_endpoints = ['/health 200', '/api/tasks/999 200' '/api/tasks/7 200', '/api/tasks 200', '/api/tasks/476 200', '/api/tasks/123 200', '/api/tasks/123 404', '/api/tasks/13 200']
    post_endpoints = ['/api/tasks 201', '/api/tasks 400', '/api/tasks/900 200', '/api/tasks/476 500', '/api/tasks/13 200']
    put_endpoints = ['/api/tasks/42 200', '/api/tasks/999 404', '/api/tasks/13 400', '/api/tasks/7 500', '/api/tasks/7 200']
    delete_endpoints = ['/api/tasks/42 204', '/api/tasks/999 404', '/api/tasks/89 200', '/api/tasks/5 500', '/api/tasks/5 204']
    
    method_to_endpoints = {
        'GET': get_endpoints,
        'POST': post_endpoints,
        'PUT': put_endpoints,
        'DELETE': delete_endpoints
    }
    
    possible_endpoints = method_to_endpoints[method]
    endpoint = possible_endpoints[random.randint(0, len(possible_endpoints) - 1)]
    
    return f"{method} {endpoint}"

def generate_request_duration(mode):
    """
    Generate a random response time for a http request based on provided mode.
    
    :param mode: A mode deciding the speed of request.
    :returns: Response time in milliseconds
    :rtype: int
    """
    low = None
    high = None
    
    if mode == 'FAST':
        low = 20
        high = 80
    elif mode == 'NORMAL':
        low = 80
        high = 300
    elif mode == 'SLOW':
        low = 300
        high = 1000
    else:
        low = 1000
        high = 3000
        
    return random.randint(low, high)
    
def generate_user_agent():
    """
    Generate a random user-agent from stock options.
    
    :returns: A random user-agent
    :rtype: str
    """
    user_agents = ['Mozilla', 'Chrome', 'Safari']
    return user_agents[random.randint(0, len(user_agents) - 1)]

def generate_log(mode):
    """
    Generates a single log for log file.
    
    :param mode: A mode deciding the speed of requests.
    :returns: An HTTP log as a dict.
    :rtype: Dict
    """
    http_request = generate_http_log()
    ip = generate_ip()
    request_duration = generate_request_duration(mode)
    user_agent = generate_user_agent()

    log = {
        "http_request": http_request,
        "ip": ip,
        "response_time": request_duration,
        "user_agent": user_agent
    }
    
    return log

def generate_logs(total_logs):  
    """
    Generate logs with various modes for response time for the requests.
    
    :param total_logs: Total number of logs to generate.
    :returns: A list of generated logs.
    :rtype: List
    """  
    logs = []
    
    for i in range(total_logs):
        log = {}

        if i < 0.1 * total_logs:
            log = generate_log(mode='FAST')
        elif i < 0.3 * total_logs:
            log = generate_log(mode='NORMAL')
        elif i < 0.4 * total_logs:
            log = generate_log(mode='SLOW')
        elif i < 0.7 * total_logs:
            log = generate_log(mode='NORMAL')
        elif i < 0.8 * total_logs:
            log = generate_log(mode='VERY SLOW')
        elif i < 0.9 * total_logs:
            log = generate_log(mode='FAST')
        else:
            log = generate_log(mode='NORMAL')
        
        logs.append(log)
        
    return logs

def get_worst_window(windows):
    """
    Get the window with the most number of errors.
    
    :param windows: List of all the time windows.
    :returns: A list of worst_window, number of 4xx errors and number of 5xx errors in that window.
    :rtype: List
    
    """
    max_failed_reqs = 0
    worst_window = windows[-1]
    errors_4xx = 0
    errors_5xx = 0
    
    for i in range(len(windows) - 1, 0, -1):
        total_4xx_errors_in_window = windows[i][1] - windows[i - 1][1]
        total_5xx_errors_in_window = windows[i][2] - windows[i - 1][2]
        total_failed_reqs_in_window = total_4xx_errors_in_window + total_5xx_errors_in_window
        if total_failed_reqs_in_window > max_failed_reqs:
            worst_window = windows[i][0]
            errors_4xx = total_4xx_errors_in_window
            errors_5xx = total_5xx_errors_in_window
        
    if windows[0][1] + windows[0][2] > max_failed_reqs:
        max_failed_reqs = windows[0][1] + windows[0][2]
        worst_window = windows[0][0]
        errors_4xx = windows[0][1]
        errors_5xx = windows[0][2]
    
    return [worst_window, errors_4xx, errors_5xx]