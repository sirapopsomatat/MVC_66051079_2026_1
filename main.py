from Models.model import TalentModel
from Views.view import TalentView
from Controllers.controller import TalentController

def main():
    model = TalentModel(data_folder='data')
    view = TalentView()
    controller = TalentController(model, view)
    
    # ทำการเริ่มรันระบบ
    controller.run()

if __name__ == "__main__":
    main()