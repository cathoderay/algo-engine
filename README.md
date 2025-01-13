# algo-engine
Engine to study and visualize algorithms. No AI was used in this project.

## running engine
In order to run an algorithm, you just need to instantiate an engine 
and call the algorithm you want to study.

Below you can see an example for the insertion sort.
  ```
    import pprint
    from engine import Engine

    engine = Engine()
    input = [4, 2, 3, 1]
    engine.insertion_sort(input)
    pprint.pprint(engine.get_events())
  ```
  ```
[{'name': 'initial', 'state': (4, 2, 3, 1), 'indices': (None, None), 'swaps': 0, 'comparisons': 0},
 {'name': 'compare', 'state': (4, 2, 3, 1), 'indices': (1, 0), 'swaps': 0, 'comparisons': 1},
 {'name': 'swap', 'state': (2, 4, 3, 1), 'indices': (1, 0), 'swaps': 1, 'comparisons': 1},
 {'name': 'compare', 'state': (2, 4, 3, 1), 'indices': (2, 1), 'swaps': 1, 'comparisons': 2},
 {'name': 'swap', 'state': (2, 3, 4, 1), 'indices': (2, 1), 'swaps': 2, 'comparisons': 2},
 {'name': 'compare', 'state': (2, 3, 4, 1), 'indices': (1, 0), 'swaps': 2, 'comparisons': 3},
 {'name': 'compare', 'state': (2, 3, 4, 1), 'indices': (3, 2), 'swaps': 2, 'comparisons': 4},
 {'name': 'swap', 'state': (2, 3, 1, 4), 'indices': (3, 2), 'swaps': 3, 'comparisons': 4},
 {'name': 'compare', 'state': (2, 3, 1, 4), 'indices': (2, 1), 'swaps': 3, 'comparisons': 5},
 {'name': 'swap', 'state': (2, 1, 3, 4), 'indices': (2, 1), 'swaps': 4, 'comparisons': 5},
 {'name': 'compare', 'state': (2, 1, 3, 4), 'indices': (1, 0), 'swaps': 4, 'comparisons': 6},
 {'name': 'swap', 'state': (1, 2, 3, 4), 'indices': (1, 0), 'swaps': 5, 'comparisons': 6},
 {'name': 'final', 'state': (1, 2, 3, 4), 'indices': (None, None), 'swaps': 5, 'comparisons': 6}]
  ```

## view
In order to visualize a step-by-step of the algorithm, you can pass the events
generated by the engine into a view and animate it!

Below you can see an example on how to do that.

```
  from engine import Engine
  from view import View

  engine = Engine()
  input = [5, 6, 8, 7, 10, 4, 9, 3, 2, 1]
  engine.insertion_sort(input)

  view = View("insertion sort", engine.events, width=6, height=4)
  view.animate(delay=200, save=True)
 ```
  ![insertion sort animation example](https://github.com/cathoderay/algo-engine/blob/main/media/insertion_sort_example.gif)


## tests
 Running tests:
   ```
     $ python3 -m pytest test.py
   ```
