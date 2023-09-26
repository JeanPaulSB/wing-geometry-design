class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

    def get_coordinates(self) -> tuple:
        return (self.x,self.y)
    
    def __str__(self) -> str:
        return f"({self.x},{self.y})"
