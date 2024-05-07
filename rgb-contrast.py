'''
This is one implementation of a color contrast checker: take 2 colors in RBG format 
and return their color contrast ratio. 

TODO - implement test cases from assignment spec
'''

# Computation Step: Convert to sRGB color format by dividing the integer value 255.
def sRBG(r, g, b):

    #TODO - input validation 

    r = round(r / 255, 4)
    g = round(g / 255, 4)
    b = round(b / 255, 4)

    return r, g, b

# Computation Step: Calculate a new value from the sRGB value
def luminance(sColor):
    # if RsRGB <= 0.03928 then R = RsRGB/12.92, else R = ((RsRGB+0.055)/1.055) ^ 2.4
    color_lum = None
    if sColor <= 0.03928:
        color_lum = sColor / 12.92
    else:
        color_lum = ((sColor + 0.055) / 1.055)**(2.4)

    return round(color_lum, 4)

# Computation Step: Calculate luminance for one color, using RGB values
def total_luminance(r_lum, g_lum, b_lum):
    # L = 0.2126 * R_lum + 0.7152 * G_lum + 0.0722 * B_lum
    L = (0.2126 * r_lum) + (0.7152 * g_lum) + (0.0722 * b_lum)
    return L

# Computation Step: Calculate the luminance ratio
def lum_ratio(L1, L2):
    # L2 > L1 → L_light - L2, L_dark = L1
    L_light = None
    L_dark = None

    if L2 > L1:
        L_light = L2
        L_dark = L1
    else:
        L_light = L1
        L_dark = L2
    
    ratio = (L_light + 0.05) / (L_dark + 0.05)
    return round(ratio, 4)

'''
Verify the user's input. If the RGB value is not an integer or is greater than 255,
flag the input and re-run the main() program. 
'''
def verify(color_num):
    try:
        color_num = int(color_num)
        
    except ValueError:
        print("Incorrect format! Try again.")
        main()
    
    if color_num > 255 or color_num < 0:
        print("Number is greater than 255! Try again.")
        main()
    else:
        return int(color_num)

def contrast(ratio):
    if ratio < 4.51:
        print(f"ratio is: {ratio} --> FAIL")
    
    else:
        print("ratio is: {ratio} --> PASS")

'''
Prompt the user for colors in RGB format. 
'''
def user_input():
    # Computation step: Begin with two colors in RGB integer format
    print("Please input the following in integer format (0 <= value <= 255): ")
    r1 = input("R value for color 1: ")
    r1 = verify(r1)

    g1 = input("G value for color 1: ")
    g1 = verify(g1)

    b1 = input("B value for color 1: ")
    b1 = verify(b1)

    r2 = input("R value for color 2: ")
    r2 = verify(r2)

    g2 = input("G value for color 2: ")
    g2 = verify(g2)

    b2 = input("B value for color 2: ")
    b2 = verify(b2)

    return r1, g1, b1, r2, g2, b2 

'''
Driving code. Run main to start the color contrast checker. 
'''
def main():
    # Use the input() funtion to get colors from user
    r1, g1, b1, r2, g2, b2 = user_input()

    # RGB integer format to sRGB
    r1_sRGB, g1_sRGB, b1_sRGB = sRBG(r1, g1, b1)
    r2_sRGB, g2_sRGB, b2_sRGB = sRBG(r2, g2, b2)

    # Calculate a new value R_lum from the RsRGB value
    R_lum_1 = luminance(r1_sRGB)
    G_lum_1 = luminance(g1_sRGB)
    B_lum_1 = luminance(b1_sRGB)

    R_lum_2 = luminance(r2_sRGB)
    G_lum_2 = luminance(g2_sRGB)
    B_lum_2 = luminance(b2_sRGB)

    L1 = total_luminance(R_lum_1, G_lum_1, B_lum_1)
    L2 = total_luminance(R_lum_2, G_lum_2, B_lum_2)

    ratio = lum_ratio(L1, L2)

    contrast(ratio)

main()