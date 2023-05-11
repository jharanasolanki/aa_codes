import random
import time

candidateData = [
    {
        "cgpa": 8,
        "internships": 2,
        "skills": {
            "marketingCertificates": 2,
            "codingCertificates": 1,
            "businessCertificates": 0
        },
        "experience": 2
    },
    {
        "cgpa": 8.5,
        "internships": 1,
        "skills": {
            "marketingCertificates": 2,
            "codingCertificates": 0,
            "businessCertificates": 0
        },
        "experience": 3
    }, {
        "cgpa": 7.5,
        "internships": 3,
        "skills": {
            "marketingCertificates": 0,
            "codingCertificates": 2,
            "businessCertificates": 1
        },
        "experience": 4
    },
    {
        "cgpa": 9,
        "internships": 5,
        "skills": {
            "marketingCertificates": 3,
            "codingCertificates": 2,
            "businessCertificates": 1
        },
        "experience": 1
    },
    {
        "cgpa": 8.6,
        "internships": 4,
        "skills": {
            "marketingCertificates": 4,
            "codingCertificates": 2,
            "businessCertificates": 0
        },
        "experience": 2
    },
    {
        "cgpa": 8.9,
        "internships": 5,
        "skills": {
            "marketingCertificates": 1,
            "codingCertificates": 6,
            "businessCertificates": 1
        },
        "experience": 4
    }

]

marketingCandidates = []
businessCandidates = []
codingCandidates = []

firingConstant = 100
firingConstant = 200

marketingCost = 0
codingCost = 0
businessCost = 0

# defining current candidates
currentMarketing = {
    "cgpa": 7.0,
    "internships": 3,
    "skills": {
        "marketingCertificates": 1,
        "codingCertificates": 0,
        "businessCertificates": 0
    },
    "experience": 3
}

currentBusiness = {
    "cgpa": 8.0,
    "internships": 2,
    "skills": {
        "marketingCertificates": 0,
        "codingCertificates": 0,
        "businessCertificates": 1
    },
    "experience": 5
}

currentCoding = {
    "cgpa": 8.0,
    "internships": 1,
    "skills": {
        "marketingCertificates": 0,
        "codingCertificates": 5,
        "businessCertificates": 1
    },
    "experience": 2
}


def filter_candidate(candidates):
    for candidate in candidates:
        if candidate["cgpa"] >= 9 and candidate["internships"] >= 3 and candidate["skills"]["codingCertificates"] >= 2:
            codingCandidates.append(candidate)
        elif candidate["cgpa"] >= 8.5 and candidate["internships"] >= 1 and candidate["skills"]["businessCertificates"] >= 1:
            businessCandidates.append(candidate)
        elif candidate["cgpa"] >= 8.0 and candidate["internships"] >= 2 and candidate["skills"]["marketingCertificates"] >= 3:
            marketingCandidates.append(candidate)


def firingCost(candidate):
    startTime = time.time()
    randomVal = random.uniform(0.1, 0.9)
    cost = candidate["experience"]*firingConstant*randomVal
    endTime = time.time()
    duration = endTime-startTime
    return cost, duration


def hiringCost(candidate):
    startTime = time.time()
    randomVal = random.uniform(0.1, 0.9)
    cost = candidate["experience"]*firingConstant*randomVal
    endTime = time.time()
    duration = endTime-startTime
    return cost, duration


def interview(candidates, currentCandidate):
    cost = 0
    for candidate in candidates:
        if candidate["cgpa"] > currentCandidate["cgpa"] and candidate["internships"] > currentCandidate["internships"]:
            firing, duration1 = firingCost(currentCandidate)
            hiring, duration2 = hiringCost(currentCandidate)
            cost += firing+hiring
            duration = duration1+duration2
            currentCandidate = candidate
    return cost, duration


# filter candidate according to their credibility into 3 categories
filter_candidate(candidateData)

# shuffle candidates for interview sequence
random.shuffle(codingCandidates)
random.shuffle(businessCandidates)
random.shuffle(marketingCandidates)

# calculating cost for interview
codingCost, duration1 = interview(codingCandidates, currentCoding)
businessCost, duration2 = interview(businessCandidates, currentBusiness)
marketingCost, duration3 = interview(marketingCandidates, currentMarketing)

totalCost = codingCost + businessCost + marketingCost
totalDuration = duration1+duration2+duration3

print("coding cost: ", codingCost, " Duration: ", duration1)
print("business cost: ", businessCost, " Duration: ", duration1)
print("marketing cost: ", marketingCost, " Duration: ", duration3)
print("total cost: ", totalCost, " Total Duration: ", totalDuration)
