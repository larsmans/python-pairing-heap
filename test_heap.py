from heap import Heap
from nose.tools import assert_equal
import random


def test_basic():
    h = Heap()
    assert_equal(len(h), 0)

    for x in reversed(range(10)):
        h.push(x)
    assert_equal(len(h), 10)

    x = h.pop()
    assert_equal(x, 0)
    assert_equal(len(h), 9)
    assert_equal(h.top, 1)


def test_merge():
    rng = random.Random(42)

    data1 = [rng.randint(0, 99) for i in range(1000)]
    data2 = range(200)

    heap1 = Heap(data1)
    heap2 = Heap(data2)

    assert_equal(len(heap1), 1000)
    assert_equal(len(heap2), 200)

    heap1 += heap2
    assert_equal(len(heap1), 1200)
    assert_equal(len(heap2), 0)


def test_sort():
    rng = random.Random(42)

    data = [rng.randint(0, 999) for i in range(2000)]

    heap = Heap(data)
    assert_equal(len(heap), 2000)

    heapsorted = iter(heap.pop_safe, None)
    assert_equal(list(heapsorted), sorted(data))
