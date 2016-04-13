w1_counter = 0
w2_counter = 0

while w1_counter + w2_counter < 102:
    w1_counter += 2
    w2_counter += 0.005

print("Walker 1 and Walker 2 met each other {} miles outside of London and {} miles outside of Leichester.".format(w2_counter, w1_counter))