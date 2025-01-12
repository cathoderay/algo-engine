import matplotlib.pyplot as plt
import matplotlib.animation as animation 


class View:
    def __init__(self, name, events, width, height):
        self.name = name
        self.events = events
        self.width = width
        self.height = height
    
    def animate(self, interval=100):
        n = len(self.events)
        artists = []
        fig, ax = plt.subplots()
        fig.set_figwidth(self.width)
        fig.set_figheight(self.height)
        for i in range(n):
            state = self.events[i].payload["state"]
            n = len(state)
            colors = ["tab:blue"]*n
            name = self.events[i].payload["name"]
            if name == "compare":
                a, b = self.events[i].payload["values"]
                colors[a] = colors[b] = "tab:purple"
            elif name == "swap":
                a, b = self.events[i].payload["values"]
                colors[a] = colors[b] = "tab:green"
            container = ax.bar(list(range(n)), state, color=colors)
            artists.append(container)
        
        ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=interval, repeat=False)
        swaps = self.events[-1].payload["swaps"]
        comparisons = self.events[-1].payload["comparisons"]
        plt.title(f"{self.name} - ( swaps: {swaps} | comparisons: {comparisons} )")
        plt.show()


if __name__ == "__main__":
    # Example of usage

    import random
    from engine import Engine

    number_of_swaps = lambda events: len([event for event in events if event.payload["name"] == "swap"])
    number_of_comparisons = lambda events: len([event for event in events if event.payload["name"] == "compare"])
    
    engine = Engine()
    n = 30 # use small n because matplotlib is slow 
    speed = 10
    width = 10
    height = 8
    inp = [random.randint(1, 200) for _ in range(n)]

    engine.bubble_sort(inp[:])
    events = engine.get_events()
    swaps = number_of_swaps(events) 
    comparisons = number_of_comparisons(engine.events) 
    print(f"Bubble sort ( number of events: {len(engine.events)} | number of swaps: {swaps} | number of comparisons: {comparisons} )")
    view = View("bubble sort", engine.events, width=width, height=height)
    view.animate(speed)

    engine.selection_sort(inp[:])
    events = engine.get_events()
    swaps = number_of_swaps(events) 
    comparisons = number_of_comparisons(engine.events) 
    print(f"Selection sort ( number of events: {len(engine.events)} | number of swaps: {swaps} | number of comparisons: {comparisons} )")
    view = View("selection sort", engine.events, width=width, height=height)
    view.animate(speed)

    engine.insertion_sort(inp[:])
    events = engine.get_events()
    swaps = number_of_swaps(events) 
    comparisons = number_of_comparisons(engine.events) 
    print(f"Insertion sort ( number of events: {len(engine.events)} | number of swaps: {swaps} | number of comparisons: {comparisons} )")
    view = View("insertion sort", engine.events, width=width, height=height)
    view.animate(speed)

    engine.merge_sort(inp[:])
    events = engine.get_events()
    swaps = number_of_swaps(events) 
    comparisons = number_of_comparisons(engine.events) 
    print(f"Merge sort ( number of events: {len(engine.events)} | number of swaps: {swaps} | number of comparisons: {comparisons} )")
    view = View("merge sort", engine.events, width=width, height=height)
    view.animate(speed)