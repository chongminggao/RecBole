
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# sns.set_theme(style="white")
# rs = np.random.RandomState(50)

# # Set up the matplotlib figure
# f, axes = plt.subplots(3, 3, figsize=(9, 9), sharex=True, sharey=True)

# # Rotate the starting point around the cubehelix hue circle
# for ax, s in zip(axes.flat, np.linspace(0, 3, 10)):

#     # Create a cubehelix colormap to use with kdeplot
#     cmap = sns.cubehelix_palette(start=s, light=1, as_cmap=True)

#     # Generate and plot a random bivariate dataset
#     x, y = rs.normal(size=(2, 50))
#     sns.kdeplot(
#         x=x, y=y,
#         cmap=cmap, fill=True,
#         clip=(-5, 5), cut=10,
#         thresh=0, levels=15,
#         ax=ax,
#     )
#     ax.set_axis_off()

# ax.set(xlim=(-3.5, 3.5), ylim=(-3.5, 3.5))
# f.subplots_adjust(0, 0, 1, 1, .08, .08)



geyser = sns.load_dataset("geyser")
a = sns.kdeplot(
    data=geyser, x="waiting", y="duration", hue="kind",
    levels=[0.6, 0.8]#, thresh=.3,
)

a.collections[1].get_paths()[0].vertices


# sns.scatterplot(x=geyser.waiting, y=geyser.duration, hue=geyser.kind, s=25, edgecolor="none", legend=False)




# Show the plot
plt.savefig('test0.pdf')
plt.show()
plt.close()
b = 1




import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mu=np.array([1,10,20])
# Let's change this so that the points won't all lie in a plane...
sigma=np.matrix([[20,10,10],
                 [10,25,1],
                 [10,1,50]])

data=np.random.multivariate_normal(mu,sigma,1000)
values = data.T

kde = stats.gaussian_kde(values)

density = kde(values)

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
x, y, z = values
ax.scatter(x, y, z, c=density)
plt.savefig('test3d.pdf')
plt.close()