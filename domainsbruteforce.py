import dns.resolver
import sys

def domainbruteforce(serverip, wordlist):
    ip_splitted = serverip.split('.')
    with open(wordlist, encoding='utf-8') as wordlist_loaded:
        for word in wordlist:
            try:
                try_domain = dns.resolver.resolve(serverip[0].replace(word), "A")
                print(f"domain: {serverip[0].replace(word)} exists")
            except (dns.reslover.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
                pass

domainbruteforce(sys.argv[1], sys.argv[2])