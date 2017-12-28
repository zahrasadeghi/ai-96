from __future__ import absolute_import
from __future__ import print_function
import rake
import collections
__author__ = 'a_medelyan'


class Data:
    def __init__(self):
        users = []

def dictionatyOfPostIdAndText(file):
    posts = []
    for post in file:
        posts[post.id] = post.text
    return posts


post = dictionatyOfPostIdAndText("trainPosts.json")


class User:
    def __init__(self, id):
        likedPostsIds = []
        id = id
        likedBlogs = []

    def favoriteSubjects(self):
        favoriteSubs = []
        finalAnswer = []
        for id in self.likedPostsIds:
            favoriteSubs.append(findSubject(post[id]))
        allPosts = len(favoriteSubs)
        counter = collections.Counter(favoriteSubs)
        for i in counter.keys():
            if counter[i]/allPosts > 0.25:
                finalAnswer.append(i)
        return finalAnswer


class PredictWhoWillLikeThisPost:
    def fillDictionaryOfsubjectsAndreltedSubjects(data):
        dictionary = {}
        for post in data.posts:
            subjects = findSubject(post)
            for sub in subjects:
                dictionary[sub].append(subjects)
        return dictionary

    def predict(self, data, post, blogId):
        users = []
        for user in data.users:
            if blogId in user.likedBlog:
                users.append(user)
        users = data.blogs[blogId].followers()
        subject = findSubject(post)
        finalAnswer = []
        subjectRelationDict = self.fillDictionaryOfsubjectsAndreltedSubjects(data)
        for user in users:
            if (subject in user.favoriteSubjects()):
                finalAnswer.append((user, 1))
            for sub in subjectRelationDict[subject]:
                if (sub in user.favoriteSubjects()):
                    finalAnswer.append((user, 2))
        for user in data.users:
            if (subject in user.favoriteSubjects()):
                finalAnswer.append((user, 3))
            for sub in subjectRelationDict[subject]:
                if (sub in user.favoriteSubjects()):
                    finalAnswer.append((user, 4))


def findSubject(post):
    stoppath = "SmartStoplist.txt"

    # 1. initialize RAKE by providing a path to a stopwords file
    rake_object = rake.Rake(stoppath, 2, 2, 2)

    # 2. run on RAKE on a given text
    keywords = rake_object.run(post)

    return keywords



def findFavoriteSubsForEachUser(data):
    favoriteSubs = []
    finalDictionary = {}
    for user in data.users:
        for post in postsThatThisUserLiked(user, data):
            favoriteSubs.append(findSubject(post))
        allPosts = len(favoriteSubs)
        counter = collections.Counter(favoriteSubs)
        for i in counter.keys():
            if counter[i]/allPosts > 0.25:
                finalDictionary[user].append(i)
        favoriteSubs = []
    return finalDictionary


