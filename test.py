def automorphic(n):
    return "Automorphic" if str(pow(n, 2))[-len(str(n)):] == n else "Not!!"

print(automorphic(76))
