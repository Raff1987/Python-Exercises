# Martin Rafter 5-3-18

with open("data/iris.csv") as f:

  for line in f:

    n = line.split(',')
    print('{0[0]:5} {0[1]:5} {0[2]:5} {0[3]:5}'.format(n))
