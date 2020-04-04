import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties
import numpy as np


def create_font_setting(sizes=(14, 12, 8)):
    """
    Create font axis for matplotlib and seaborn plots.
    Returns:
        (FontProperties) for title, for axis, and for ticks
    """
    title_font = FontProperties(family="Arial", size=sizes[0],
                                weight="semibold")
    axis_font = FontProperties(family="Arial", size=sizes[1])
    ticks_font = FontProperties(family="Arial", size=sizes[2])

    return title_font, axis_font, ticks_font


def corr_plot(ax, corr, labels, sub=False, plot_title="", cmap="coolwarm",
              triangle=False, upper=True, font_size=(14, 12, 8), annot_size=20,
              decimals=2):
    """
    Plot a correlation matrix.

    Inputs:
        - ax: (Axes) instance to draw the plot on
        - corr: (2D-array) the correlation matrix
        - labels: ([str]) names of the variables for plotting
        - sub: (Bool) whether the plot is a subplot, control for the title font
        - plot_title: (string) title of the plot
        - cmap: (string) color map for the heat map
        - triangle: (Bool) whether to plot the upper or lower part of the matrix
            as it's symmetric
        - upper: (Bool) if only plot half of the plot, whether it's upper
        - font_size: (int, int, int) font size for title, axis, and tick
        - annot_size: (int) font size for the correlation number annotations
        - decimals: (int) round the correlation coefficients to
    """
    TITLE, AXIS, TICKS = create_font_setting(font_size)
    default = {'ax': ax,
               'cmap': cmap, 'cbar_kws': {"shrink": .5},
               'vmax': 1, 'vmin': -1, 'center': 0,
               'square': True, 'linewidths': 0.5}
    if annot_size != 0:
        default['annot'] = True
        default['annot_kws'] = {"size": annot_size}
    corr = corr.round(decimals)

    if triangle:
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[[np.triu_indices_from, np.tril_indices_from][int(upper)](
            mask)] = True
        sns.heatmap(corr, mask=mask, **default)
    else:
        sns.heatmap(corr, **default)

    # Make tick labels to
    ax.set_title(plot_title, fontproperties=[TITLE, AXIS][int(sub)])
    ax.set_xticklabels(labels, fontproperties=AXIS, rotation='vertical')
    ax.set_yticklabels(labels, fontproperties=AXIS, rotation='horizontal')
    ax.tick_params(axis='both', length=0.0)

    if upper:
        x_hide, y_hide = 0, -1
        ax.xaxis.tick_top()
    else:
        x_hide, y_hide = -1, 0
    plt.setp(ax.get_xticklabels()[x_hide], visible=False)
    plt.setp(ax.get_yticklabels()[y_hide], visible=False)

    cbar = ax.collections[0].colorbar
    cbar.set_ticks([-1.0, -0.8, -0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6, 0.8, 1.0])
    cbar.ax.set_yticklabels(cbar.ax.get_yticks(), fontproperties=TICKS)
    cbar.ax.set_title('Correlation', fontproperties=AXIS)


if __name__ == "__main__":
    pass
