from address_parser import address_parser as ap
import unittest


class TestAddressParser(unittest.TestCase):
    def test_simple_cases(self):
        t1 = 'Miritiba 339'
        t2 = 'Babaçu 500'
        t3 = 'Cambuí 804B'
        t4 = 'Coca 2901'
        t5 = 'Palmeiras 12'
        self.assertEqual(ap(t1), ('Miritiba', '339'))
        self.assertEqual(ap(t2), ('Babaçu', '500'))
        self.assertEqual(ap(t3), ('Cambuí', '804B'))
        self.assertEqual(ap(t4), ('Coca', '2901'))
        self.assertEqual(ap(t5), ('Palmeiras', '12'))

    def test_complicated_cases(self):
        t1 = 'Rio Branco 23'
        t2 = 'Quirino dos Santos 23 b'
        t3 = 'Cam buí 804B'
        t4 = 'Coc a 2901'
        t5 = 'Pal mei ras 12'
        self.assertEqual(ap(t1), ('Rio Branco', '23'))
        self.assertEqual(ap(t2), ('Quirino dos Santos', '23 b'))
        self.assertEqual(ap(t3), ('Cam buí', '804B'))
        self.assertEqual(ap(t4), ('Coc a', '2901'))
        self.assertEqual(ap(t5), ('Pal mei ras', '12'))

    def test_bonus_foreign_addresses(self):
        t1 = 'Calle 44 No 1991'
        t2 = '100 Broadway Av'
        t3 = 'Calle Sagasta, 26'
        t4 = '4, Rue de la République'
        self.assertEqual(ap(t1), ('Calle 44', 'No 1991'))
        self.assertEqual(ap(t2), ('Broadway Av', '100'))
        self.assertEqual(ap(t3), ('Calle Sagasta', '26'))
        self.assertEqual(ap(t4), ('Rue de la République', '4'))


if __name__ == "__main__":
    unittest.main()
