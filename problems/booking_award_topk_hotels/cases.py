METHOD = "awardTopKHotels"

CASES = [
    dict(
        args=(
            "breakfast beach citycenter location metro view staff price",
            "not",
            [1, 2, 1, 1, 2],
            [
                "This hotel has a nice view of the citycenter. The location is perfect.",
                "The breakfast is ok. Regarding location, it is quite far from citycenter but price is cheap so it is worth.",
                "Location is excellent and 5 minutes from citycenter. There is also a metro station very close to the hotel.",
                "They said I couldn't take my dog and there were other guests with dogs! That is not fair.",
                "Very friendly staff and good cost-benefit ratio. Its location is a bit far from citycenter.",
            ],
            2,
        ),
        expected=[2, 1],
    ),
    dict(args=("good", "bad", [5, 3], ["good", "Good!"], 2), expected=[3, 5]),
    dict(args=("clean", "dirty noisy", [1, 2, 3], ["dirty and noisy", "clean", "nothing special"], 2), expected=[2, 3]),
    dict(args=("clean", "dirty", [7, 7], ["clean", "clean"], 3), expected=[7]),
    dict(args=("good", "bad", [1, 2], ["goodness", "bad"], 1), expected=[1]),
]
