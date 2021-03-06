#-------------------------------------------------------------------------------
# Name:        Trojan.Netduke - HAMMERTOSS (APT29) String Decryptor
# Ref Url:     'https://www2.fireeye.com/rs/848-DID-242/images/rpt-apt29-hammertoss.pdf'
# Purpose:     Decryptor for strings embedded in the HAMMERTOSS samples
#
# Author:      Ptr32Void - @Ptr32Void
#
# Ref MD5:     d3109c83e07dd5d7fe032dc80c581d08
#-------------------------------------------------------------------------------

import string

def decrypt_string_array(enc_array):
    i = 0
    dec_buff = {}
    while i < len(enc_array):
        dec_buff[i] =  chr(enc_array[i] ^ (i % 256) ^ 170)
        i += 1
    return dec_buff


def build_string_based_on_index(dec_buff):
    string_indexes = [
        '(0, 0, 10);',
        '(1, 10, 3);',
        '(2, 13, 1);',
        '(3, 14, 0);',
        '(4, 14, 1);',
        '(5, 15, 1);',
        '(6, 16, 4);',
        '(7, 20, 7);',
        '(8, 27, 3);',
        '(9, 30, 21);',
        '(10, 51, 6);',
        '(11, 57, 27);',
        '(12, 84, 16);',
        '(13, 100, 8);',
        '(14, 108, 59)',
        '(15, 167, 24)',
        '(16, 191, 18)',
        '(17, 209, 2); ',
        '(18, 211, 9);',
        '(19, 220, 2);',
        '(20, 222, 1);',
        '(21, 223, 36)',
        '(22, 259, 28)',
        '(23, 287, 12)',
        '(24, 299, 1);',
        '(25, 300, 4); ',
        '(26, 304, 15) ',
        '(27, 319, 19) ',
        '(28, 338, 1); ',
        '(29, 339, 5); ',
        '(30, 344, 7); ',
        '(31, 351, 9); ',
        '(32, 360, 21) ',
        '(33, 381, 16) ',
        '(34, 397, 3); ',
        '(35, 400, 8); ',
        '(36, 408, 3); ',
        '(37, 411, 4); ',
        '(38, 415, 17) ',
        '(39, 432, 6); ',
        '(40, 438, 5); ',
        '(41, 443, 7); ',
        '(42, 450, 6); ',
        '(43, 456, 5); ',
        '(44, 461, 10) ',
        '(45, 471, 60) ',
        '(46, 531, 18) ',
        '(47, 549, 12);'
    ]

    print 'Decrypted strings:'
    for si in string_indexes:
        pos = si.find(', ')
        num = int (si[1:pos], 10)

        pos = si.find(' ')
        pos1 = si.find(', ', pos)
        start_string = int (si[pos+1:pos1])

        pos2 = si.find(')')
        end_string_count = int (si[pos1+2:pos2])

        c = 0
        decrypted = ''
        idx = start_string
        while c < end_string_count:
            decrypted += dec_buff[idx]
            idx += 1
            c += 1
        print '[%d] -> %s' % (num, decrypted)

def main():
    enc_byte_array = [
                    201, 194, 216, 193, 203, 221, 248, 200, 218, 215, 235, 196,
                    223, 251, 138, 134, 153, 192, 136, 196, 202, 200, 213, 201,
                    198, 214, 194, 213, 223, 193, 228, 199, 229, 237, 225, 229,
                    235, 219, 251, 232, 231, 247, 173, 226, 233, 233, 240, 224,
                    244, 239, 235, 221, 247, 254, 240, 241, 253, 216, 209, 254,
                    173, 213, 201, 206, 222, 163, 194, 207, 211, 223, 174, 222,
                    159, 170, 191, 201, 131, 175, 145, 138, 143, 221, 156, 130,
                    196, 186, 174, 178, 155, 153, 206, 218, 151, 131, 159, 173,
                    161, 143, 158, 129, 190, 160, 174, 162, 148, 146, 132, 164,
                    142, 140, 129, 156, 133, 152, 141, 139, 140, 154, 146, 137,
                    141, 134, 131, 148, 132, 139, 135, 186, 76, 95, 95, 72,
                    92, 74, 112, 96, 75, 64, 82, 78, 85, 72, 66, 81,
                    102, 114, 86, 77, 91, 77, 82, 88, 70, 19, 117, 73,
                    70, 91, 91, 71, 111, 121, 84, 68, 111, 102, 98, 73,
                    107, 112, 97, 99, 106, 98, 66, 108, 104, 104, 108, 75,
                    107, 113, 95, 104, 97, 103, 127, 124, 127, 109, 113, 86,
                    2, 14, 11, 2, 49, 46, 31, 30, 13, 0, 9, 0,
                    18, 14, 11, 11, 9, 21, 23, 2, 78, 2, 7, 76,
                    15, 8, 66, 12, 18, 69, 12, 69, 122, 123, 122, 13,
                    8, 127, 125, 96, 114, 115, 112, 113, 107, 119, 116, 117,
                    106, 118, 27, 105, 110, 111, 113, 109, 98, 99, 96, 97,
                    102, 103, 100, 101, 154, 159, 158, 200, 230, 253, 156, 206,
                    234, 238, 150, 237, 223, 158, 148, 193, 136, 215, 136, 221,
                    249, 233, 197, 241, 223, 253, 198, 211, 229, 143, 137, 241,
                    229, 252, 230, 229, 225, 238, 232, 173, 199, 241, 242, 224,
                    238, 243, 233, 233, 178, 167, 249, 183, 180, 160, 162, 179,
                    184, 172, 172, 190, 247, 169, 189, 250, 132, 136, 132, 128,
                    141, 132, 209, 207, 163, 128, 131, 132, 150, 147, 204, 204,
                    193, 217, 136, 141, 151, 139, 144, 152, 154, 146, 131, 153,
                    130, 150, 147, 167, 175, 173, 173, 187, 171, 189, 246, 237,
                    135, 177, 178, 225, 162, 168, 179, 171, 182, 180, 185, 189,
                    254, 173, 185, 174, 189, 166, 162, 178, 179, 139, 152, 186,
                    93, 119, 107, 70, 64, 91, 73, 67, 86, 13, 105, 100,
                    19, 78, 73, 66, 110, 84, 107, 77, 76, 86, 82, 90,
                    65, 65, 83, 106, 28, 106, 26, 124, 100, 125, 105, 101,
                    103, 107, 44, 94, 107, 100, 110, 96, 114, 114, 118, 96,
                    70, 90, 124, 118, 124, 122, 93, 121, 125, 113, 117, 77,
                    87, 115, 123, 119, 15, 55, 52, 61, 11, 2, 28, 49,
                    62, 55, 5, 12, 22, 23, 11, 18, 31, 9, 11, 17,
                    27, 19, 16, 80, 55, 11, 21, 18, 3, 3, 29, 26,
                    36, 27, 39, 37, 39, 44, 53, 109, 32, 58, 48, 32,
                    53, 52, 100, 104, 13, 50, 54, 61, 49, 40, 15, 41,
                    43, 63, 53, 113, 62, 62, 48, 49, 207, 197, 136, 132,
                    203, 193, 207, 194, 198, 198, 196, 226, 201, 202, 201, 196,
                    212, 223, 152, 226, 144, 226, 231, 252, 159, 233, 209, 156,
                    204, 234, 207, 135, 166, 184, 245, 213, 253, 211, 207, 226,
                    236, 247, 229, 239, 242, 169, 205, 192, 175
                ]

    build_string_based_on_index( decrypt_string_array(enc_byte_array) )



if __name__ == '__main__':
    main()
