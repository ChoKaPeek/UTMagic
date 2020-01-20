class Transform:
    def __init__(self, coords=(0, 0), parent=None):
        self.local_x, self.local_y = coords
        self.parent = parent
        self.children = []

    def get_global_coords(self):
        if not self.parent:
            return int(self.local_x), int(self.local_y)
        parent_global_coords = self.parent.get_global_coords()
        return (int(self.local_x) + parent_global_coords[0],
                int(self.local_y) + parent_global_coords[1])

    def attach(self, child):
        if child.parent:
            child.parent.children.remove(child)
            old_parent = child.parent.get_global_coords()
        else:
            old_parent = (0, 0)
        new_parent = self.get_global_coords()
        child.local_x += old_parent[0] - new_parent[0]
        child.local_y += old_parent[1] - new_parent[1]
        self.children.append(child)
        child.parent = self

    def move_to(self, coords, delta_time):
        speed = delta_time / 300
        self.local_x = self.local_x - (self.local_x - coords[0]) * speed
        self.local_y = self.local_y - (self.local_y - coords[1]) * speed
