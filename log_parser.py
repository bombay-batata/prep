import sys
from collections import Counter


def analyze_logs (file_path):
    sql_injections_attempts = []
    ip_counter = Counter()
    sql_keywords = ["SELECT", "UNION","INSERT", "DELETE"]
    
    
    with open(file_path, 'r') as file:
        for line in file:
             ip = line.split()[0]
             ip_counter[ip] +=1
            
            
        if any(keyword in line for keyword in sql_keywords):
            sql_injections_attempts.append(line.strip())
            print("SQL Injection Attempts")
        for attempts in sql_injections_attempts:
            print (attempts)
        
        # Top 3 Most common IP addresses 
        print(" Top 3 Most Common IP Addresses")                
        for ip, count in ip_counter.most_common(3):
            print(f"IP: {ip}, Count: {count}")        
            
if __name__ == "__main__":
    analyze_logs("webserver_logs.txt")
    