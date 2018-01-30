from __future__ import absolute_import
from __future__ import print_function
import rake
import collections
from sklearn.datasets import load_breast_cancer
__author__ = 'a_medelyan'
class Data:
    def __init__(self):
        users = []

def dictionatyOfPostIdAndText(file = "trainPosts.json"):
    posts = []
    for post in file:
        posts[post.id] = post.text
    return posts

post = dictionatyOfPostIdAndText("data")

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

class who:
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

def fillDictionaryOfSubjectsAndUsersWhoLikeThisSub(data, favoriteSub):
    dictionay = {}
    for post in data.posts:
        subjects = findSubject(post)
        for sub in subjects:
            for user in data.users:
                if sub in favoriteSub[user]:
                    dictionay[sub].append(user)
    return dictionay

def findSubject(post):
    stoppath = "SmartStoplist.txt"

    # 1. initialize RAKE by providing a path to a stopwords file
    rake_object = rake.Rake(stoppath, 2, 2, 2)

    # 2. run on RAKE on a given text
    keywords = rake_object.run(post)

    return keywords

def findUsersThatLikedThisPost(post, data):
    pass

def postsThatThisUserLiked(user, data):
    pass

def basedOnSubject(subject, sub_usersDict, p):
    return (sub_usersDict[subject], p)

def basedOnPeopelLikedIt(usersThatLiked, data, p):
    posts = []
    answer = []
    for user in usersThatLiked:
        posts.append(postsThatThisUserLiked(user, data))
    for post in posts:
        answer.append((findUsersThatLikedThisPost(post, data), p))
    return answer

def answersBasedOnSubject(subject, sub_usersDict, usersThatLiked, data):
    answer = []
    answer.append(basedOnPeopelLikedIt(usersThatLiked, data, 3))
    answer.append(basedOnSubject(subject, sub_usersDict, 2))
    return answer

def answersBasedOnRelatedsubjects(subject, sub_usersDict, subjectRelationDict):
    relatedSubs = subjectRelationDict[subject]
    answer = []
    for sub in relatedSubs:
        answer.append(basedOnSubject(sub, sub_usersDict, 1))
    return answer

def clustering(data):
    pass

def main(post, data):
    usersThatLikedThePost = findUsersThatLikedThisPost(post, data)
    finalAnswer = []
    subject = findSubject(post)
    favoriteSub = findFavoriteSubsForEachUser(data)
    sub_usersDict = fillDictionaryOfSubjectsAndUsersWhoLikeThisSub(data, favoriteSub)
    subjectRelationDict = fillDictionaryOfsubjectsAndreltedSubjects(data)
    finalAnswer.append(answersBasedOnSubject(subject, sub_usersDict, usersThatLikedThePost, data))
    finalAnswer.append(answersBasedOnRelatedsubjects(subject, sub_usersDict, subjectRelationDict))


