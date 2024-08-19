import csv

with open("sample.csv", mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


with open("sample.csv", mode="r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    with open("result.tsv", newline="", mode="w", encoding="utf-8") as write_file:
        writer = csv.writer(write_file, delimiter="\t")
        writer.writerow(["都道府県", "人口密度"])
        for row in reader:
            population_density = float(row[2]) / float(row[3])
            writer.writerow([row[1], int(population_density)])
