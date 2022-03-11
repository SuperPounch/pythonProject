# hw model - synthesizable operations only
def anlz_byte(src_byte):
    wrk_byte = src_byte
    lsb_detected = False
    lsb = 0
    for i in range(7, -1, -1):
        if (wrk_byte & 0x80) == 0:
            #print("wrk_byte& 0x80=" + format(wrk_byte & 0x80))
            lsb_detected = True
            lsb = i
            #print("lsb="+str(lsb))
        wrk_byte = wrk_byte << 1
    return lsb_detected, lsb

def lsb(x):
    byte_lsb = [0, 0, 0, 0]
    byte_lsb_detected = [False, False, False, False]
    # stage 0: analyze least significant zeroes in individual bytes (in parallel)
    #print("x >> 0) & 0xff="+format((x >> 0) & 0xff))
    byte_lsb_detected[0], byte_lsb[0] = anlz_byte((x >> 0) & 0xff)
    #print("x >> 8) & 0xff=" + format((x >> 8) & 0xff))
    byte_lsb_detected[1], byte_lsb[1] = anlz_byte((x >> 8) & 0xff)
    #print("x >> 16) & 0xff=" + format((x >> 16) & 0xff))
    byte_lsb_detected[2], byte_lsb[2] = anlz_byte((x >> 16) & 0xff)
    #print("x >> 24) & 0xff=" + format((x >> 24) & 0xff))
    byte_lsb_detected[3], byte_lsb[3] = anlz_byte((x >> 24) & 0xff)
    # stage 1: produce final result of analysis
    lsb = 0
    for i in range(3, -1, -1):
        if byte_lsb_detected[i]:
            lsb = byte_lsb[i]+ (i << 3)
            print("for循环"+ str(lsb))
    print(str(lsb))
    return lsb
# generating test stimulus
for i in range(0, 16):
    x = pow(2, (i*2)+1) + i*333
    x = x | (x >> 1) | (x >> 2)
    print("x: " + '0x{:08x}'.format(x) + ", lsb: " + str(lsb(x)))
