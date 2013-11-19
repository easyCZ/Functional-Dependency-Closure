

def closure(elems, fds):
    """
    Find closure for given functional dependencies.
    Args:
        elems <list>            Elements in question for closure
        fds <list of tuples>    Tuples of x -> b in form ([x1,x2,x3], [y1,y2])
    Returns:
        set of elements under closure.
    """
    unused = set(fds)
    closure = set(elems)
    for i in range(0, len(fds)):
        if fds[i % len(fds)][0] in closure:
            unused.remove(fds[i % len(fds)])
            closure.add(fds[i % len(fds)][1])

    return closure