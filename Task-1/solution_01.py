url = "https://api.github.com/v3"

domain = url.split("//")[1].split("/")[0]
domain = domain.replace("api.","")

print(domain)