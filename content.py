#!/usr/bin/env python
"""
Welcome to www.nyymanni.com

Size of this webpage is 68 kB, of which 56 kB is due to  the background image.
I like small websites.
"""
import threading
import time


class Self:

    name = 'Henrik Nyman'
    email = 'henrikjohannesnyman@gmail.com'

    def education(self):
        year = 2011
        yield Matriculation(location='Euran Lukio')

        # Military service
        year = 2012
        time.sleep(180 * 24 * 3600)

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
        title = 'Software Engineer'
