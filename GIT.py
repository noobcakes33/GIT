import requests
import json

def repository(username):
    if username == "":
        return "[username] provide username"
    elif (username == list()):
        return "[repository] repositories list empty"
    elif (not isinstance(username, str)):
        return "{}: not valid".format(str(username))
    elif((requests.get("https://api.github.com/users/" + str(username) + "/repos")).json() == []):
        return "The account [{username}] does not have any repositories".format(username)
    else:
        arr = list()
        x = json.loads(requests.get('https://api.github.com/users/'+str(username)+'/repos').text)

        for i in x:
            try:
                array += [i['name']]
            except:
                print("API RATE LIMIT EXCEEDED")


    return arr

def commitsNumber(username, repositories_list, repository):
    if(not isinstance(repositories_list, list)):
        return "repositories list empty"
    if (username == ""):
        return "[username] provide username"
    if (repository == ""):
        return "[repository] Provide a repository to view"
    try:
        j = json.loads(requests.get('https://api.github.com/repos/'+username+'/'+ repository +'/commits').text)
        commits_num = len(j)
    except:
        print("{} not found in {}'s repo".format(repository, username))

    return commits_num

def main():
    username = input('GitHub User ID: ')
    print(str(json.loads(requests.get('https://api.github.com/users/'+ username +'/repos').text)['message']))
    repositories_list = repository(username)
    for repo in (repositories_list):
        print('Repo: '+ repository +' Number of commits: '+ commitsNumber(username, repositories_list, repo))

if __name__ == '__main__':
    main()
