import argparse

a = {}
k = False
parser = argparse.ArgumentParser()
parser.add_argument('integers', metavar='integers', nargs='+', type=str)
args = parser.parse_args()
for i in args.integers:
    k = False
    for j in i:
        if j in a and j is i[0] and j.isdigit(): 
            if not k:
                a[j] += 1
            k = True
        elif j not in a and j is i[0] and j.isdigit():
            if not k:
                a[j] = 1  
            k = True 
        elif j not in a and j.isdigit():
            a[j] = 0

sor = sorted(a.keys())
f = open("result.txt", 'w')
for i in sor:
    print(f.write(' '.join((str(i) + str(sor[i])))))
    print(f.write('\n'))