import csv

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            return row

if __name__ == "__main__":
    file_path = '/home/wolf/files/file.csv'
    read_csv(file_path)