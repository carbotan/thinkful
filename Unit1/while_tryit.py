w1_counter = 0
w2_counter = 0

while w1_counter + w2_counter != 102:
    print("Walker 1: I have walked {} miles but I haven't seen Walker 2 yet.".format(w1_counter))
    print("Walker 2: I have walked {} miles but I haven't seen Walker 1 yet.".format(w2_counter))
    w1_counter += 2
    w2_counter += 1
else: 
    print("Walker 1 and Walker 2 met each other {} miles outside of London and {} miles outside of Leichester.".format(w2_counter, w1_counter))