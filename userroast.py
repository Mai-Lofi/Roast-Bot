
class UserRoast:

    def __init__(self, name, username, description):
        self.username = username
        self.name = name
        self.description = description

    def roast_by_name(self):
        # UserRoast -> str
        # Creates a roast if the the name contains keywords love or says
        uname = self.name
        kword = "Love "
        if kword in uname:
            lv = word_after(uname, kword)
            return ("Hey @" + self.username + " it's great and all that you love "
                    + lv + ", but like I just chatted with your mom and she said"
                    + " she would love if you could take a shower and move"
                    + " our of her bacement 👵😡 💩🚿")
        kword = "says "
        if kword in uname:
            lv = word_after(uname, kword)
            return ("@" + self.username + " says "
                    + lv + " more like " + self.username
                    + "'s doctor says to loose some weight "
                    + "👨‍⚕️🤷  🍕🤰🍩")
        else:
            # return an empty string if no keyword in the name
            return ""


    def roast_by_bio(self):
        # UserRoast -> str
        # Returns custom roast if the bio contains certain words
        d = self.description
        if "NFT" in d:
            return ("Yo @" + self.username + " I dont even think I need to roast "
                    + "you as you need to wake up every day living with your" +
                    " terrible financial decision... Nobody cares about your jpg " +
                    "so plz stop.PS. Bitcoin dropped 30 percent last week 😂😂")
        if "dog" in d:
            return ("@" + self.username + " you seem to REALLY like your dog... "
                    + "Just becase you love dogs and not cats does not " +
                    "exclude you from becoming a crazy lady. TBH you prob "
                    + "feed your dog better food then your family 🐶😳")
        else:
            # If these words are not found return empty string
            return ""


    def roast_by_hobby(hb, self):
        # str, UserRoast -> str
        # returns custom roast based on a users hobby
        if hb == "anime":
            return ("Lmaooooo get your weeb ass out of the bacement lol. The "
                    + "The only reason @" + self.username + " likes 2d anime "
                    + "girls is because all the real woman run away 🏃😢 😂😂😂")
        if hb == "gaming":
            return ("Real talk with @" + self.username + " now. I dont know how"
                    + "your life became consisting of a bag of doritos and "
                    + "fortnite but we can get you back on track. Call me back "
                    + "after you shower, you can do it! 🙏😌")
        if hb == "Trump ":
            return ("Hey @" + self.username + " you kinda have a lil Trump "
                    + "obsession... idk if you love or hate him but we can move"
                    + " on now.... I dont care if he caused you HUGEEE issues "
                    + "but go tell him on truth social 😂😂😂")
        if hb == "Biden":
            return ("Lmaoo @" + self.username + " you better not unironicly be "
                    + "talking about boring ol politics on twitter. Lets talk about "
                    + "how good ol joey cant ride a bike 🚴🤕 😂😂😂")
        if hb == "art ":
            return ("Yo @" + self.username + ' What sort of "art" are you looking '
                    + "at 🤔... Arts cool and all but have you heard of grass? 🌾"
                    + " The sun is also p dope as awell ☀️ "
                    + "Give it a shot sometime!")
        if (hb == "football") or (hb == "baseball"):
            return ("Uhhh @" + self.username + " So your telling me you invite "
                    + "guys over to your house and watch men play with balls "
                    + 'all day 🤨  ...ok "bro" ')
        if hb == "reddit":
            return ("Do I actually need to roast @" + self.username + " man "
                    + "deadass gets yelled at by his mom everyday to move out"
                    + " of his house, shower, shave his neckbeard, and to not" +
                    " wear the fedora 🤓🖥️ ...poor mom 👵")
        if hb == "food":
            return ("Ey yo @" + self.username + " I like food as well ya know but"
                    + " how many calories did you say you were eating every "
                    + "day 🤔 ...ok bro I will let your doctor talk to you "
                    + "about your McHabits 🍟")
        if hb == "running":
            return ("The only reason @" + self.username + " runs is because "
                    + "they were bullied in school... Just because you call it a "
                    + '"hobby" now, it really is just the same thing lol 🏃 🤛😠')
        if hb == "meme":
            return ("Hey @" + self.username + " you do know people follow you "
                    + "for the memes you steal not actually you, right? 🤷")
        else:
            # If user has no hobbies return a complement!
            return ("Good for you @" + self.username + "for not spending your "
                    + "time on twitter. I donthave a roast for you! 😁 ... Or "
                    + "you are just into uncommon hobbies 😳")


    def word_after(s, keyword):
        # str, str -> str
        # Returns the word after keyword in a string
        sindex = s.find(keyword)
        return ((s[(len(keyword) + sindex):]).split())[0]