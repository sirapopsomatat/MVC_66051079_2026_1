class TalentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def run(self):
        while True:
            choice = self.view.show_main_menu()
            if choice == '1':
                self.view.show_contestants(self.model.contestants)
            elif choice == '2':
                j_id, c_id, res = self.view.get_vote_input()
                try:
                    self.model.vote(j_id, c_id, res)
                    self.view.show_message(f"กรรมการ {j_id} ให้ผลผู้เข้าแข่งขัน {c_id} เป็น {res}")
                except ValueError as e:
                    self.view.show_message(str(e), is_error=True)
            elif choice == '3':
                j_id, c_id = self.view.get_gb_input()
                try:
                    self.model.use_golden_buzzer(j_id, c_id)
                    self.view.show_message(f"กรรมการ {j_id} ใช้ Golden Buzzer ให้ผู้เข้าแข่งขัน {c_id}")
                except ValueError as e:
                    self.view.show_message(str(e), is_error=True)
            elif choice == '4':
                for c in self.model.contestants:
                    status, desc = self.model.get_contestant_status(c['id'])
                    c['status'] = status
                    c['desc'] = desc
                self.view.show_summary(self.model.contestants)
            elif choice == '5':
                print("ออกจากระบบเรียบร้อย")
                break
            else:
                print("กรุณาเลือกเมนูที่ถูกต้อง (1-5)")