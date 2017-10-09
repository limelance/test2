#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def indexreshape(n, m):
    """
    separates n indexes in m equal disjoint parts, trims edges equally
    returns tuple ((1_start_idx, 1_end_idx),...,(m_start_idx, m_end_idx))
    """
    if n < m:
        raise ValueError('m must be lower or equal to n')

    delta = (n % m) // 2
    end = n - (n % m)
    step = end // m
    r = tuple((i + delta, i + delta + step - 1) for i in range(0, end, step))
    return r


if __name__ == '__main__':
    try:
        length = int(input("enter N = "))
        parts = int(input("enter number of parts M = "))
        print(indexreshape(length, parts))
    except ValueError or TypeError as e:
        print('Error: incorrect input: %s' % str(e))
        exit()
