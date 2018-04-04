class RainData:
    def __init__(self, file_path):
        self.name = self.load(file_path)
        self.data = {}

    def load(self, file_path):
        with open(self.name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        start = None
        for i in enumerate(lines):
            if i[1][0] == '-':
                start = lines[i[0]+1]
                break
        for line in lines[start:]:
            tmp = line.split()
            self.data[tmp[0]] = tmp[2:]
            print(line)
        return lines[0]


if __name__ == '__main__':
    hayden = RainData('rain_data.txt')
print(hayden.name)
print(hayden.data)