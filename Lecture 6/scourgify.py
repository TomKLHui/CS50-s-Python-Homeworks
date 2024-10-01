import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    students = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2],"w") as file:
        writer= csv.DictWriter(file, fieldnames=["first","last","house"])
        writer.writeheader()
        for student in students:
            writer.writerow({"first":student["name"].split(",")[1].lstrip(),
                            "last":student["name"].split(",")[0],
                            "house":student["house"]})

if __name__ == "__main__":
    main()
