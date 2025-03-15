# 使用python读写csv文件
import csv


def write_csv():
    with open("source.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(("number", "number plus 2", "number times 2"))
        for i in range(100):
            writer.writerow((i, i + 2, i * 2))


def read_csv():
    with open("source.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


if __name__ == "__main__":
    # write_csv()
    read_csv()
