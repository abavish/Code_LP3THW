def vada_and_pavs(vada_count, pav_count):
    print(f"You have {vada_count} vadas!")
    print(f"You have {pav_count} loafs of pav!")
    print("Get some dry chutney and fried chillies!")
    print("Delicious and spicy.\n")

print("We can just give the function numbers directly:")
vada_and_pavs(10, 2)

print("OR, we can use variables from our script:")
number_of_vadas = 20
pav_loafs = 3

vada_and_pavs(number_of_vadas, pav_loafs)

print("We can even do the math inside too:")
vada_and_pavs(10 + 20, 2 + 3)

print("And we can combine the two, variables and math:")
vada_and_pavs(number_of_vadas + 80, pav_loafs + 7)
