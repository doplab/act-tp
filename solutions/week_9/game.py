from binder import Binder, start

def collision(data):
    for i in range(len(data)-1):
        rec1 = data[i]
        for j in range(i+1, len(data)):
            rec2 = data[j]
            if rec1["x"] > rec2["x"] + 40 or rec2["x"] > rec1["x"] + 40:
                continue
            if rec1["y"] + 40 < rec2["y"] or rec2["y"] + 40 < rec1["y"]:
                continue
            data[i]["deleted"] = True
            data[j]["deleted"] = True
    return data

start(51, collision)