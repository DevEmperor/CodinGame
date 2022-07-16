w, h = [int(i) for i in input().split()]
dwe = input().split()
image = "".join(" "*int(dwe[x+1]) if dwe[x] == "W" else "x"*int(dwe[x+1]) for x in range(0, len(dwe), 2))  # parse image
image = [image[x:x+w] for x in range(0, len(image), w)]  # rotate image

note, notes, stub = [], [], ""
for x in range(w):  # go through every vertical line
    line = "".join(image[y][x] for y in range(h))[::-1]

    if "x" in line:  # check if notation has started
        if stub == "":  # initialize stub only once to compare with lines that include notes
            stub = line[line.index("x"):line[line.index("x"):].index(" x") + line.index("x") + 1]
            first_line = line
        if line.strip() in [(stub*5).strip(), (stub*6).strip()]:  # if there aren't notes in the current line...
            if len(note) > 0:  # ...check if a note is in cache and continue with recognition
                mid = note[len(note) // 2]
                longest = max(mid.split(), key=len)
                if len(longest) > sum(len(p) for p in mid.split() if p != longest) and not all(p == mid.split()[0] for p in mid.split()):  # quarter note
                    duration = "Q"
                else:  # half note
                    notehead_top = max([i for i in range(len(mid)) if mid[i] == "x" and first_line[i] != "x"])
                    space = mid[:notehead_top][::-1].index(" x") + 1
                    mid = mid[:notehead_top - space] + "x"*space + mid[notehead_top:]
                    duration = "H"
                longest = max(mid.split(), key=len)
                mid_len = len(mid.split())
                note_idx = mid.split().index(longest)
                if mid_len == 6: pitch = "C"
                elif len(mid.split()[0]) == len(longest) and mid.count(stub) == 5: pitch = "D"
                elif note_idx == 0: pitch = "E" if mid_len == 5 else "F"
                elif note_idx == 1: pitch = "G" if mid_len == 5 else "A"
                elif note_idx == 2: pitch = "B" if mid_len == 5 else "C"
                elif note_idx == 3: pitch = "D" if mid_len == 5 else "E"
                elif len(mid.split()[4]) == len(longest) and stub*4 not in mid: pitch = "F"
                else: pitch = "G"
                notes.append(pitch + duration)
                note = []
        else:  # else append the current line to the current note
            note.append(line)
print(*notes, sep=" ")
