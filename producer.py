from faker import Faker
from random import choice
from struct import pack

faker = Faker()
preamble = faker.text()[:40].encode()

# FIXME: note that this opens the file in append mode
# so multiple runs will ruin the file format
with open("data.bin", "ab") as f:
    f.write(preamble)
    for i in range(10):
        id = pack(">H", i).decode()
        name = faker.name()[:7]
        grade = choice(["A", "B", "C"])
        record = f"{name}{id}{grade}".encode()
        f.write(record)
    f.close()
