"""
    Author: Ronald Andreu Kaiser
    Date: Jan 11th, 2025
    Last updated: Jan 13th, 2025

    Description: This is an engine to study algorithms.

    1. The idea is to instantiate an engine:
        engine = Engine()
    2. call your algorithm:
        engine.insertion_sort([5, 3, 2, 1])
    3. and then check out the list of state changes:
        engine.get_events()
    
    The list of events can be used to plot and visualize
    a step-by-step states change the algorithm performs.

    See an example in view.py
    
"""


from math import inf
from random import randint

import constants


class Event:
    def __init__(self, payload):
        self.payload = payload
    
    def __repr__(self):
        return str(self.payload)


class Engine:
    def __init__(self):
        self.events = []
        self.total_swaps = 0
        self.total_comparisons = 0

    def __add_event(self, event):
        self.events.append(Event(event))

    def get_last_event(self):
        return self.events[-1]
    
    def get_events(self):
        return self.events
    
    def cleanup_events(self):
        self.events = []

    def initialize(self):
        self.cleanup_events()
        self.total_swaps = 0
        self.total_comparisons = 0 
    
    def add_event(self, name, l, a=None, b=None):
        self.__add_event({
            constants.NAME: name,
            constants.STATE: tuple(l),
            constants.INDICES: (a, b),
            constants.SWAPS: self.total_swaps,
            constants.COMPARISONS: self.total_comparisons
        })
    
    def add_swap(self, l, a, b):
        self.total_swaps += 1
        self.add_event(constants.SWAP, l, a, b)
    
    def add_comparison(self, l, a, b):
        self.total_comparisons += 1
        self.add_event(constants.COMPARE, l, a, b)
    
    def start(self, l):
        self.initialize()
        self.add_event(constants.INITIAL, l)
    
    def finish(self, l):
        self.add_event(constants.FINAL, l)

    def bubble_sort(self, a):
        self.start(a)
        n = len(a)
        for i in range(n):
            for j in range(n-i-1):
                self.add_comparison(a, j, j + 1)
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    self.add_swap(a, j, j + 1)
        self.finish(a)
    
    def selection_sort(self, a):
        self.start(a)
        n = len(a)
        for i in range(n):
            k = i
            for j in range(i + 1, n):
                self.add_comparison(a, j, k)
                if a[j] < a[k]:
                    k = j
            a[k], a[i] = a[i], a[k]
            self.add_swap(a, i, k)
        self.finish(a)
    
    def insertion_sort(self, a):
        self.start(a)
        n = len(a)
        for i in range(n):
            for j in range(i, 0, -1):
                self.add_comparison(a, j, j - 1)
                if a[j] < a[j - 1]:               
                    a[j], a[j-1] = a[j-1], a[j]
                    self.add_swap(a, j, j - 1)
                else:
                    break
        self.finish(a)
    
    def merge_sort(self, a):
        def combine(s, m, e):
            l = a[s:m+1] + [inf]
            r = a[m+1:e+1] + [inf]
            i = j = 0
            for k in range(s, e+1):
                self.add_comparison(a, s+i, min(m+1+j, e))
                if l[i] <= r[j]:
                    a[k] = l[i] 
                    self.add_swap(a, k, s+i)
                    i += 1
                else:
                    a[k] = r[j]
                    self.add_swap(a, k, m+1+j)
                    j += 1
        
        def merge(s, e):
            if s >= e: return

            m = (s + e) // 2
            merge(s, m)
            merge(m + 1, e)
            combine(s, m, e)
        
        self.start(a)
        merge(0, len(a) - 1)
        self.finish(a)

    def quick_sort(self, a):
        def partition(s, e):
            p_i = randint(s, e)
            self.add_swap(a, p_i, s)
            a[p_i], a[s] = a[s], a[p_i]
            p = a[s]
            i = j = s + 1
            for j in range(s + 1, e + 1):
                self.add_comparison(a, j, s)
                if a[j] < p:
                    self.add_swap(a, i, j)
                    a[i], a[j] = a[j], a[i]
                    i += 1
            self.add_swap(a, s, i-1)
            a[s], a[i-1] = a[i-1], a[s]
            return i - 1

        def quick(s, e):
            if s > e: return

            p = partition(s, e)
            quick(s, p - 1)
            quick(p + 1, e)

        self.start(a)
        quick(0, len(a) - 1)
        self.finish(a)


if __name__ == "__main__":
    # Example of usage

    import random
    import pprint

    engine = Engine()
    inp = [random.randint(0, 100) for _ in range(100)]
    engine.bubble_sort(inp[:])
    pprint.pprint(engine.get_events())

    engine.selection_sort(inp[:])
    pprint.pprint(engine.get_events())

    engine.insertion_sort(inp[:])
    pprint.pprint(engine.get_events())

    engine.merge_sort(inp[:])
    pprint.pprint(engine.get_events())

    engine.quick_sort(inp[:])
    pprint.pprint(engine.get_events())