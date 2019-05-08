import os
cnts = 0
sums = 0
avgs = []
while True:
    with open('{0}/fibo-clock.log'.format(os.path.expanduser('~/Desktop/Git/FiboClock/logs')), 'r') as f:
        lines = f.readlines()
        if not lines:
            break
        for line in lines:
            nl = line.split('-')
            pl = nl[1:]
            sums += int(pl[0])
            cnts += 1
            avgs.append(sums/cnts)
            print('LIVE Clock AVG #{1}: {0} -> {2}'.format(avgs[-1], cnts, line))
        print(avgs)
        print('LIVE Clock BIG-AVG: {0}'.format(sum(avgs) / avgs.__len__()))
    f.close()
    break
