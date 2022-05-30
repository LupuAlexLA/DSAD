import matplotlib.pyplot as plt


def plot_profile(l, c, profile_l, profile_c, v1, v2, procent_inertie, k1=0, k2=1,
                 titlu="Plot profile"):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontsize=18)
    ax.set_xlabel("a" + str(k1 + 1) + "-" + str(procent_inertie[k1]) + "%", fontsize=12, color='b')
    ax.set_ylabel("a" + str(k2 + 1) + "-" + str(procent_inertie[k2]) + "%", fontsize=12, color='r')
    ax.scatter(l[:, k1], l[:, k2], c='b', label=v1)
    ax.scatter(c[:, k1], c[:, k2], c='r', label=v2)
    for i in range(len(profile_l)):
        ax.text(l[i, k1], l[i, k2], profile_l[i], color='b')
    for i in range(len(profile_c)):
        ax.text(c[i, k1], c[i, k2], profile_c[i], color='r')
    ax.legend()

def show():
    plt.show()

