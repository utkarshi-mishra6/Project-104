import csv
with open("data.csv" , newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float (n_num))

n = len(new_data)

new_data.sort()

if n % 2 == 0:
    m1 = float(new_data[n//2])
    m2 = float(new_data[n//2-1])
    m = (m1+m2)/2

else:
    m = new_data[n//2]

print(n)
print("Median is:" + str(m))