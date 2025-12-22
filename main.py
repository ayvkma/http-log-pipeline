from services.generator import Generator
from services.analyzer import Analayzer
from datetime import datetime

def main():
    print('Generating and Analyzing...\n')
    
    # Generator Instance
    gen = Generator(42, "access.log")
    gen.generate_and_save_logs(100)  
    
    # Analyzer Instance
    azr = Analayzer('access.log')      
    report = azr.analyze_and_create_report()
    
    print('HERE IS THE REPORT: \n')
    print(f'Total Requests: {report['total_requests']}\n')
    print(f'Total Successful Requests: {report['total_requests'] - report['total_failed_requests']}\n')
    print(f'Total Failed Requests: {report['total_failed_requests']}\n')
    print(f'Fastest Endpoint: {report['fastest_endpoint_info']}\n')
    print(f'Slowest Endpoint: {report['slowest_endpoint_info']}\n')
    print(f'Busiest Endpoint: {report['busiest_endpoint']}\n')
    worst_window = report['worst_window']
    print(f'Worst Window: {worst_window[0]} {worst_window[1]} 4xx errors {worst_window[2]} 5xx errors\n')
    print(f'Suspicious IPs: {report['suspicious_ips']}\n')
    error_rates_by_endpoints = report['error_rates_by_endpoints']   
    for endpoint in error_rates_by_endpoints:
        print(f"{endpoint} ---> {error_rates_by_endpoints[endpoint]}\n") 
        
if __name__ == "__main__":
    print('------------------------------------------------------------- LOG GENERATOR & ANALYZER --------------------------------------------------------------------\n')
    main()
    print('------------------------------------------------------------- LOG GENERATOR & ANALYZER --------------------------------------------------------------------\n')
    