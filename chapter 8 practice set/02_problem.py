def f_to_c(f):
    return 5*(f-32)/9



f=int(input("Enter temprature in farenhite: "))

celcius=(f_to_c(f))

print(f"farnhite {f} = celcious {celcius:.2f}")