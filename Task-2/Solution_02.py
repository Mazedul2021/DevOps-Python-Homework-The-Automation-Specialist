bucket_name = " My Project Backup "

safe_name = bucket_name.strip()
safe_name= safe_name.replace(" ", "-")
safe_name = safe_name.lower()

print(safe_name)