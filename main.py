import requests
print("REV-IP")
def get_domains(ip_address)   : 
    try                       : 
        ip_resp               = requests.get('https://sonar.omnisint.io/reverse/'+ip_address)
        domain                = ip_resp.text
        clean_list            = domain.replace("]", "")
        clean_list            = clean_list.replace("[", "")
        return clean_list.split(",")
    except                    : 
        print("[-] ERROR IN API")
def domain_list(ip)           : 
    domains                   = get_domains(ip)
    print("=====================================================")
    print("SERVER INFO")
    print("[+] IP:"+ip)
    print("=====================================================")
    for domain in domains     : 
        print("[+] "+domain)
    print("=====================================================")
domain_list('69.167.169.77')
