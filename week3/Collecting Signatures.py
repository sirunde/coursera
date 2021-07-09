# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments = sorted(segments, key=lambda x: x.end)
    position = segments[0].end
    points.append(position)
    for s in segments:
        if s.start > position or s.end < position:
            position = s.end
            points.append(position)

    return points


    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    y = zip(data[::2], data[1::2])
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
