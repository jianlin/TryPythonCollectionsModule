heading = "id     name    age    phoneNumber"
data = "1  mike  18  123-456-7890"

arrHeadings = heading.split()
arrData = data.split()

print(arrHeadings)
print(arrData)

print(dict(zip(arrHeadings, arrData)))
