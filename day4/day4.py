
def valid_doc_part2(doc):
    if not ("byr" in doc and len(doc["byr"]) == 4 and doc["byr"].isnumeric() and 1920 <= int(doc["byr"]) <= 2002):
        return False

    if not ("iyr" in doc and len(doc["iyr"]) == 4 and doc["iyr"].isnumeric() and 2010 <= int(doc["iyr"]) <= 2020):
        return False

    if not ("eyr" in doc and len(doc["eyr"]) == 4 and doc["eyr"].isnumeric() and 2020 <= int(doc["eyr"]) <= 2030):
        return False

    if not ("hgt" in doc and doc["hgt"][-2:] in ["cm", "in"] and doc["hgt"][:-2].isnumeric()
            and ((doc["hgt"][-2:] == "cm" and 150 <= int(doc["hgt"][:-2]) <= 193)
                 or (doc["hgt"][-2:] == "in" and 59 <= int(doc["hgt"][:-2]) <= 76))):
        return False

    if not (
            "hcl" in doc and len(doc["hcl"]) == 7
            and doc["hcl"][0] == "#"
            and all(c in '0123456789abcdef' for c in doc["hcl"][1:])):
        return False

    if not ("ecl" in doc and doc["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return False

    if not ("pid" in doc and len(doc["pid"]) == 9 and doc["pid"].isnumeric()):
        return False

    return True

with open('./input.txt') as file:
    required_fields = [
        "byr",  # (Birth Year)
        "iyr",  # (Issue Year)
        "eyr",  # (Expiration Year)
        "hgt",  # (Height)
        "hcl",  # (Hair Color)
        "ecl",  # (Eye Color)
        "pid",  # (Passport ID)
        # "cid", # (Country ID) # not required for now
    ]

    documents = []
    temp_doc = {}
    for line in file:
        if line == "\n":
            documents.append(temp_doc)
            temp_doc = {}
        else:
            key_values = [pair.split(":") for pair in line.split()]
            for key, value in key_values:
                temp_doc[key] = value

    valid_docs = 0
    for doc in documents:
        if all(required_field in doc for required_field in required_fields):
            valid_docs += 1
    print(f"Part 1: {valid_docs=}")

    valid_docs = 0
    for doc in documents:
        if valid_doc_part2(doc):
            valid_docs += 1
    print(f"Part 2: {valid_docs=}")

