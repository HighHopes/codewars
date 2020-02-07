"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet" """


def domain_name(url):
    return url.replace("http://", "").replace("https://", "").replace("www.", "").split(".")[0]


print(domain_name("http://google.com"))  # "google"
print(domain_name("http://google.co.jp"))  # "google"
print(domain_name("www.xakep.ru"))  # "xakep"
print(domain_name("https://youtube.com"))  # "youtube"