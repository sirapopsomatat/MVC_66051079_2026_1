class TalentView:
    # แสดงเมนูให้ผู้ใช้งานติดต่อกับระบบ
    def show_main_menu(self):
        print("\n" + "="*45)
        print("    Ladkrabang's Got Talent System")
        print("="*45)
        print("1. ดูรายชื่อผู้เข้าแข่งขัน")
        print("2. ให้ผลการแสดง (ปกติ)")
        print("3. ใช้สิทธิ์ Golden Buzzer")
        print("4. ดูสรุปผลแบ่งตามสถานะ")
        print("5. ออกจากระบบ")
        return input("กรุณาเลือกเมนู (1-5): ")

    def show_contestants(self, contestants_info):
        print("\n--- รายชื่อผู้เข้าแข่งขัน ---")
        for c in contestants_info:
            print(f"[{c['id']}] {c['name']} (โชว์: {c['performance']}) | สถานะ: {c['status']} | {c['desc']}")

    def get_vote_input(self):
        j_id = input("รหัสกรรมการ (เช่น J01): ").strip().upper()
        c_id = input("รหัสผู้เข้าแข่งขัน (เช่น P01): ").strip().upper()
        res = input("ผลการตัดสิน (พิมพ์ PASS หรือ FAIL): ").strip().upper()
        return j_id, c_id, res

    def get_gb_input(self):
        j_id = input("รหัสกรรมการ (เช่น J01): ").strip().upper()
        c_id = input("รหัสผู้เข้าแข่งขัน (เช่น P01): ").strip().upper()
        return j_id, c_id

    def show_message(self, msg, is_error=False):
        if is_error:
            print(f"\n[แจ้งเตือนข้อผิดพลาด] {msg}")
        else:
            print(f"\n[ทำรายการสำเร็จ] {msg}")

    def show_summary(self, contestants_info):
        print("\n--- สรุปผลการแข่งขัน ---")
        categories = {"รอผล": [], "ผ่านเข้ารอบ": [], "ไม่ผ่านเข้ารอบ": []}
        for c in contestants_info:
            if c['status'] in categories:
                categories[c['status']].append(c)

        for stat, items in categories.items():
            print(f"\n>> หมวดหมู่: {stat} ({len(items)} คน)")
            if not items:
                print("   (ไม่มีข้อมูล)")
            for c in items:
                print(f"   - [{c['id']}] {c['name']} : {c['desc']}")