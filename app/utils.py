import time

# DEBUG = True
DEBUG = False


class Timer:
    """simple Timer"""

    def __init__(self):
        self.reset()

    @property
    def delta(self):
        return time.monotonic() - self.start

    def reset(self):
        self.start = time.monotonic()


def rgb_to_int(rgbTuple: tuple):
    if 3 == len(rgbTuple):
        acc = 0
        for e in rgbTuple:
            acc *= 256
            acc += e
        return acc
    return 0x0


def debugMessage(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


def fnName(fn):
    return str(fn).split(" ")[1]


def debugAnounce(enable: bool = True):
    def daDec(fn):
        def inner(*args, **kwargs):
            if enable:
                print(f">> {fnName(fn)} {args=} {kwargs=}")
            t = Timer
            r = fn(*args, **kwargs)
            end = t.delta
            if enable:
                print(f"  << {fnName(fn)} : [ {end} ]")
            return r

        return inner

    return daDec


def transpose(lol: list) -> list:
    return [list(r) for r in zip(*lol)]


def rotate(lol: list) -> list:
    return list(reversed(transpose(lol)))


if __name__ == "__main__":
    print(fnName(rotate))
