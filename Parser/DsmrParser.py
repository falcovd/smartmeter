def extract_input(inp):
    try:
        splitted = inp.split(":")
        key_value = splitted[1].split("(")

        key = key_value[0]

        if key == "24.2.1":
            v = key_value[2]
        else:
            v = key_value[1]

        value = v.split(")")[0]

        return [key, value]
    except:
        return False

def accepted_codes():
    return ["1.8.1", "1.8.2", "2.8.1", "2.8.2", "1.7.0", "2.7.0", "21.7.0", "22.7.0", "24.2.1"]

def get_floated_value(inp):
    val = inp.split("*")
    return float(val[0])
