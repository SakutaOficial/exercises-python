number = int(input("init number: "))
end = int(input("end number: "))

### for loop to multiply
for i in range(end):
    print(f'{number} x {i+1} = {number * (i+1)}')

