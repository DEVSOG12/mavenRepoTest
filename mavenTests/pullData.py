from importss import *

def run():
    # Check if raw data exists
    if os.path.exists("data/raw/maven_sample_5000Fixed.csv"):
        file = csv.reader(open("data/raw/maven_sample_5000Fixed.csv", "r"))
        data = []
        for row in file:
            data.append(row)
        # Clean up data
        # 3 and 9 column are the repo name and url
        # data = [[data[i][3], data[i][10]] for i in range(1, len(data))]
        print(len(data))
        return 1
    else:
        return False


def runFixed():
    # Check if raw data exists
    if os.path.exists("data/raw/maven_sample_5000Fixed.csv"):
        file = csv.reader(open("data/raw/maven_sample_5000Fixed.csv", "r"))
        data = []
        for row in file:
            data.append(row)

        data = data[1:]
        # Clean up data
        # 3 and 9 column are the repo name and url
        # data = [[data[i][3], data[i][10]] for i in range(1, len(data))]
        return data
    else:
        return False


if __name__ == "__main__":
    datas = run()
    print(datas)