import dns.resolver

a = dns.resolver.query("www.hzau.edu.cn", "A")
ip = a.response.answer[0].to_text().split(" ")[-1]
print("华中农业大学主页的IP地址：" + ip)
