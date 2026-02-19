from collections import defaultdict

log_file = "logs/auth.log"
failed_attempts = defaultdict(int)

threshold = 5

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-1]
            failed_attempts[ip] += 1

print("\n=== Brute Force Detection Report ===\n")

for ip, count in failed_attempts.items():
    if count >= threshold:
        print(f"[ALERT] Possible brute force from {ip} → {count} failed attempts")
