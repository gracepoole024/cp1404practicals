"""
CP1404/CP5632 Practical 5
Hex Colours Program
"""

COLOUR_TO_CODE = {"banana yellow": "#ffe135", "cameo pink": "#efbbcc", "deep champagne": "#fad6a5",
                  "emerald": "#50c878",
                  "ferrari red": "#ff2800", "glossy grape": "#85754e", "heliotrope": "#df73ff", "inchworm": "#b2ec5d",
                  "jazzberry jam": "#a50b5e", "zomp": "#39a78e"}

colour = input("Enter colour: ").lower()
while colour != "":
    try:
        print(colour.title(), "is", COLOUR_TO_CODE[colour])
    except KeyError:
        print("Invalid colour name")
    colour = input("Enter colour: ").lower()
