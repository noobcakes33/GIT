import requests, json

class RepoCommits:

    def __init__(self):
        self.user = input("enter the GitHub user name: \n")
        self.res = self.getRepoCommits(self.user)
        if self.res != None:
            for self.i in self.res:
                print(self.i)
        else:
            print('Invalid Request!')


    def getRepoCommits(self, user):
        """
            Args: userId (string)
            Returns: Repo name and number of commits made (list)
        """

        try:
            url = 'https://api.github.com/users/{}/repos'.format(user)
        except requests.exceptions.InvalidURL:
            print('Invalid URL!')
        except requests.exceptions.ConnectionError:
            print('Invalid Request!')
        except requests.exceptions.InvalidSchema:
            print('Invalid Request!')
        else:
            # Get response from the git url
            response = requests.get(url)
            # Response status code
            responseCode = response.status_code
            # Check if the status code is 200
            if  responseCode == 200:
                # Then return dictionary of repos
                repositories = json.loads(response.content)
                repoData = list()

                # Looping through the keys of the repositories dictionary
                for repo in repositories: # repositories is dict
                    repoName = repo['name']
                    repoURL = 'https://api.github.com/repos/{}/{}/commits'.format(user, repoName)
                    # get request from the repoURL
                    commits = requests.get(repoURL)
                    # stores commits content in the commits dict
                    commits = json.loads(commits.content)
                    # stores number of commits (keys of dict)
                    numCommits = len(commits)
                    # storing reponame and number of commits in the repoData empty list
                    repoData.append('Repo: {}, Number of commits: {}'.format(repoName, numCommits))

                return repoData

if __name__ == "__main__":
    rc = RepoCommits()
