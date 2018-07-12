#!/usr/bin/env python
"""
Welcome to www.nyymanni.com

Size of this webpage is 68 kB, of which 56 kB is due to  the background image.
I like small websites.
"""


class Self:

    name = 'Henrik Nyman'
    email = 'henrikjohannesnyman@gmail.com'

    def education(self):
        year = 2011
        yield Matriculation(location='Euran Lukio')

        year = 2016
        yield Candidate(major='Information Technology',
                        location='Tampere University of Technology')

        year = 2018
        yield MasterOfScience(major='Pervasive Systems',
                              location='Tampere University of Technology')
