import itertools
import requests
import string
from concurrent.futures import ThreadPoolExecutor


def check_subdomain(subdomain, domain):
    errors = [500,404]
    url = f"https://{domain}/{subdomain}/"
    response = requests.get(url)
    if response.status_code == 200:
        return(True, url)
    elif response.status_code not in errors:
        return(False, url)
    elif "error" in response.text:
        return (False, url)
    elif "sorry," in response.text:
        return (False, url)
    elif "404" in response.text:
        return (False, url)
    else:
        return (True, url)


def get_subdomains(domain):
    subdomains = []
    errors = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        for i in range(1, 69420):
            subdomain_combinations = itertools.product(string.ascii_lowercase, repeat=i)
            results = executor.map(lambda c: check_subdomain(''.join(c), domain), subdomain_combinations)
            for success, subdomain_url in results:
                if success:
                    hakrawlerurl = f"echo {subdomain_url} | hakrawler -subs -d 10 -t 10"
                    print(f"Success! {hakrawlerurl}, {subdomain_url}")
                    subdomains.append(subdomain_url)
                    errors = []

                else:
                    errors.append(subdomain_url)
                    if len(errors) >= 12:
                        print(f"Err: {' '.join(errors)}")
                        '''
                        : {' '.join(errors)}
                        ")
                        '''
                        errors = []

    if errors:
        print(f"Errors: {' '.join(errors)}")

    return subdomains


def main():
    domain = input("Enter a domain: ")
    hakrawlerurl = f"echo https://{domain} | hakrawler -subs -d 10 -t 10"
    print(hakrawlerurl)
    subdomains = get_subdomains(domain)
    print("Subdomains:")
    print(*subdomains, sep='\n')


if __name__ == "__main__":
    main()
