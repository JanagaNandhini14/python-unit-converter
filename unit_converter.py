# unit_converter.py
CONVERSIONS_TO_METER = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "in": 0.0254,
    "ft": 0.3048
}

def convert(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in CONVERSIONS_TO_METER or to_unit not in CONVERSIONS_TO_METER:
        raise ValueError("Unsupported unit")
    meters = value * CONVERSIONS_TO_METER[from_unit]
    return meters / CONVERSIONS_TO_METER[to_unit]

def main():
    print("Units: m, km, cm, mm, in, ft")
    try:
        val = float(input("Value: "))
    except ValueError:
        print("Invalid number")
        return
    f = input("From unit: ")
    t = input("To unit: ")
    try:
        res = convert(val, f, t)
        print(f"{val} {f} = {res} {t}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
