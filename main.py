from services.generator import Generator
from services.analyzer import Analyzer
from datetime import datetime
import json

def main():
    print('Generating and Aggregating Insights...\n')
    
    # Generator Instance
    gen = Generator(42, "server.log")
    gen.generate_and_save_logs(5000)  
    
    # Analyzer Instance
    azr = Analyzer('access.log')      
    report = azr.analyze_and_create_report()
    
    print('>---------------------------------- ANALYSIS REPORT ----------------------------------------------<\n')
    print(f'Total Requests: {report['total_requests']}\n')
    print(f'Total Successful Requests: {report['total_requests'] - report['total_failed_requests']}\n')
    print(f'Total Failed Requests: {report['total_failed_requests']}\n')
    print(f'Fastest Endpoint: {report['fastest_endpoint_info']}\n')
    print(f'Slowest Endpoint: {report['slowest_endpoint_info']}\n')
    print(f'Busiest Endpoint: {report['busiest_endpoint']}\n')
    worst_window = report['worst_window']
    print(f'''Worst Window: {worst_window[0]}\n
Total Requests: {worst_window[1]}\n
4xx Errors: {worst_window[2]} \n
5xx Errors: {worst_window[3]}\n
Suspicious IPs in this window: {worst_window[4]}\n''')
    suspicious_ips = set(report['suspicious_ips'])
    print(f'Suspicious IPs: \n')
    for ip in suspicious_ips:
        print(f'{ip}\n')
    error_rates_by_endpoints = report['error_rates_by_endpoints']   
    for endpoint in error_rates_by_endpoints:
        print(f"{endpoint} ---> {error_rates_by_endpoints[endpoint]}\n") 
        
if __name__ == "__main__":
    print('------------------------------------------------------------- LOG GENERATOR & ANALYZER --------------------------------------------------------------------\n')
    main()
    print('------------------------------------------------------------- LOG GENERATOR & ANALYZER --------------------------------------------------------------------\n')
    