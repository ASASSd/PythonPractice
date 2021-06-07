import struct

C_SIZE = 10
D_SIZE = 2 + 4 + 8 + 5 + 2 + 4
B_SIZE = C_SIZE * 7 + D_SIZE
A_SIZE = 2 + 8 + 2 + 2 + 8 + 4 + 2

def parseC(offset, bytez):
    struct_bytes = bytez[offset:offset + C_SIZE]
    struct_parsed = struct.unpack('>qh', struct_bytes)
    return {'C1': struct_parsed[0], 'C2': struct_parsed[1]}


def parseD(offset, bytez):
    struct_bytes = bytez[offset:offset + D_SIZE]
    struct_parced = struct.unpack('>HIqbbbbbhI',struct_bytes)
    struct1_bytes = bytez[struct_parced[1]:struct_parced[1] + struct_parced[0]]
    struct1_parsed = struct.unpack('>' + 'B' * struct_parced[0], struct1_bytes)
    return {'D1': list(struct1_parsed),
            'D2': struct_parced[2],
            'D3': list([struct_parced[3], struct_parced[4], struct_parced[5], struct_parced[6], struct_parced[7]]),
            'D4': struct_parced[8],
            'D5': struct_parced[9]
            }


def parseB(offset, bytez):
    list_c_parsed = [parseC(offset + addr * C_SIZE, bytez) for addr in range(7)]
    #for i in range(7):
    #    mas_c_parsed[i] = parseC(offset + i * C_SIZE, bytes)
    struct2_parsed = parseD(offset + C_SIZE * 7, bytez)
    return {'B1': list_c_parsed, 'B2': struct2_parsed}


def parceA(offset, bytez):
    a_bytes = bytez[offset:offset + A_SIZE]
    a_parsed = struct.unpack('>HqHHqIH', a_bytes)
    a3_parsed = struct.unpack('>' + 'f' * a_parsed[2], bytez[a_parsed[3]:a_parsed[3] + a_parsed[2] * 4])
    a5_parsed = struct.unpack('>' + 'b' * a_parsed[5], bytez[a_parsed[6]:a_parsed[6] + a_parsed[5]])
    return {'A1': parseB(a_parsed[0], bytez),
            'A2': a_parsed[1],
            'A3': list(a3_parsed),
            'A4': a_parsed[4],
            'A5': list(a5_parsed)}


def f31(bytestr):
    return parceA(5, bytestr)


#print(f31((b'GYJCj\x00$yC\xe8\xba\tn\x8c\xb6\x00\x03\x00\x83V\xb6\xec\x80\x87'
#b'\xbe\xf5i\x00\x00\x00\x02\x00\x8f\x00\x01\xc0W\x1f\xdd4\xf7\xc6\xa5m'
#b'\xde\xa1\t\xa4\x17[\xd1\xd0\xdeD1\xda\xdbdX7\xaeKT\x11\xc5\xf8\x84\x81'
#b'dB\x94\xd3\x9e\x1fy\xd2\x93\x84D\x0c\xc5\x1c\x89\x8eU6\xa1\x97p\xcf\xb9\xc0'
#b'\xbe\x88\xa2\x9e\xfa\xb0\x08\xe8\xf3c\x05\x8b\x19\xd4\x00\x03\x00\x00\x00!'
#b'j`\xac\xed\xd0\xd5\x81C\xf5\x1c\xea\x86\x03\xea\xe8\xcb?\xc9\xf3?\x07\x02i?'
#b'3\xf5D>\xad\x93\x13\xf1\xda')))