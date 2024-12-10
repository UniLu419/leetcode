#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'awardTopKHotels' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING positiveKeywords
#  2. STRING negativeKeywords
#  3. INTEGER_ARRAY hotelIds
#  4. STRING_ARRAY reviews
#  5. INTEGER k
#


def awardTopKHotels(positiveKeywords, negativeKeywords, hotelIds, reviews, k):
    # Write your code here
    positiveKeywords = set(positiveKeywords.lower().split())
    negativeKeywords = set(negativeKeywords.lower().split())
    hotelScores = {}
    for hotelId, review in zip(hotelIds, reviews):
        score = 0
        words = review.lower().split()
        for word in words:
            word = word.strip(".,!?")
            if word in positiveKeywords:
                score += 3
            elif word in negativeKeywords:
                score -= 1
        if hotelId in hotelScores:
            hotelScores[hotelId] += score
        else:
            hotelScores[hotelId] = score
    sortedHotels = sorted(hotelScores.items(), key=lambda x: (-x[1], x[0]))
    topKHotels = [hotelId for hotelId, _ in sortedHotels[:k]]

    return topKHotels


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    positiveKeywords = input()

    negativeKeywords = input()

    hotelIds_count = int(input().strip())

    hotelIds = []

    for _ in range(hotelIds_count):
        hotelIds_item = int(input().strip())
        hotelIds.append(hotelIds_item)

    reviews_count = int(input().strip())

    reviews = []

    for _ in range(reviews_count):
        reviews_item = input()
        reviews.append(reviews_item)

    k = int(input().strip())

    result = awardTopKHotels(positiveKeywords, negativeKeywords, hotelIds, reviews, k)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
