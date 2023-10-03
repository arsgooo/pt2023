import unittest
import pawnshop as ps

class TestGoodsFunctions(unittest.TestCase):
    def setUp(self):
        self.goods = {"Radio": 200, "Headphones": 300}

    def test_add_good_normal(self):
        ps.add_good(self.goods, "Laptop", 1000)
        self.assertIn("Laptop", self.goods)

    @unittest.expectedFailure
    def test_add_good_wrong(self):
        self.assertTrue(ps.add_good(self.goods, 700, "Necklace"))
        self.assertTrue(ps.add_good(self.goods, "Phone", "900"))
        self.assertTrue(ps.add_good(self.goods, 500, 400))

    def test_remove_good(self):
        ps.remove_good(self.goods, "Radio") #removing radio and checking that it doesn't exist anymore
        self.assertNotIn("Radio", self.goods)

        with self.assertRaises(ValueError): #trying to remove radio again and facing error
            ps.remove_good(self.goods, "Radio")

    def test_get_goods_amount(self):
        amount = ps.get_goods_amount(self.goods)
        self.assertEqual(amount, 2)

    def test_get_total_cost(self):
        total_cost = ps.get_total_cost(self.goods)
        self.assertEqual(total_cost, 500)

if __name__ == "__main__":
    unittest.main()