import matplotlib

"""
  это пример не заработал с ходу
  не хочу разбираться
gui_env = [i for i in matplotlib.rcsetup.interactive_bk]
non_gui_backends = matplotlib.rcsetup.non_interactive_bk
print ("Non Gui backends are:", non_gui_backends)
print ("Gui backends I will test for", gui_env)
for gui in gui_env:
    print ("testing", gui)
    try:
        matplotlib.use(gui,warn=False, force=True)
        from matplotlib import pyplot as plt
        print ("    ",gui, "Is Available")
        plt.plot([1.5,2.0,2.5])
        fig = plt.gcf()
        fig.suptitle(gui)
        plt.show()
        print ("Using ..... ",matplotlib.get_backend())
    except:
        print ("    ",gui, "Not found")
"""

# перебираем возможные backend
gui_env = ['Qt5Agg','GTKAgg','TKAgg','WXAgg']
for gui in gui_env:
    try:
        print ("testing", gui)
        matplotlib.use(gui,warn=False, force=True)
        from matplotlib import pyplot as plt
        break
    except:
        continue
    else:
        print("Not found backend for GUI. Terminate program ")
        exit(1)
print ("Using:",matplotlib.get_backend())


class PlotInTread():
    pass
