import dns.resolver
import sys
from rich.progress import Progress
from rich.console import Console

console = Console()

results = []

def domainbruteforce(serverip, wordlist):
    ip_splitted = serverip.split('.')
    with open(wordlist, encoding='utf-8') as wordlist_loaded:
        wordlist_readed = wordlist_loaded.readlines()
        with Progress() as progress:
            task = progress.add_task("[red]Brute forcing...", total=len(wordlist_readed))
        for word in wordlist_readed:
            try:
                try_domain = dns.resolver.resolve(serverip[0].replace(word), "A")
                print(f"domain: {serverip[0].replace(word)} exists")
            except (dns.reslover.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
                pass

domainbruteforce(sys.argv[1], sys.argv[2])