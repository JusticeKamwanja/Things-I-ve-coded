from lrc_reader import LRCReader

lyrics = [
    ['Wanasemaga mapenzi safari', 0.08, 0.3],
    ['Unavyopipta ndo jinsi unajongea', 0.07, 0.6],
    ['Ila niendapo ni mbali sijui ka ntafika sababu natembea', 0.07, 0.8],
    ['Niliposikiaga habari, ', 0.08, 0.05],
    ['yakisifika nkakesha nangojea', 0.07, 0.6, 'False'],
    ['Akabariki Jalali, ', 0.07, 0.805,],
    [ 'na nikawika mziki nkauotea', 0.08, 0.6, 'False'],
    ['Ile pruu mpaka Macca',],
    ['Nikadandiaga Bongo movie',],
    ['Kumbe mapenzi hayataki haraka',],
    ['Ni kama tango natia tu chumyi',],
    ['Mwenzenu nikaoza haswa',],
    ['Na kujitia kitandani mjuzi',],
    ['Eti nataka fukuza paka', 0.08, 0.05],
    ['Badala ya mbwa ', 0.08, 0.05],
    ['nkafuga mbuzi ',  0.08, 0.05, 'False'],
    ['mmmh', 0.08, 0.03,  'False'],
    ['Wivu ukanifanya nkagombana ', 0.08, 0.03],
    ['na marafiki', 0.08, 0.3,  'False'],
    ['Ugomvi na mamangu, ',  0.07, 0.01],
    ['akiniambia siambiliki',  0.07, 0.01,  'False'],
]

if __name__ == '__main__':
    LRCReader.sing(lyrics)