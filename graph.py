"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Somya Krishna and Iniya Vidyashankar, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1:sk55256
UT EID 2:iv3976
"""

import sys

# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------
RESET_CHAR = "\u001b[0m"  # Code to reset the terminal color
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
}
BLOCK_CHAR = "\u2588"  # Character code for a block


def colored(text, color):
    """Wrap the string with the color code."""
    color = color.strip().lower()
    if color not in COLOR_DICT:
        raise ValueError(color + " is not a valid color!")
    return COLOR_DICT[color] + text


def print_block(color):
    """Print a block in the specified color."""
    print(colored(BLOCK_CHAR, color) * 2, end="")


# -----------------------PRINTING LOGIC, DON'T WORRY ABOUT THIS PART----------------------------


class Node:
    """
    Represents a node in a singly linked list.

    Instance Variables:
        data: The value or data stored in the node.
        next: The reference to the next node in the linked list (None by default).
    """

    def __init__(self, data, link=None):
        """
        Initializes a new node with the given data and a reference to the next node.

        Args:
            data: The data to store in the node.
            next: Optional; the next node in the linked list (None by default).
        """
        self.data = data
        self.next = link

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")


class StackError(Exception):
    """An Exception raised when the Stack class performs an illegal operation"""


class Stack:
    """
    A class that implements a stack using a singly linked list.

    Instance Variables:
        _top: The top node of the stack.
        _size: The number of elements in the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack with no elements.
        """
        self._top = None
        self._size = 0

    def peek(self):
        """
        Returns the value at the top of the stack without removing it.

        Raises:
            StackError: If the stack is empty, raises "Peek from empty stack.".

        Returns:
            The data stored in the top node of the stack.
        """
        if self.is_empty():
            raise StackError("Peek from empty stack.")
        return self._top.data

    def push(self, item):
        """
        Pushes a new item onto the top of the stack.

        Args:
            item: The data to push onto the stack.
        """
        new_node = Node(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1

    def pop(self):
        """
        Removes and returns the item at the top of the stack.

        Raises:
            StackError: If the stack is empty, raises "Pop from empty stack.".

        Returns:
            The data from the top node of the stack.
        """
        if self.is_empty():
            raise StackError("Pop from empty stack.")
        removed_data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return removed_data

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self._top is None

    def size(self):
        """
        Returns the number of items in the stack.

        Returns:
            The size of the stack as an integer.
        """
        return self._size


class QueueError(Exception):
    """An Exception raised when the Queue class performs an illegal operation"""


class Queue:
    """
    A class that implements a queue using a singly linked list with a tail.

    Instance Variables:
        _front: The beginning node of the queue.
        _rear: The end node of the queue.
        _size: The number of elements in the queue.
    """

    def __init__(self):
        """
        Initializes an empty queue with no elements.
        """
        self._front = None
        self._rear = None
        self._size = 0

    def peek(self):
        """
        Returns the value at the front of the queue without removing it.

        Raises:
            QueueError: If the queue is empty, raises "Peek from empty queue.".

        Returns:
            The data stored in the front node of the queue.
        """
        if self.is_empty():
            raise QueueError("Peek from empty queue.")
        return self._front.data

    def enqueue(self, item):
        """
        Enqueues a new item at the end of the queue.

        Args:
            item: The data to put at the end of queue.
        """
        new_node = Node(item)
        if self.is_empty():
            self._front = new_node
        else:
            self._rear.next = new_node
        self._rear = new_node
        self._size += 1

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.

        Raises:
            QueueError: If the queue is empty, raises "Dequeue from empty queue.".

        Returns:
            The data from the front node of the queue.
        """
        if self.is_empty():
            raise QueueError("Dequeue from empty queue.")
        front_data = self._front.data
        self._front = self._front.next
        if self._front is None:  # If queue becomes empty
            self._rear = None
        self._size -= 1
        return front_data

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self._size == 0

    def size(self):
        """
        Returns the number of items in the queue.

        Returns:
            The size of the queue as an integer.
        """
        return self._size


class ColoredVertex:
    """Class for a graph vertex."""

    def __init__(self, index, x, y, color):
        self.index = index
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    def add_edge(self, vertex_index):
        """Add an edge to another vertex."""
        self.edges.append(vertex_index)

    def visit_and_set_color(self, color):
        """Set the color of the vertex and mark it visited."""
        self.visited = True
        self.prev_color = self.color
        self.color = color
        print("Visited vertex " + str(self.index))

    def __str__(self):
        return f"index: {self.index}, color: {self.color}, x: {self.x}, y: {self.y}"


class ImageGraph:
    """Class for the graph."""

    def __init__(self, image_size):
        self.vertices = []
        self.image_size = image_size

    def print_image(self):
        """Print the image formed by the vertices."""
        img = [
            ["black" for _ in range(self.image_size)] for _ in range(self.image_size)
        ]

        # Fill img array
        for vertex in self.vertices:
            img[vertex.y][vertex.x] = vertex.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # Print new line/reset color
        print(RESET_CHAR)

    def reset_visited(self):
        """Reset the visited flag for all vertices."""
        for vertex in self.vertices:
            vertex.visited = False

    # Create the adjacency matrix.
    # Return the matrix at the end
    def create_adjacency_matrix(self):
        """
        Creates and returns the adjacency matrix for the graph.

        post: return a 2D list of integers representing the adjacency matrix.
        """
        n = len(self.vertices)
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for vertex in self.vertices:
            for neighbor in vertex.edges:
                matrix[vertex.index][neighbor] = 1
        return matrix


    def bfs(self, start_index, color):
        """
        You must implement this algorithm using a Queue.

        Performs a Breadth-First Search (BFS) starting from a given vertex, changing
        all vertices that are adjacent and share the same color as the starting
        vertex's color to the given color. Think of how an image bucket fill will
        only change all same colored pixels that are in contact with each other.

        Do not remove the first 2 statements we provide.
        you may choose to call print_images in this method debugging yourself


        This method assumes that the pre conditions have been handled before
        calling this method.

        pre: start_index is a valid integer representing the index of the starting
             vertex in the vertices instance variable.
             color: The color to change vertices to during the BFS traversal

        post: every vertex that matches the start index's color will be recolored
              to the given color
        """

        self.reset_visited()
        print("Starting BFS; initial state:")
        self.print_image()

        original_color = self.vertices[start_index].color
        q = Queue()
        q.enqueue(start_index)

        while not q.is_empty():
            current_index = q.dequeue()
            current_vertex = self.vertices[current_index]

            if (not current_vertex.visited and
                current_vertex.color == original_color):

                current_vertex.visit_and_set_color(color)
                self.print_image()

                for neighbor_index in sorted(current_vertex.edges):
                    neighbor_vertex = self.vertices[neighbor_index]
                    if (not neighbor_vertex.visited and
                        neighbor_vertex.color == original_color):
                        q.enqueue(neighbor_index)

    def dfs(self, start_index, color):
        """
        You must implement this algorithm using a Stack WITHOUT using recursion.

        Performs a Depth-First Search (DFS) starting from a given vertex, changing
        all vertices that are adjacent and share the same color as the starting
        vertex's color to the given color. Think of how an image bucket fill will
        only change all same colored pixels that are in contact with each other.

        Do not remove the first 2 statements we provide.
        you may choose to call print_images in this func method debugging yourself


        This method assumes that the pre conditions have been handled before
        calling this method.

        pre: start_index is a valid integer representing the index of the starting
             vertex in the vertices instance variable.
             color: The color to change vertices to during the DFS traversal

        post: every vertex that matches the start index's color will be recolored
              to the given color
        """

        self.reset_visited()
        print("Starting DFS; initial state:")
        self.print_image()

        original_color = self.vertices[start_index].color
        s = Stack()
        s.push(start_index)

        while not s.is_empty():
            current_index = s.pop()
            current_vertex = self.vertices[current_index]

            if (not current_vertex.visited and
                current_vertex.color == original_color):

                current_vertex.visit_and_set_color(color)
                for neighbor_index in sorted(current_vertex.edges, reverse=True):
                    neighbor_vertex = self.vertices[neighbor_index]
                    if (not neighbor_vertex.visited and
                        neighbor_vertex.color == original_color):
                        s.push(neighbor_index)


def create_graph(data):
    """
    Creates a Graph object from the given input data and parses the starting
    position and search color.

    pre: data is the entire inputted data as a single string.

    post: a tuple containing the ImageGraph instance, the starting position,
          and the search color.
    """

    # split the data by new line

    # get size of image and number of vertices

    # create the ImageGraph

    # create vertices - vertex info has the format "x,y,color"

    # create edges between vertices - edge info has the format "from_index,to_index"
    # connect vertex A to vertex B and the other way around

    # read search starting position and color

    # return the ImageGraph, starting position, and color as a tuple in this order.
    lines = data.strip().split("\n")

    image_size = int(lines[0])
    num_vertices = int(lines[1])

    graph = ImageGraph(image_size)

    for i in range(2, 2 + num_vertices):
        x, y, color = lines[i].split(",")
        graph.vertices.append(ColoredVertex(i - 2, int(x.strip()), int(y.strip()), color.strip()))

    idx = 2 + num_vertices
    num_edges = int(lines[idx])

    for i in range(idx + 1, idx + 1 + num_edges):
        from_idx, to_idx = map(int, lines[i].split(","))
        graph.vertices[from_idx].add_edge(to_idx)
        graph.vertices[to_idx].add_edge(from_idx)

    start_info = lines[idx + 1 + num_edges]
    start_index_str, start_color = start_info.split(",")
    start_index = int(start_index_str.strip())
    start_color = start_color.strip()

    return graph, start_index, start_color

def main():
    """
    The main function that drives the program execution.

    This function will not be tested, but you should
    implement it to test your code visually.
    """

    # read all input as a single string.
    data = sys.stdin.read()

    # create graph, passing in data

    # print adjacency matrix in a readable format (maybe row by row)

    # run bfs

    # reset by creating graph again

    # run dfs
    graph, start_index, color = create_graph(data)

    matrix = graph.create_adjacency_matrix()
    for row in matrix:
        print(row)

    graph.bfs(start_index, color)

    graph, start_index, color = create_graph(data)
    graph.dfs(start_index, color)


if __name__ == "__main__":
    main()
