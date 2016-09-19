#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Sumner Evans <sumner.evans98@gmail.com>
#
# Distributed under terms of the MIT license.

from fractions import Fraction

class Matrix:
    def __init__(self, data=None):
        self.data = data

    def __getitem__(self, arg):
        return self.data[arg]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for row in self.data:
            yield row

    def print(self):
        for row in self.data:
            print('|' + ' '.join([str(round(x, 5)) for x in row]) + '|')

    def validate(self):
        if len(self.data) == 0: return False

        n = len(self.data[0])
        for row in self.data:
            if len(row) != n: return False

        return True

    def is_square(self):
        return len(self.data) == len(self.data[0])

    def interchange(self, r1, r2):
        self.data[r1], self.data[r2] = self.data[r2], self.data[r1]

    def scale(self, r1, scale):
        self.data[r1] = [Fraction(scale * c) for c in self.data[r1]]

    # (scale)R1 + R2 -> R2
    def replace(self, scale, r1, r2):
        self.data[r2] = [Fraction((scale * c) + self.data[r2][i]) for i, c in enumerate(self.data[r1])]

    def prompt_for_matrix(self, prompt_text, requires_square=False):
        requires_entry = True
        while requires_entry:
            print('\n%s' % prompt_text)

            self.data = []
            i = 0
            while True:
                row = input().strip()

                if row.lower() == 'done': break

                if len(row) == 0: continue

                # Add and populate the row
                self.data.append([Fraction(x) for x in row.split()])

                i += 1

            requires_entry = not self.validate() or (requires_square and not self.is_square())
