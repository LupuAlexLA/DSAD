import matplotlib.pyplot as plt
import seaborn as sb

def scatter2d(t, var1, var2,tg,varg1,varg2,y,clase,titlu="Plot axe discriminante", aspect=1):
    fig = plt.figure(figsize=(13, 8))
    assert isinstance(fig, plt.Figure)
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel(var1+"/"+varg1, fontdict={"fontsize": 12, "color": "b"})
    ax.set_ylabel(var2+"/"+varg2, fontdict={"fontsize": 12, "color": "b"})
    ax.set_aspect(aspect)
    sb.scatterplot(x = t[var1],y=t[var2],hue=y,hue_order=clase,ax=ax)
    sb.scatterplot(x = tg[varg1],y = tg[varg2],hue = clase,ax=ax,legend=False,
                   marker = "s", s = 100)

def show():
    plt.show()

