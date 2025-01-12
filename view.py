import constants

import matplotlib.pyplot as plt
import matplotlib.animation as animation 



class View:
    def __init__(self, name, events, width, height):
        self.name = name
        self.events = events
        self.width = width
        self.height = height
    
    def print_results(self):
        print(f"""
           {self.name}
            number of events: {len(self.events)}
            number of swaps: {self.events[-1].payload[constants.SWAPS]}
            number of comparisons: {self.events[-1].payload[constants.COMPARISONS]}
        """)

    def animate(self, interval=100):
        n = len(self.events)
        artists = []
        fig, ax = plt.subplots()
        fig.set_figwidth(self.width)
        fig.set_figheight(self.height)
        for i in range(n):
            state = self.events[i].payload[constants.STATE]
            n = len(state)
            colors = ["tab:blue"] * n
            name = self.events[i].payload[constants.NAME]
            if name == constants.COMPARE:
                a, b = self.events[i].payload[constants.INDICES]
                colors[a] = colors[b] = "tab:purple"
            elif name == constants.SWAP:
                a, b = self.events[i].payload[constants.INDICES]
                colors[a] = colors[b] = "tab:green"
            container = ax.bar(list(range(n)), state, color=colors)
            artists.append(container)
        
        ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=interval, repeat=False)
        swaps = self.events[-1].payload[constants.SWAPS]
        comparisons = self.events[-1].payload[constants.COMPARISONS]
        plt.title(f"{self.name} - ( swaps: {swaps} | comparisons: {comparisons} )")
        plt.show()


if __name__ == "__main__":
    # Example of usage

    import random
    from engine import Engine

    engine = Engine()
    n = 10 # use small n because matplotlib is slow
    speed = 10
    width = 10
    height = 8
    inp = [random.randint(1, 200) for _ in range(n)]

    engine.bubble_sort(inp[:])
    events = engine.get_events()
    view = View("bubble sort", engine.events, width=width, height=height)
    view.print_results()
    view.animate(speed)

    engine.selection_sort(inp[:])
    events = engine.get_events()
    view = View("selection sort", engine.events, width=width, height=height)
    view.print_results()
    view.animate(speed)

    engine.insertion_sort(inp[:])
    events = engine.get_events()
    view = View("insertion sort", engine.events, width=width, height=height)
    view.print_results()
    view.animate(speed)

    engine.merge_sort(inp[:])
    events = engine.get_events()
    view = View("merge sort", engine.events, width=width, height=height)
    view.print_results()
    view.animate(speed)