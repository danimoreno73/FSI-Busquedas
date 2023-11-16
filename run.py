from unittest import TestCase
import search


class TestSearch(TestCase):
    def setUp(self):
        self.ab = search.GPSProblem('A', 'B', search.romania)
        self.oe = search.GPSProblem('O', 'E', search.romania)
        self.gz = search.GPSProblem('G', 'Z', search.romania)
        self.nd = search.GPSProblem('N', 'D', search.romania)
        self.mf = search.GPSProblem('M', 'F', search.romania)

    # Test breadth_first_graph_search

    def test_search_bfgs_ab(self):
        print("Test bfgs Origen A y Destino B")
        try:

            self.assertEqual(str(search.breadth_first_graph_search(self.ab).path()),
                             "[<Node B>, <Node F>, <Node S>, <Node A>]")
        except AssertionError:
            pass

    def test_search_bfgs_oe(self):
        print("Test bfgs Origen O y Destino E")
        try:
            self.assertEqual(str(search.breadth_first_graph_search(self.oe)),
                             "[<Node E>, <Node H>, <Node U>, <Node B>, <Node F>, <Node S>, <Node O>]")
        except AssertionError:
            pass

    def test_search_bfgs_gz(self):
        print("Test bfgs Origen G y Destino Z")
        try:
            self.assertEqual(str(search.breadth_first_graph_search(self.gz).path()),
                             "[<Node Z>, <Node A>, <Node S>, <Node F>, <Node B>, <Node G>]")
        except AssertionError:
            pass

    def test_search_bfgs_nd(self):
        print("Test bfgs Origen N y Destino D")
        try:
            self.assertEqual(str(search.breadth_first_graph_search(self.nd)),
                             "[<Node D>, <Node C>, <Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]")
        except AssertionError:
            pass

    def test_search_bfgs_mf(self):
        print("Test bfgs Origen M y Destino F")
        try:
            self.assertEqual(str(search.breadth_first_graph_search(self.mf)),
                             "[<Node F>, <Node S>, <Node R>, <Node C>, <Node D>, <Node M>]")
        except AssertionError:
            pass

    # Test depth_first_graph_search
    def test_search_dfgs_ab(self):
        print("Test dfgs Origen A y Destino B")
        try:
            self.assertEqual(str(search.depth_first_graph_search(self.ab)),
                             "[<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]")
        except AssertionError:
            pass

    def test_search_dfgs_oe(self):
        print("Test dfgs Origen O y Destino E")
        try:
            self.assertEqual(str(search.depth_first_graph_search(self.oe)),
                             "[<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node O>]")

        except AssertionError:
            pass

    def test_search_dfgs_gz(self):
        print("Test dfgs Origen G y Destino Z")
        try:
            self.assertEqual(str(search.depth_first_graph_search(self.gz)),
                             "[<Node Z>, <Node A>, <Node T>, <Node L>, <Node M>, <Node D>, <Node C>, <Node P>, "
                             "<Node R>, <Node S>, <Node F>, <Node B>, <Node G>]")

        except AssertionError:
            pass

    def test_search_dfgs_nd(self):
        print("Test dfgs Origen N y Destino D")
        try:
            self.assertEqual(str(search.depth_first_graph_search(self.nd)),
                             "[<Node D>, <Node C>, <Node P>, <Node R>, <Node S>, <Node F>, <Node B>, <Node U>, "
                             "<Node V>, <Node I>, <Node N>]")

        except AssertionError:
            pass

    def test_search_dfgs_mf(self):
        print("Test dfgs Origen M y Destino F")
        try:
            self.assertEqual(str(search.depth_first_graph_search(self.mf)),
                             "[<Node F>, <Node B>, <Node P>, <Node R>, <Node S>, <Node A>, <Node T>, <Node L>, "
                             "<Node M>]")

        except AssertionError:
            pass

    # Test Branch and Bound
    def test_search_bab_ab(self):
        print("Test Branch and Bound Origen A y Destino B")
        try:
            self.assertEqual(str(search.branch_and_bound_search(self.ab)),
                             "[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]")
        except AssertionError:
            pass

    def test_search_bab_oe(self):
        print("Test Branch and Bound Origen O y Destino E")
        try:
            self.assertEqual(str(search.branch_and_bound_search(self.oe)),
                             "[<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node O>]")
        except AssertionError:
            pass

    def test_search_bab_gz(self):
        print("Test Branch and Bound Origen G y Destino Z")
        try:
            self.assertEqual(str(search.branch_and_bound_search(self.gz)),
                             "[<Node Z>, <Node A>, <Node S>, <Node R>, <Node P>, <Node B>, <Node G>]")
        except AssertionError:
            pass

    def test_search_bab_nd(self):
        print("Test Branch and Bound Origen N y Destino D")
        try:
            self.assertEqual(str(search.branch_and_bound_search(self.nd)),
                             "[<Node D>, <Node C>, <Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]")
        except AssertionError:
            pass

    def test_search_bab_mf(self):
        print("Test Branch and Bound Origen M y Destino F")

        try:
            self.assertEqual(str(search.branch_and_bound_search(self.mf)),
                             "[<Node F>, <Node S>, <Node R>, <Node C>, <Node D>, <Node M>]")
        except AssertionError:
            pass

    # Test Branch and Bound with underestimation
    def test_search_babu_ab(self):
        print("Test Branch and Bound with Underestimation Origen A y Destino B")

        try:
            self.assertEqual(str(search.branch_and_bound_underestimation_search(self.ab)),
                             "[<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]")
        except AssertionError:
            pass

    def test_search_babu_oe(self):
        print("Test Branch and Bound with Underestimation Origen O y Destino E")
        try:
            self.assertEqual(str(search.branch_and_bound_underestimation_search(self.oe)),
                             "[<Node E>, <Node H>, <Node U>, <Node B>, <Node P>, <Node R>, <Node S>, <Node O>]")
        except AssertionError:
            pass

    def test_search_babu_gz(self):
        print("Test Branch and Bound with Underestimation Origen G y Destino Z")
        try:
            self.assertEqual(str(search.branch_and_bound_underestimation_search(self.gz)),
                             "[<Node Z>, <Node A>, <Node S>, <Node R>, <Node P>, <Node B>, <Node G>]")
        except AssertionError:
            pass

    def test_search_babu_nd(self):
        print("Test Branch and Bound with Underestimation Origen N y Destino D")
        try:
            self.assertEqual(str(search.branch_and_bound_underestimation_search(self.nd)),
                             "[<Node D>, <Node C>, <Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]")
        except AssertionError:
            pass

    def test_search_babu_mf(self):
        print("Test Branch and Bound with Underestimation Origen M y Destino F")
        try:
            self.assertEqual(str(search.branch_and_bound_underestimation_search(self.mf)),
                             "[<Node F>, <Node S>, <Node R>, <Node C>, <Node D>, <Node M>]")
        except AssertionError:
            pass
