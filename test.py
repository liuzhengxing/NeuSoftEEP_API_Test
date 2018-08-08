run_status = {
            'smoke_production': True,
            'smoke_logistics': False,
            'smoke_quality': False,
            'smoke_equipment': False
        }

for mod in run_status:
    if run_status[mod]:
        print(mod)