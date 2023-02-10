class Solution(object):
    def capitalizeTitle(self, title):
        title = title.split(" ")

        t = []

        for s in title:
            if len(s) >= 3:
                t.append(s.capitalize())
            else: t.append(s.lower())

        title = " ".join(i for i in t)

        return title