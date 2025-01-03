import matplotlib.pyplot as plt
squares=[1,4,9,16,25]
fig,ax=plt.subplots()
ax.plot(squares,linewidth=3)
ax.set_title("neberr",fontsize=14)
ax.set_xlabel("vlalen",fontsize=14)
ax.set_ylabel("square of vlaue",fontsize=14)
ax.tick_params(labelsize=14)
plt.show()