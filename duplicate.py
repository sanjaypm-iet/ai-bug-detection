def find_duplicate_lines(code):
    seen = set()
    duplicates = set()

    for line in code:
        if line in seen:
            duplicates.add(line)
        else:
            seen.add(line)

    return list(duplicates)

code = [
    "int a = 10;",
    "int b = 20;",
    "int a = 10;",
    "print(a);",
    "print(a);"
]

print(find_duplicate_lines(code))