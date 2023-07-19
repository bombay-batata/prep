import re
import sys

def parse_cloudflare_warp_dns_log(log_line):
  """Parses a Cloudflare Warp DNS log line and returns a dictionary of the parsed data.

  Args:
    log_line: The Cloudflare Warp DNS log line to be parsed.

  Returns:
    A dictionary of the parsed data.
  """

  match = re.match(r"(?P<timestamp>.+) (?P<client_ip>\d+) (?P<resolver_ip>\d+) (?P<domain>\S+) (?P<query_type>\S+) (?P<response_code>\d+)", log_line)
  if match:
    return {
        "timestamp": match.group("timestamp"),
        "client_ip": match.group("client_ip"),
        "resolver_ip": match.group("resolver_ip"),
        "domain": match.group("domain"),
        "query_type": match.group("query_type"),
        "response_code": match.group("response_code"),
    }
  else:
    return None

def flag_suspicious_domains(dns_logs):
  """Flags suspicious domains in a list of Cloudflare Warp DNS logs.

  Args:
    dns_logs: A list of Cloudflare Warp DNS logs.

  Returns:
    A list of suspicious domains.
  """

  suspicious_domains = []
  for log in dns_logs:
    parsed_log = parse_cloudflare_warp_dns_log(log)
    if parsed_log and parsed_log["response_code"] == "NXDOMAIN":
      suspicious_domains.append(parsed_log["domain"])

  return suspicious_domains

def main():
  """The main function."""

  if len(sys.argv) != 2:
    print("Usage: python cloudflare_warp_dns_log_parser.py <path_to_dns_logs>")
    sys.exit(1)

  path_to_dns_logs = sys.argv[1]
  with open(path_to_dns_logs, "r") as f:
    dns_logs = f.readlines()

  suspicious_domains = flag_suspicious_domains(dns_logs)
  print(suspicious_domains)

if __name__ == "__main__":
  main()

'''
sample cloudflare warp dns logs looks like this 

dns_logs = [
      "2023-07-18T23:29:59.536Z 127.0.0.1 warp-resolver.cloudflare-dns.com 1.2.3.4 A 0",
      "2023-07-18T23:30:00.536Z 127.0.0.1 warp-resolver.cloudflare-dns.com google.com A 0",
      "2023-07-18T23:30:01.536Z 127.0.0.1 warp-resolver.cloudflare-dns.com suspicious.com NXDOMAIN 0",
  ]

The timestamp is in the format YYYY-MM-DDTHH:MM:SS.sssZ. The IP address of the client is the IP address of the device that made the DNS query. 
The name of the Cloudflare Warp resolver is the IP address of the Cloudflare Warp server that responded to the query. 
The domain name that was queried is the domain name that the client was trying to resolve. 
The type of DNS query that was made is A, which means that the client was requesting the IPv4 address for the domain name. 
The response code from the resolver is 0, which means that the query was successful.
NXDOMAIN in Cloudflare Warp DNS logs stands for "Non-Existent Domain". It is a response code that is returned by a DNS resolver when the domain name that is being queried does not exist
You can use a tool like VirusTotal to scan the domains that are returning NXDOMAIN response codes. This will help you to determine if the domains are malicious
'''

