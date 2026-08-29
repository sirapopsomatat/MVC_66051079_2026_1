import csv
import os

class TalentModel:
    def __init__(self, data_folder='data'):
        # โหลดข้อมูลเก็บไว้ใน List
        self.judges = self.load_data(os.path.join(data_folder, 'judges.csv'))
        self.contestants = self.load_data(os.path.join(data_folder, 'contestants.csv'))
        self.decisions = self.load_data(os.path.join(data_folder, 'decisions.csv'))
        self.golden_buzzers = self.load_data(os.path.join(data_folder, 'golden_buzzers.csv'))

    def load_data(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, mode='r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                return list(reader)
        else:
            return []

    def get_contestant_status(self, contestant_id):
        for gb in self.golden_buzzers:
            if gb['contestant_id'] == contestant_id:
                return "ผ่านเข้ารอบ", "Golden Buzzer"
        votes   = [d for d in self.decisions if d['contestant_id'] == contestant_id]
        if len(votes) == 4:
            pass_count = sum(1 for v in votes if v['result'] == 'PASS')
            if pass_count >= 3:
                return "ผ่านเข้ารอบ", f"ผลโหวต: {pass_count} PASS / {len(votes)} โหวต"
            else:
                return "ไม่ผ่านเข้ารอบ", f"ผลโหวต: {pass_count} PASS / {len(votes)} โหวต"
        else:
            return "รอผล", f"ผลโหวต: {len(votes)} /4 โหวต"

    def vote(self, judge_id, contestant_id, result):
        status, _ = self.get_contestant_status(contestant_id)
        if status != "รอผล":
            raise ValueError("ผู้เข้าแข่งขันไม่ได้อยู่ในสถานะรอผล")

        for d in self.decisions:
            if d['judge_id'] == judge_id and d['contestant_id'] == contestant_id:
                raise ValueError("กรรมการเคยให้ผลปกติแล้ว")
        
        self.decisions.append({
            'judge_id': judge_id,
            'contestant_id': contestant_id,
            'result': result
        })

    def use_golden_buzzer(self, judge_id, contestant_id):
        if any(gb['judge_id'] == judge_id for gb in self.golden_buzzers):
            raise ValueError("กรรมการคนนี้เคยใช้ Golden Buzzer ไปแล้ว")
        status, _ = self.get_contestant_status(contestant_id)
        if status == "ไม่ผ่านเข้ารอบ" or status == "ผ่านเข้ารอบ":
            raise ValueError("ผู้เข้าแข่งขันไม่ได้อยู่ในสถานะรอผล")
        for d in self.decisions:
            if d['judge_id'] == judge_id and d['contestant_id'] == contestant_id:
                raise ValueError("กรรมการเคยให้ผลปกติแล้ว")
        self.golden_buzzers.append({
            'judge_id': judge_id,
            'contestant_id': contestant_id
        })
    def get_all_contestants_info(self):
        info = []
        for c in self.contestants:
            status, desc = self.get_contestant_status(c['id'])
            info.append({
                'id': c['id'],
                'name': c['name'],
                'performance': c['performance'],
                'status': status,
                'desc': desc
            })
        return info
