import hashlib
target_hash = input("Enter target SHA-256 hash: ")
with open("wordlist.txt", "r") as file:
    for word in file:
        word = word.strip()
        hashed_word = hashlib.sha256(word.encode()).hexdigest()
        if hashed_word == target_hash:
            print(f"Password found: {word}")
            break
    else:
        print("Password not found in wordlist.")
