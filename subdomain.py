import socket


def wordlist(filepath):
    with open(filepath,'r') as f:
        for i in f:
            word=i.strip().lower()
            yield word


def check_domain(subdomain):
    try:
        ip=socket.gethostbyname(subdomain)
        return ip
    except socket.gaierror:
        return None
    except socket.timeout:
        return None


def main():
    domain=input('Enter the target domain name in format like google.com:')
    print('Targeted domain is : ',domain)
    socket.setdefaulttimeout(3)
    for word in wordlist('n0kovo_subdomains_huge.txt'):
        subdomain=word+'.'+domain
        ip=check_domain(subdomain)
        if ip is not None:
            print(subdomain,' -> ',ip)



if __name__ =="__main__":
    main()