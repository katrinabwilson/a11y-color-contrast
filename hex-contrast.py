# Incomplete!
# Hex to decimal
def convertRBG(hex):
    # separate hex into pairs 
    # convert pairs into decimals
    
    #TODO input validation

    hex = hex.lstrip('#')
    r_dec = int(hex[0:2], 16)
    g_dec = int(hex[2:4], 16)
    b_dec = int(hex[4:6], 16)

    # print(r_dec)
    # print(g_dec)
    # print(b_dec)

    # return decimal representation
    return r_dec, g_dec, b_dec

R, G, B = convertRBG("#FFC0CB")
