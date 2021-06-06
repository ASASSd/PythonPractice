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
            'D3': struct_parced[3],
            'D4': struct_parced[4],
            'D5': struct_parced[5],
            'D6': struct_parced[6],
            'D7': struct_parced[7],
            'D8': struct_parced[8],
            'D9': struct_parced[9]
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
    print(a_parsed)
    print(bytez[a_parsed[3]:a_parsed[3] + a_parsed[2] - 1])
    print(struct.unpack('ffff',bytez[a_parsed[3]:a_parsed[3] + a_parsed[2] - 1]))
    a3_parsed = struct.unpack('>' + 'f' * a_parsed[2], bytez[a_parsed[3]:a_parsed[3] + a_parsed[2]])
    a5_parsed = struct.unpack('>' + 'b' * a_parsed[5], bytez[a_parsed[6]:a_parsed[6] + a_parsed[5]])
    return {'A1': parseB(a_parsed[0], bytez),
            'A2': a_parsed[1],
            'A3': a3_parsed,
            'A4': a_parsed[4],
            'A5': a5_parsed}


def f31(bytestr):
    return parceA(5, bytestr)


print(f31(b'GYJCj\x00#\xd1\xc8\xde\xc9\x11\xfc|\xfa\x00\x04\x00\x82\x9e\xdf\x95\xfd\x12'
b'\x82\xadx\x00\x00\x00\x03\x00\x92X\xc3\xf7\xdb\x1f\x95B\xd9\x0b\x83\x1e'
b'\x9e\x12\xdaL\xcf\xb9\x1f\x89V%&@\xac\xd6\xb5\x94\x9fW3\xcf=H\x1c\x8d'
b'^\x02\xa5Q%?\xf4\x16\r6\xfec\xdd\xfa\x92\x17\xdc%\xcb\xd0%\xea\xb2\x8f'
b'>\xf3\x9a\xb0\xa7!)\xba\x91b8\xf5\x89\x00\x02\x00\x00\x00!z\xd0\x123\xa5'
b'H!\x8b;y\xafF\x98\x06\t\x14\xeeo\xea\xbf?\xb4\x06\xbfw}\x87?\x0e'
b'x\xd0\xbb\xca\xf3s\xae\x93\xec'))