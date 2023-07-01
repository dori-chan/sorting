import matplotlib.pyplot as plt


def make_plot(times, name_array):
    plt.figure(figsize=(7, 4), dpi=100)
    ox_names = [time for time in times]
    ox_len = range(len(times))
    plt.plot(range(len(times)), times.values(), color='c', alpha=1.0,
             marker='o', ms=3, mfc='b', mec='b', label=name_array)
    plt.title(name_array, weight='bold')
    plt.xticks(ox_len, ox_names, rotation=40,
               horizontalalignment='right', fontsize=7)
    plt.tight_layout()
    plt.show()
