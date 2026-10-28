class Solution:
    def awardTopKHotels(self, positiveKeywords, negativeKeywords, hotelIds, reviews, k):
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
