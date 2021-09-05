def height(v):
    if v is None:
        return -1
    return v.height


class Node:
    def __init__(self, element):
        self.element = element  # dataen som blir lagret i noden
        self.left = None  # venstre barn av v (noden)
        self.right = None  # hoyre varn av v (noden)
        # høyden til v (noden)... altså avstanden fra den noden til den dypeste løvnoden
        self.height = 0


nodeY = Node("Y")  # Dette er da start noden
