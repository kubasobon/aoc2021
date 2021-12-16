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
        assert all(b in '01' for b in bits) # binary
        self.subpackets = []
        self.header = bits[:3]   # 3 bits
        self.type_id = bits[3:6] # 3 bits
        self.tail = bits[6:]

        self.length_type_id = None
        self.packet_len = None
        if not self.is_literal():
            self.length_type_id = bits[6]
            self.tail = bits[7:]
            if self.length_type_id == "0":
                self.packet_len = 15   # length in bits of sub-packets
                bytes_to_read = Packet(self.tail[:15]).value()
                assert bytes_to_read is not None
                self.subpackets = self.parse_subpackets(self.tail[:bytes_to_read])
                self.tail = self.tail[bytes_to_read:]
            elif self.length_type_id == "1":
                self.packet_len = 11   # number of immediate sub-packets
                packets_to_read = Packet(self.tail[:11]).value()
                assert packets_to_read is not None
                self.tail = self.tail[11:]
                for _ in range(packets_to_read):
                    sp = Packet(self.tail[:11])
                    self.subpackets.append(sp)
                    self.tail = self.tail[11:]

    def packet_type(self):
        return int(self.type_id, 2)

    def is_literal(self):
        return Packet.TYPE[self.packet_type()] == "literal"

    def is_operator(self):
        return not self.is_literal()

    def value(self):
        if not self.is_literal():
            return None
        bit_repr = ""
        pointer = 0
        read_more = True
        while read_more:
            control = self.tail[pointer]
            if self.tail[pointer] == "0":
                read_more = False
            bit_repr += self.tail[pointer+1:pointer+5] # read 4 bits
            pointer += 5
        return int(bit_repr, 2)

if __name__ == "__main__":
    #    VVVTTTAAAAABBBBBCCCCC
    b = "110100101111111000101000"
    p = Packet(b)
    print(p.header)
    print(p.type_id)
    print(p.tail)
    print(p.subpackets)
    if p.is_literal():
        print(p.value())
