#!/usr/bin/env python
"""
Welcome to www.nyymanni.com

This web page tells the story of my life.

As it might be obvious from the style of this website, my tool of choice is GNU
Emacs. I also get along with Vim-folks, since I prever vim-style keybindings and
use evil-mode. I am highly allergic to IDEs and tools that hide complexity and
remove control. I am a Linux-user and prefer working with a tiling window manager
(currently using Sway).

I like to work on low-level stuff with C(++), and high-level stuff in Python, and
also love Lisp. Web development is not the greatest passion of mine, allthough I
did manage to pull off this website.

On my free time I like to work on my open source "rojekti"s, which are in various
states of completeness. Those can be found on my Github page at
https://github.com/nyyManni. I also like to play with networking and server
software at my home network (ask my wife how many times our networking has
changed for "no obvious reason").

-Henrik
"""
import threading
import time
import math


YEAR = 1970


class Self:

    def __init__(self):
        YEAR = 1992
        self.name = 'Henrik Nyman'
        self.hometown = 'Hinnerjoki, Eura'
        self.email = 'h@nyymanni.com'
        self.title = None
        self.career = threading.Thread(target=self.work_experience)

    def education(self):
        YEAR = 2011
        yield Matriculation(location='Euran Lukio')

        # Military service
        YEAR = 2012
        time.sleep(180 * 24 * 3600)
        self.hometown = 'Tampere'

        YEAR = 2015
        self.career.start()

        YEAR = 2016
        yield Candidate(major='Information Technology',
                        location='Tampere University of Technology')

        YEAR = 2018
        yield MasterOfScience(major='Pervasive Systems',
                              location='Tampere University of Technology')

    def work_experience(self):
        company = 'OptoFidelity Ltd.'
        self.title = 'Software Trainee'

        YEAR = 2015
        self.countries_visited.append('China')

        self.title = 'Software Engineer'

        YEAR = 2016
        self.countries_visited.append('U.S.')

        YEAR = 2018
        self.thesis_work(company)

        YEAR = 2019
        self.title = 'Scrum Master, Software Lead'


if __name__ == '__main__':
    me = Self()
    YEAR = 1999
    for _ in me.education():
        me.party(hard=True)

    YEAR = 2019
    self.childen += 1

    YEAR = math.nan  # This generation won't get to retire...
    me.career.join()
