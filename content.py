#!/usr/bin/env python
"""
Welcome to www.nyymanni.com

Size of this webpage is 28 kB, including the background image.
I like small websites.
"""
import threading
import time
from datetime import datetime
import random


class Self:

    def __init__(self):
        year = 1992
        self.name = 'Henrik Nyman'
        self.hometown = 'Hinnerjoki, Eura'
        self.email = 'henrikjohannesnyman@gmail.com'

    def education(self):
        year = 2011
        yield Matriculation(location='Euran Lukio')

        # Military service
        year = 2012
        time.sleep(180 * 24 * 3600)
        self.hometown = 'Tampere'

        year = 2015
        threading.Thread(target=self.work_experience).start()

        year = 2016
        yield Candidate(major='Information Technology',
                        location='Tampere University of Technology')

        year = 2018
        yield MasterOfScience(major='Pervasive Systems',
                              location='Tampere University of Technology')

    def work_experience(self):
        company = 'OptoFidelity Ltd.'
        title = 'Software Trainee'

        year = 2015
        self.countries_visited.append('China')

        title = 'Software Engineer'

        year = 2016
        self.countries_visited.append('U.S.')

        year = datetime.now().year
        while True:
            self.work(company)
            self.masters_thesis(company)
            time.sleep(random.randint(5 * 3600, 8 * 3600))
