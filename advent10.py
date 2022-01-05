
def complete_and_calc_score(chunks):
    total_points = 0
    expected_endings = list()
    for c in chunks:
        if c in corresponding_endings.keys():
            expected_endings.append(corresponding_endings[c])
        else:
            expected_endings.pop()
    for c in reversed(expected_endings):
        total_points *= 5
        total_points += closing[c]
    return total_points

def verify_chunks(chunks):
    expected_endings = list()
    for c in chunks:
        if c in corresponding_endings.keys():
            expected_endings.append(corresponding_endings[c])
        else:
            expected_chunk_ending = expected_endings.pop()
            if c != expected_chunk_ending:
                return scores[c]
    return 0

if __name__ == '__main__':
    file1 = open("input10.txt", "r")
    chunk = file1.read().split()
    openning = ["[","{","(","<"]
    closing = {")" : 1,
                   "]" : 2,
                   "}" : 3,
                   ">" : 4}
    corresponding_endings = {"(" : ")", 
                         "[" : "]",
                         "<" : ">",
                         "{" : "}"}
    scores = {")" : 3,
                  "]" : 57,
                  "}" : 1197,
                  ">" : 25137}
    print(sum([verify_chunks(chunks) for chunks in chunk]))
    incomplete_chunks = [chunks for chunks in chunk if verify_chunks(chunks) == 0]
    newscores = sorted([complete_and_calc_score(chunks) for chunks in incomplete_chunks])
    print(newscores[int(len(newscores) / 2 )])

