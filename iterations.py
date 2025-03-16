import math

def create_tuple(n: int, chord: float) -> tuple:
    factor = (chord / 2) ** 2
    half_cord = math.sqrt((1 - math.sqrt(1 - factor)) ** 2 + factor)
    return (n, chord, factor, half_cord, half_cord * n)

last_chord = math.sqrt(2)
rows = []
for n in range(2, 13):
    row = create_tuple(2 ** n, last_chord)
    rows.append(row)
    last_chord = row[3]

print("n".rjust(7), "chord".center(12), "factor".center(12), "half cord".center(12), "rough pi".center(12))
for n, chord, factor, half_cord, rough_pi in rows:
    print(
        str(n).rjust(7),
        rf"{chord:.7f}".rjust(12),
        rf"{factor:.7f}".center(12),
        rf"{half_cord:.7f}".center(12),
        rf"{rough_pi:.7f}".center(12)
    )
