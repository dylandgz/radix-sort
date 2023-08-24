# Radix Sort with Unstable Sorting Subroutine

## Introduction

This repository contains the source code for an empirical study on the modification of the radix sort algorithm by replacing its stable sorting subroutine with an unstable one. The goal of this study is to investigate the impact of this modification on the correctness, performance, and limitations of the radix sort algorithm.

## Radix Sort Overview

Radix sort is a non-comparative sorting algorithm that sorts numbers digit by digit. It can be implemented from the least significant digit (LSD) to the most significant digit (MSD) or vice versa. The algorithm uses a stable sorting subroutine to sort integers based on individual digits. The stable nature of the subroutine ensures that elements with equal keys maintain their relative order.

The original radix sort primarily uses counting sort as the stable sorting subroutine due to its efficiency and linear time complexity. This efficiency is crucial when dealing with integers in base 10, where each digit ranges from 0 to 9. Radix sort's time complexity depends on the complexity of the subroutine algorithm and can achieve linear time when sorting fixed-size integers.

## Proposed Modification

The main focus of this study is on the modification of radix sort, where the stable sorting subroutine is replaced with an unstable one. This modification aims to explore the impact on correctness, performance, and trade-offs. The chosen unstable sorting algorithm significantly influences the performance of the modified radix sort. In the provided code, quicksort is used as the unstable sorting subroutine.

## Conclusion

The modified radix sort algorithm with an unstable sorting subroutine offers insights into the mechanics of radix sort and its trade-offs between stability, time complexity, and memory usage. While this modification has the potential to optimize performance in specific scenarios, it comes with limitations, especially in terms of correctness when dealing with equal keys.
