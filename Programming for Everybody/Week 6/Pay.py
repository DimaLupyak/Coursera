def computepay(h,r):
    if h < 40:
        return h * r
    else:
        return (40 + (h - 40) * 1.5) * r

hours = input("Enter Hours:")
rate = input("Enter Rate:")

p = computepay(float(hours), float(rate))
print("Pay",p)