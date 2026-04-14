import dns.resolver


dns_cache = []


def get_ip(domain):
    for item in dns_cache:
        if item[0] == domain:
            return item[1]
    answer = dns.resolver.resolve(domain, "A")
    ip = answer.response.answer[0].to_text().split(" ")[-1]
    dns_cache.append([domain, ip])
    return ip


print(get_ip("www.hzau.edu.cn"))
print(dns_cache)
