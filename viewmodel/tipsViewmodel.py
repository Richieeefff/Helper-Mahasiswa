from model.tipsModel import load_tips_data, save_tips_data

def add_tip(admin, tips):
    tips_data = load_tips_data()
    
    for key in tips_data:
        if tips_data[key] == tips:
            return False
    
    tips_data[admin] = tips
    save_tips_data(tips_data)
    return True

def get_all_tips():
    return load_tips_data()
