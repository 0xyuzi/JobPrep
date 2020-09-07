# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
# order of DIRECTIONS is important! 
DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]
class Solution:
    """
    :type robot: Robot
    :rtype: None
    """
    def cleanRoom(self, robot):
        #write your code here
        
        visited = set()
        
        self.dfs((0,0), robot, 0, visited)
        
    
    def dfs(self,pos, robot, direction, visited):
        if pos in visited:
            return 
        
        visited.add(pos)
        
        robot.clean()
        
        for _ in range(4):
            if robot.move():
                next_x = pos[0] + DIRECTIONS[direction][0]
                next_y = pos[1] + DIRECTIONS[direction][1]
                
                self.dfs((next_x, next_y), robot, direction, visited)
                
                self.go_back(robot)
            robot.turnRight()
            direction = (direction + 1) % len(DIRECTIONS)
        
    
    def go_back(self,robot):
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnRight()
        robot.turnRight()