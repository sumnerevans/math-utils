#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Sumner Evans <sumner.evans98@gmail.com>
#
# Distributed under terms of the MIT license.

import sys
from matrix import Matrix

def rowreduce(matrix, start_y = 0, start_x = 0):
    pivot_found = False
    for (i, row) in enumerate(matrix):
        if i < start_y: continue

        if row[start_x] != 0:
            pivot_found = True

            # If this isn't the top already, move it to the top
            if i != start_y:
                matrix.interchange(i, start_y)

            matrix.print()
            print()

            # Make everything under the pivot a zero
            for (j, row) in enumerate(matrix):
                if j <= start_y: continue

                if row[start_x] != 0:
                    scale = - (row[start_x] / matrix[start_y][start_x])
                    matrix.replace(scale, start_x, j)

            matrix.print()
            print()

            break

    if not pivot_found and start_x < len(matrix[0]) - 1:
        rowreduce(matrix, start_y, start_x + 1)
    elif start_y < len(matrix) - 1:
        rowreduce(matrix, start_y + 1)

    if not pivot_found: return

    # Pivot Was Found
    if matrix[start_y][start_x] != 0:
        matrix.scale(start_y, 1 / matrix[start_y][start_x])

    for (j, row) in enumerate(matrix):
        if j == start_y: return

        if row[start_x]:
            scale = -(row[start_x] / matrix[start_y][start_x])
            matrix.replace(scale, start_x, j)

    matrix.print()
    print()

print('Welcome to rowreduce')

matrix = Matrix()

matrix.prompt_for_matrix('Type each row of your matrix, separating the entries with a space. ' +
        'When you are finished entering your matrix, type "done".')

rowreduce(matrix)

matrix.print()
