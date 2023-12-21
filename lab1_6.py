class Elevator:
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor
    
    def go_to_floor(self, floor):
        while True:
            self.floor = input("")
            if self.floor.lower() == 'done':
                break
            if
    
    def report_current_floor(self):
        print(f"{self.current_floor}")