#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Sumner Evans <sumner.evans98@gmail.com>
#
# Distributed under terms of the MIT license.

import sys

def print_matrix(matrix):
    for row in matrix:
        print('|' + ' '.join([str(x) for x in row]) + '|')

def validate_matrix(matrix):
    if len(matrix) == 0:
        return False

    n = len(matrix[0])
    for row in matrix:
        if len(row) != n:
            return False

    return True

def get_matrix():
    requires_entry = True
    while requires_entry:
        print('\nType each row of your matrix, separating the entries with a space. When you are ' +
                'finished entering your matrix, type "done".')

        matrix = []
        i = 0
        while True:
            row = input().strip()

            if row.lower() == 'done':
                break

            if len(row) == 0:
                continuesum

            # Add and populate the row
            matrix.append([int(x) for x in row.split()])

            i += 1

        requires_entry = not validate_matrix(matrix)

    return matrix

def interchange(matrix, r1, r2):
    matrix[r1], matrix[r2] = matrix[r2], matrix[r1]

def scale_matrix(matrix, r1, scale):
    matrix[r1] = [scale * c for c in matrix[r1]]

# (scale)R1 + R2 -> R2
def replace(matrix, scale, r1, r2):
    matrix[r2] = [(scale * c) + matrix[r2][i] for i, c in enumerate(matrix[r1])]

def rowreduce(matrix, start_y = 0, start_x = 0):
    pivot_found = False
    for (i, row) in enumerate(matrix):
        if i < start_y: continue

        if row[start_x] != 0:
            pivot_found = True

            # If this isn't the top already, move it to the top
            if i != start_y:
                interchange(matrix, i, start_y)

            # Make everything under the pivot a zero
            for (j, row) in enumerate(matrix):
                if j <= start_y: continue

                if row[start_x] != 0:
                    scale = - (row[start_x] / matrix[start_y][start_x])
                    replace(matrix, scale, start_x, j)

            break

    if not pivot_found and start_x < len(matrix[0]):
        rowreduce(matrix, start_y, start_x + 1)
    elif start_y < len(matrix):
        rowreduce(matrix, start_y + 1)

    if not pivot_found: return

    # Pivot Was Found
    scale_matrix(matrix, start_y, 1 / matrix[start_y][start_x])

    for (j, row) in enumerate(matrix):
        if j == start_y: return

        if row[start_x]:
            scale = -(row[start_x] / matrix[start_y][start_x])
            replace(matrix, scale, start_x, j)

print('Welcome to rowreduce')

matrix = get_matrix()

rowreduce(matrix)

print_matrix(matrix)
