import praw

reddit = praw.Reddit('perm_bot')

subreddit = reddit.subreddit('math+learnmath+programming+programmerhumor')

for submission in subreddit.stream.submissions():
    for comment in submission.comments.list(): #Navigates comments in a BFS manner.
        #Look for permutation(s) in comment.body
        #Find some fact about that permutation or set of permutations
        #Reply with found fact with comment.reply



