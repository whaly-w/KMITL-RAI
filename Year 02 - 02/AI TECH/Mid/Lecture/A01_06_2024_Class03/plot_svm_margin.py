# Import essential library
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm

# Create 40 dataset using standard normal distribution (SND)
# | .r_ is a method to combine 2 numpy array
# | randn(20, 2) -> 20, 2 is the dimension, random is SND
np.random.seed(0)
X = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]
Y = [0] * 20 + [1] * 20

# Plot the dataset
# | c= Y set the data by a different color
plt.scatter(X[:, 0], X[:, 1], c= Y)
# plt.show()


fignum = 1
for name, penalty in (("unreg", 1), ("reg", 0.05)):
    # Create instance & train the model
    clf = svm.SVC(kernel="linear", C=penalty)
    clf.fit(X, Y)

    # get the separating hyperplane
    # we got the "coef" of the line equaiton (w1x1 + w2x2 + b = 0)
    # | w[0] -> w1 (weight of feature 1)
    # | w[1] -> w2 (weight of feature 2)
    # | i -> b (bias)
    w = clf.coef_[0]
    i = clf.intercept_[0]
    
    # When plotting we use y = mx +c, so we've to transform the line eq. to this form
    # we gonna set y-axis as feature 2 and x-axis as feature 1
    # | w1x1 + w2x2 + b -> w1x + w2y + b = 0
    # Caculate slope: w1x + w2y + b = 0 -> y = (-w1/w2)x - (b/w2)
    # | y = mx + c
    # | a = -w1/w2
    # | c = -b/w2 (clr.intercept_[0])
    m = -w[0] / w[1]
    c = -i / w[1]
    
    # Generate x and y dataset for plotting
    xx = np.linspace(-5, 5)
    yy = m*xx + c

    # Plot the graph
    plt.plot(xx, yy)
    plt.show()



    # plot the parallels to the separating hyperplane that pass through the
    # support vectors (margin away from hyperplane in direction
    # perpendicular to hyperplane). This is sqrt(1+a^2) away vertically in
    # 2-d.
    margin = 1 / np.sqrt(np.sum(clf.coef_**2))
    yy_down = yy - np.sqrt(1 + m**2) * margin
    yy_up = yy + np.sqrt(1 + m**2) * margin

    # Setup the figure
    plt.figure(fignum, figsize=(4, 3))
    # Clear figure
    plt.clf() 
    # Plot data
    plt.plot(xx, yy, "k-")
    plt.plot(xx, yy_down, "k--")
    plt.plot(xx, yy_up, "k--")

    plt.scatter(
        clf.support_vectors_[:, 0],
        clf.support_vectors_[:, 1],
        s=80,
        facecolors="none",
        zorder=10,
        edgecolors="k",
        cmap=plt.get_cmap("RdBu"),
    )
    plt.scatter(
        X[:, 0], X[:, 1], c=Y, zorder=10, cmap=plt.get_cmap("RdBu"), edgecolors="k"
    )

    plt.axis("tight")
    x_min = -4.8
    x_max = 4.2
    y_min = -6
    y_max = 6

    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = clf.decision_function(xy).reshape(XX.shape)

    # Put the result into a contour plot
    plt.contourf(XX, YY, Z, cmap=plt.get_cmap("RdBu"), alpha=0.5, linestyles=["-"])

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.xticks(())
    plt.yticks(())
    fignum = fignum + 1

plt.show()
