def sign(x: float) -> int:
    return 1 if x > 0 else (-1 if x < 0 else 0)

def bisection(xL: float, xR: float, f, e: float) -> float:
    fL, fR = f(xL), f(xR)

    while sign(fL) == sign(fR):
        if abs(fR) < abs(fL):
            xR += xR - xL
            fR = f(xR)
        else:
            xL -= xR - xL
            fL = f(xL)

    xD = (xR - xL) / 2
    xM = xL + xD

    fM = f(xM)

    while abs(fM) > e:
        if sign(f(xL)) != sign(fM):
            xR = xM
        else:
            xL = xM
        
        xD /= 2

        xM = xL + xD
        fM = f(xM)
    
    return xM
