from scipy.stats import linregress

print("{0:.3f}".format(linregress([15, 12,  8,  8,  7,  7,  7,  6, 5,  3],[10, 25, 17, 11, 13, 17, 20, 13, 9, 15]).slope))
