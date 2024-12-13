email = "user@example.com"
extract_domain = lambda email: email.split('@')[1]
result = extract_domain(email)
print(result)