class Elevator:
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor
    
    def go_to_floor(self, floor):
        if 1 <= floor <= self.max_floor:
            self.current_floor = floor
        else:
            print("Invalid Floor!")
    
    def report_current_floor(self):
        print(f"{self.current_floor}")

    def operate_elevator(self):
        while True:
            floor_input = input("")
            
            if floor_input.lower() == 'done':
                break
            
            try:
                floor = int(floor_input)
                self.go_to_floor(floor)
            except ValueError:
                print("Invalid Floor!")
        
        # แสดงผลลัพธ์
        self.report_current_floor()

# รับค่าชั้นสูงสุดที่ลิฟต์สามารถเคลื่อนที่ไปถึงได้
max_floor = int(input(""))
elevator = Elevator(max_floor)

# เรียกใช้เมธอด operate_elevator
elevator.operate_elevator()
