#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Sumner Evans <sumner.evans98@gmail.com>
#
# Distributed under terms of the MIT license.

import sys
from matrix import Matrix

def determinant(matrix):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i, col in enumerate(matrix[0]):
        m = Matrix([row[:i] + row[i + 1:] for row in matrix[1:]])

        if i % 2 == 1:
            det -= col * determinant(m)
        else:
            det += col * determinant(m)

    return det

print('Welcome to determinant')

matrix = Matrix()

matrix.prompt_for_matrix('Type each row of your matrix, separating the entries with a space. ' +
        'When you are finished entering your matrix, type "done".', requires_square=True)

print(determinant(matrix))
