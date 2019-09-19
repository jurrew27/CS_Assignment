import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv('istherecorrelation.csv', delimiter=';')
fig = plt.figure()
plt.plot(data.iloc[:, 0], data.iloc[:, 2])
plt.title('NL Beer consumption [x1000 hectoliter]')
plt.savefig('graph.png')