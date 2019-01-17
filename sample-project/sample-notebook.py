#%%
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib as mpl


# x = np.linspace(0, 20, 100)
# plt.plot(x, np.sin(x))

fig, plot = plt.subplots()

nums = np.random.randint(0, 10, 100)
plot.hist(nums, range=(0,10), align='left', rwidth=0.25)
plot.set_title('Frequency of Numbers')
plot.set_xlabel('Number')
plot.set_xticks(range(10))
plot.set_ylabel('Frequency')
plot.set_yticks(range(20))
plot.get_yaxis().grid()

plt.show() 