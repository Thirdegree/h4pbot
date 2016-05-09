import praw, obot, re

r = obot.login()
pattern = r"(?i)(?:Hillary For Prison|Another Year For Hillary|I will guard her|I will guard it)"

with open(per, "r") as f:
    tot = float(f.readline())

def main():
    for com in praw.helpers.comment_stream(r, "hillaryforprison", limit=None):
        if re.match(pattern, com.body):
            tot += 1
            com.reply("Hillary's sentence just got a year longer ! Total length : " + tot + "years!")
            with open(per, "w") as f: 
                per.write(tot)

if __name__ == '__main__':
    main()
