import json
def calculate_scores(data):
    if not data:
        return None

    # กำหนดค่าเริ่มต้นสำหรับค่ามากสุดและค่าน้อยสุด
    high_score = data[0]
    low_score = data[0]
    total_score = 0

    # หาค่ามากสุด, ค่าน้อยสุด, และผลรวม
    for score in data:
        if score > high_score:
            high_score = score
        if score < low_score:
            low_score = score
        total_score += score

    # คำนวณค่าเฉลี่ย
    avg_score = round(total_score / len(data), 2)

    # สร้าง tuple ที่มีลักษณะ (ค่ามากสุด, ค่าน้อยสุด, ค่าเฉลี่ย)
    result_tuple = (round(high_score, 2), round(low_score, 2), avg_score)
    return result_tuple

# รับข้อมูลคะแนนจากผู้ใช้
try:
    my_list = json.loads(input(""))
    result = calculate_scores(my_list)

    if result:
        print(f"{result}")
    else:
        print("Empty list. Please enter scores.")
except json.JSONDecodeError:
    print("Invalid JSON format. Please enter a valid JSON list.")
except Exception as e:
    print(f"An error occurred: {e}")
