import matplotlib.pyplot as plt
import numpy as np

def my_pairplot(X,y, title):
    plt.figure(figsize=(10, 10))

    n_feats = np.minimum(5, X.shape[1])
    for i in range(n_feats):
        for j in range(n_feats):
            ax = plt.subplot(n_feats, n_feats, n_feats*(i)+ j+1)

            if j==0:
                ax.set_ylabel(f"Feature {i}")

            if i==n_feats-1:
                ax.set_xlabel(f"Feature {j}")

            if i==j:
                plt.hist(X[y==0,j], color='y', alpha=0.5, edgecolor='k', density=True)
                plt.hist(X[y==1,j], color='b', alpha=0.5, edgecolor='k', density=True)
            
            else:
                plt.scatter(X[:,i], X[:,j], c=y)

    plt.suptitle(title)
    plt.tight_layout()
    return None


