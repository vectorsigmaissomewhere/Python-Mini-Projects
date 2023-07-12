#Conversation Based Mad-libs game in Python
#conversation taken from https://www.englishfor2day.com/article/dialogue/177
your_friend_name = input("Enter your friend's name: ")
name = input("Enter your name: ")
greeting = input("Greet her: ")
herself1 = your_friend_name + ": I am fine, thank you. Why are you looking so sad?"
print(herself1)
yourself1 = input("Give her a reason, like getting worried about your examination: ")
herself2 = your_friend_name + ": Well, I'm going on well with my studies. I am worried about my exam."
print(herself2)
yourself2 = input("Ask her about her preparation: ")
herself3 = your_friend_name + ": You know I'm weak in English. That's why I'm taking special care in English. I'm having a detailed revision in other subjects."
print(herself3)
yourself3 = input("Ask her if she is taking any help from any special books: ")
herself4 = your_friend_name + ": Yes, but I study textbooks very carefully."
print(herself4)
yourself4 = input("Tell her that you also want to get interested in reading textbooks: ")
herself5 = your_friend_name + ": Yes, I think it'll be very helpful not only for English but also for other subjects."
print(herself5)
yourself6 = input("Greet her by saying that she supported you and also greet her for her exams: ")
herself6 = your_friend_name + ": You are most welcome."
print(herself6)

madlibs = name + ": " + greeting + "\n" + herself1 + "\n" + name + ": " + yourself1 + "\n" + herself2 + "\n" + name + ": " + yourself2 + "\n" + herself3 + "\n" + name + ": " + yourself3 + "\n" + herself4 + "\n" + name + ": " + yourself4 + "\n" + herself5 + "\n" + name + ": " + yourself6 + "\n" + herself6
print("\n\n\n\n")
print("Entire conversation")
print(madlibs)
