colour_dic = {"black": "#000000", "blue1": "#0000ff",
              "brown": "#a52a2a", "coral": "ff7f50",
              "DarkOrange": "#ff8c00", "DarkOrchid": "#9932cc",
              "DeepPink1": "#ff1493", "firebrick": "#b22222",
              "ForestGreen": "#228b22", "gold1": "#ffd700"}
colour_name = input("Enter colour name:")
while colour_name != "":
    print("Colour code: {}".format(colour_dic.get(colour_name)))
    colour_name = input("Enter colour name:")
