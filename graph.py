import matplotlib.pyplot as plt 
import pickle

handle = open('data.pickle', 'rb')
data = pickle.load(handle)
print(data)
data = data['dns']
fig1, ax1 = plt.subplots()
labels = [k for k,v in data.items()]
ax1.pie([v for k,v in data.items()],labels=labels)
plt.show()