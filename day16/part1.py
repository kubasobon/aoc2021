import colorama
import string


class Packet:
    TYPE = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "literal",
        5: "",
        6: "",
        7: "",
    }

    def __init__(self, bits):
        assert all(b in "01" for b in bits)  # binary
        self.subpackets = []
        self.header = bits[:3]  # 3 bits
        self.type_id = bits[3:6]  # 3 bits
        self.tail = bits[6:]
        self.v = None

        self.length_type_id = None
        self.packet_len = None
        if self.is_literal():
            self.v = self.__value()  # cut tail
        if not self.is_literal():
            self.length_type_id = bits[6]
            self.tail = bits[7:]
            if self.length_type_id == "0":
                self.packet_len = 15  # length in bits of sub-packets
                bytes_to_read = int(self.tail[:15], 2)
                self.tail = self.tail[15:]
                self.parse_subpackets(self.tail[:bytes_to_read])
                self.tail = self.tail[bytes_to_read:]
            elif self.length_type_id == "1":
                self.packet_len = 11  # number of immediate sub-packets
                packets_to_read = int(self.tail[:11], 2)
                for _ in range(packets_to_read):
                    self.tail = self.tail[11:]
                    sp = Packet(self.tail[:11])
                    self.subpackets.append(sp)

    def packet_type(self):
        return int(self.type_id, 2)

    def is_literal(self):
        return Packet.TYPE[self.packet_type()] == "literal"

    def is_operator(self):
        return not self.is_literal()

    def __value(self):
        if not self.is_literal():
            return None
        if self.v is not None:  # run once
            return self.v
        bit_repr = ""
        pointer = 0
        read_more = True
        while read_more:
            control = self.tail[pointer]
            if self.tail[pointer] == "0":
                read_more = False
            bit_repr += self.tail[pointer + 1 : pointer + 5]  # read 4 bits
            pointer += 5
        self.tail = self.tail[pointer:]
        return int(bit_repr, 2)

    def parse_subpackets(self, bits):
        tail = bits
        while tail and not all(ch == "0" for ch in tail):
            p = Packet(tail)
            self.subpackets.append(p)
            tail = p.tail


def sum_versions(p):
    total = int(p.header, 2)
    print(total)
    for sp in p.subpackets:
        total += sum_versions(sp)
    return total


if __name__ == "__main__":
    # Test packets:
    #    VVVTTTAAAAABBBBBCCCCC
    # b = "110100101111111000101000"
    #    VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB
    # b = "00111000000000000110111101000101001010010001001000000000"
    #    VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC
    # b = "11101110000000001101010000001100100000100011000001100000"

    with open("input.txt") as f:
        hex_data = f.readline().strip(string.whitespace)

    hex_data = "8A004A801A8002F478"
    # convert hex to bin, stringify, cut off leading '0b'
    b = str(bin(int(hex_data, 16)))[2:]
    print(f"hex: {hex_data}")
    print(f"bin: {b}")
    p = Packet(b)
    print(f"sum: {sum_versions(p)}")
