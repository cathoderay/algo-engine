import pytest
import unittest

from engine import Event, Engine


class EngineTest(unittest.TestCase):
    def test_add_event(self):
        event = Event(payload={"test": 42})
        self.assertEqual(42, event.payload["test"])

    def test_generate_event(self):
        engine = Engine()
        engine.add_event(name="swap", l=[1, 2, 3], a=0, b=1)
        event = engine.get_last_event()
        self.assertEqual(event.payload["name"], "swap")
    
    def test_bubble_sort(self):
        engine = Engine()
        inp = [5, 3, 2, 1]
        engine.bubble_sort(inp)
        self.assertEqual([1, 2, 3, 5], inp)
        events = engine.get_events()
        self.assertEqual(1, len([event for event in events if event.payload["name"] == "initial"]))
        self.assertEqual(6, len([event for event in events if event.payload["name"] == "compare"]))
        self.assertEqual(6, len([event for event in events if event.payload["name"] == "swap"]))
        self.assertEqual(1, len([event for event in events if event.payload["name"] == "final"]))
        self.assertEqual(tuple(sorted(inp)), engine.get_last_event().payload["state"])
    
    def test_cleanup_events(self):
        engine = Engine()
        engine.add_event(name="swap", l=[1, 2, 3], a=0, b=1)
        events = engine.get_events()
        self.assertEqual(1, len(events))
        engine.cleanup_events()
        events = engine.get_events()
        self.assertEqual(0, len(events))
    
    def test_selection_sort(self):
        engine = Engine()
        inp = [5, 3, 2, 1]
        engine.selection_sort(inp)
        self.assertEqual([1, 2, 3, 5], inp)
        events = engine.get_events()
        self.assertEqual(1, len([event for event in events if event.payload["name"] == "initial"]))
        self.assertEqual(6, len([event for event in events if event.payload["name"] == "compare"]))
        self.assertEqual(4, len([event for event in events if event.payload["name"] == "swap"]))
        self.assertEqual(1, len([event for event in events if event.payload["name"] == "final"]))
        self.assertEqual(tuple(sorted(inp)), engine.get_last_event().payload["state"])
    
    def test_insertion_sort(self):
        engine = Engine()
        inp = [5, 3, 2, 1]
        engine.insertion_sort(inp)
        self.assertEqual([1, 2, 3, 5], inp)
        events = engine.get_events() 
        self.assertEqual(1, len([event for event in events if event.payload["name"] == "initial"]))
        self.assertEqual(6, len([event for event in events if event.payload["name"] == "compare"]))
        self.assertEqual(6, len([event for event in events if event.payload["name"] == "swap"]))
        self.assertEqual(1, len([event for event in events if event.payload["name"] == "final"]))
        self.assertEqual(tuple(sorted(inp)), engine.get_last_event().payload["state"])
    
    def test_merge_sort(self):
        engine = Engine()
        inp = [5, 3, 2, 1]
        engine.merge_sort(inp)
        self.assertEqual([1, 2, 3, 5], inp)
        events = engine.get_events() 
        self.assertEqual(1, len([event for event in events if event.payload["name"] == "initial"]))
        self.assertEqual(8, len([event for event in events if event.payload["name"] == "compare"]))
        self.assertEqual(8, len([event for event in events if event.payload["name"] == "swap"]))
        self.assertEqual(1, len([event for event in events if event.payload["name"] == "final"]))
        self.assertEqual(tuple(sorted(inp)), engine.get_last_event().payload["state"])