import GIT, unittest

class UnitTests(unittest.TestCase):

    def testCase0(self):
        self.assertEqual(GIT.repository(''), "[username] provide username")
        username = 0
        self.assertEqual(GIT.repository(username), "{}: not valid".format(str(username)))
        self.assertEqual(GIT.repository(list()), "[repository] repositories list empty")

    def testCase1(self):
        repositories = GIT.repository('richkempinski')
        self.assertIn('helloworld', repositories)

    def testCase2(self):
        repositories_list = GIT.repository('otavara')
        self.assertIn('Triangle567', repositories_list)
        self.assertIn('GitHubApi567', repositories_list)

    def testCase_commits_number(self):
        self.assertEqual(GIT.commitsNumber("otavara",'',''), "repositories list empty")
        self.assertEqual(GIT.commitsNumber("otavara",list(("Triangle567","GitHubApi567")),''), "[repository] Provide a repository to view")
        self.assertEqual(GIT.commitsNumber("",list(("Triangle567","GitHubApi567")),'Triangle567'), "[username] provide username")

    def testCase_commits(self):
        repositories = GIT.repository('richkempinski')
        self.assertEqual(GIT.commitsNumber("richkempinski",repositories,'helloworld'), 2)

    def testCase2_commits_number(self):
        repositories = GIT.repository('otavara')
        self.assertEqual(GIT.commitsNumber('otavara', repositories, 'Triangle567'), 6)

if __name__ == "__main__":
    print("[Running UnitTests]")
    #ut = UnitTests()
    unittest.main()
