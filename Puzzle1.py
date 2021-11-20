"""
Solve 8-puzzle problem using best first search?

"""
def puzzle_solver(puzzle):
    """
    This function takes a puzzle as input and returns the solution to the puzzle
    """
    # Initialize the start node with the given puzzle
    start_node = Node(puzzle,0,0)
    # Create an empty list to store the visited nodes
    visited = []
    # Create an empty list to store the nodes to be visited
    queue = []
    # Append the start node to the queue
    queue.append(start_node)
    # Loop till the queue is empty
    while len(queue) > 0:
        # Pop the first node from the queue
        node = queue.pop(0)
        # Check if the node is the goal node
        if node.data == [[1,2,3],[4,5,6],[7,8,'_']]:
            return node
        # Check if the node is already visited
        if node.data not in visited:
            # Append the node to the visited list
            visited.append(node.data)
            # Generate the child nodes from the current node
            children = node.generate_child()
            # Loop through the generated child nodes
            for child in children:
                # Check if the child node is already visited
                if child.data not in visited:
                    # Append the child node to the queue
                    queue.append(child)
    return None

# Class node
class Node:
    def __init__(self,data,level,fval):
        """ Initialize the node
        """
        self.data = data
        self.level = level
        self.fval = fval
    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x,y = self.find(self.data,'_')
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.level+1,0)
                children.append(child_node)
        return children
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
    def copy(self,root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
    def find(self,puz,x):
        """ Specifically used to find the position of the blank space """
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j
    def print_puzzle(self):
        """ Print the puzzle """
        for i in self.data:
            for j in i:
                print(j,end=" ")
            print()
    def print_solution(self):
        """ Print the solution """
        print("Solution is: ")
        self.print_puzzle()
        print("Number of moves: ",self.level)
            
    # Main function
def main():
    """ Main function """
    # Initialize the puzzle
    puzzle = [[1,2,3],[4,5,6],[7,8,'_']]
    # Solve the puzzle
    solution = puzzle_solver(puzzle)
    # Print the solution
    solution.print_solution()
    
    # Call the main function
if __name__ == "__main__":
    main()
