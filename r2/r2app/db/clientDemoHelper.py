import time
import numpy as np
import random

from ..models.models import Thing

SAMPLE = "Of course machines can't think as people do. A machine is different from a person. Hence, they think differently. The interesting question is, just because something, uh... thinks differently from you, does that mean it's not thinking? Well, we allow for humans to have such divergences from one another. You like strawberries, I hate ice-skating, you cry at sad films, I am allergic to pollen. What is the point of... different tastes, different... preferences, if not, to say that our brains work differently, that we think differently? And if we can say that about one another, then why can't we say the same thing for brains... built of copper and wire, steel? No one normal could have done that. Do you know, this morning... I was on a train that went through a city that wouldn't exist if it wasn't for you. I bought a ticket from a man who would likely be dead if it wasn't for you. I read up on my work... a whole field of scientific inquiry that only exists because of you. Now, if you wish you could have been normal... I can promise you I do not. The world is an infinitely better place precisely because you weren't."

MID_POINT = len(SAMPLE) / 2

class DemoHelper:

    def __init__(self) -> None:
        self.start_timer = None

    def start_time(self, method, text):
        self.start_timer = time.time()
        print("==================")
        print(f'{method} 1000 THINGS ({text}) START')

    def end_time(self, method, text):
        time_elapsed = '%.2f' % ((time.time() - self.start_timer) * 1000.00)
        print(f'{method} 1000 THINGS TIME ELAPSED: {time_elapsed} ms')
        return self.return_message(text, method, time_elapsed)

    def char_field(self):
        return SAMPLE[random.randint(0, MID_POINT):random.
                        randint(MID_POINT, len(SAMPLE))]

    def bool_field(self):
        return np.random.choice([True, False], size = 1)

    def int_field(self):
        return random.randint(0, 3000)

    def return_message(self, text, method, time):
        return f"{text} {method} Complete im {time} ms, please check your server terminal for more information."

    def generate_thing(self):
        return Thing(name="Post Name",
                    description="Post Description",
                    content=DemoHelper.char_field(),
                    upvote_count=DemoHelper.int_field(),
                    downvote_count=DemoHelper.int_field())
