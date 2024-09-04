class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # X:Horizental Position Y:Vertical Position 
        maximum=0
        def change_position(position,direction):
            if position=="+Y":
                if direction==-2:
                    position="-X"
                else:
                    position="+X"
            elif position=="-Y":
                if direction==-1:
                    position="-X"
                else:
                    position="+X"
            elif position=="+X":
                if direction==-2:
                    position="+Y"
                else:
                    position="-Y"
            else:
                if direction==-1:
                    position="+Y"
                else:
                    position="-Y"
            return position
        obstacle_positions=set()
        for item in obstacles:
            obstacle_positions.add(tuple(item))
        
        position="+Y"
        X=0 
        Y=0
        for direction in commands:
            if direction==-2 or direction==-1:
                position=change_position(position,direction)
            
            else:
                if position=="+Y":
                    for i in range(Y+1,Y+direction+1):
                        if (X,i) in obstacle_positions:
                            Y=i-1
                            break
                        else:
                            Y=i 
                elif position=="-Y":
                    for i in range(Y-1,Y-direction-1,-1):
                        if (X,i) in obstacle_positions:
                            Y=i+1
                            break
                        else:
                            Y=i 
                elif position=="+X":
                    for i in range(X+1,X+direction+1):
                        if (i,Y) in obstacle_positions:
                            X=i-1
                            break
                        else:
                            X=i 
                else:
                    for i in range(X-1,X-direction-1,-1):
                        if (i,Y) in obstacle_positions:
                            X=i+1
                            break
                        else:
                            X=i
                maximum=max(maximum,X**2 +Y**2)
    
        return maximum