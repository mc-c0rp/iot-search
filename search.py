import data

def check_vin(num, vin_path):
    vin = data.load_json(vin_path)
    print(vin)
    if vin == None:
        return -1

    if num in vin:
        if vin[num]['s-iot'].replace(' ', '') == '':
            return 1
        
        text = f"Вин-номер самоката: {vin[num]['vin']}\nСерийный номер iot'a: {vin[num]['s-iot']}\nНомер самоката: {vin[num]['index']}"
        return text
    else:
        return 0