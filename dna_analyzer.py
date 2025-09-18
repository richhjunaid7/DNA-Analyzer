#DNA Analyzer

valid_bases = ["A","T","G","C"]


valid = False
while valid == False:
    seq = input("Enter the DNA sequence: ").upper()
    valid = True

    for each_base in seq:
        if each_base not in valid_bases:
            print(f"Invalid base found: {each_base}")
            valid = False
            break


a = seq.count("A")
t = seq.count("T")
g = seq.count("G")
c = seq.count("C")

melt_temp = 2*(a + t) + 4*(g + c)

at_content = ((a+t)/(a + t + g + c))*100
gc_content = ((g + c)/(a + t + g + c))*100

print("Base Composition Report:-")
print(f"Adenine:{a}")
print(f"Thymine:{t}")
print(f"Guanine:{g}")
print(f"Cytosine:{c}")
print(f"Total AT present in the sequence:{a+t}")
print(f"Total GC present in the sequence:{g+c}")

print(f"Melting Temperature of a DNA:{melt_temp}"+chr(176)+"C")

print("Content Report:-")
print(f"GC content of a sequence is:{gc_content:.2f}%")
print(f"AT content of a sequence is:{at_content:.2f}%")