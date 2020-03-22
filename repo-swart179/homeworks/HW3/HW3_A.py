# CSCI 1133, Lab Section 002, HW 3, Problem A
# Daniel Swarts, swart179

def CMYK_to_RGB(C,M,Y,K):

    R = int(round(255 * (1-C*0.01) * (1-K*0.01)))
    G = int(round(255 * (1-M*0.01) * (1-K*0.01)))
    B = int(round(255 * (1-Y*0.01) * (1-K*0.01)))

    R_G_B = [R,G,B]
    return R_G_B

def main():

    
    C = int(input("Cyan component: "))
    M = int(input("Magenta component: "))
    Y = int(input("Yellow component: "))
    K = int(input("Black (Key) component: "))
    R_G_B_list = CMYK_to_RGB(C,M,Y,K)
    print("RGB representation:",R_G_B_list[0],R_G_B_list[1],R_G_B_list[2])


if __name__ == "_main_":
    main()
