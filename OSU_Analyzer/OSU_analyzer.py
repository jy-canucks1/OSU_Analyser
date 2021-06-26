import bms_reader

song_info1 = bms_reader.BmsInfo('bms/Kishida Kyoudan & The Akeboshi Rockets - STRIKE THE BLOOD ([GraveChaos]) [4K MX].osu.txt') # << this is sample file. input your file.

outF = open("results/Analyzed_result.txt", "w")
outF1 = open("results/note1_timeline.txt", "w")
outF2 = open("results/note2_timeline.txt", "w")
outF3 = open("results/note3_timeline.txt", "w")
outF4 = open("results/note4_timeline.txt", "w")

# write info in 'Analyzed_result.txt'
for line in song_info1.info():
    for data in line:
        outF.write(str(data) + ' ')
    outF.write('\n')
outF.write("TimingPoint / millisecond per 1 beat")
outF.write('\n')
for line in song_info1.spd_info():
    for data in line:
        outF.write(str(data) + ' ')
    outF.write('\n')

outF.write('\n')
outF.write('Unit: millisecond')
outF.write('\n')
outF.write("Time / key1 / End_time(1) / key2 / End_time(2) / key3 / End_time(3) / key4 / End_time(4)")
outF.write('\n\n')
for line in song_info1.note_info():
    for data in line:
        outF.write(str(data) + ' ')
    outF.write('\n\n')

# write key1 info in 'note1_timeline.txt'
outF1.write("Time/End_time")
outF1.write('\n\n')
cnt1 = 0
for line in song_info1.note1_info():
    cnt1 += 1
    outF1.write(str(line))
    if cnt1 % 2 == 0:
        outF1.write("\n")
        outF1.write("\n")
    else:
        outF1.write("\n")

# write key2 info in 'note2_timeline.txt'
outF2.write("Time/End_time")
outF2.write('\n\n')

cnt2 = 0
for line in song_info1.note2_info():
    cnt2 += 1
    outF2.write(str(line))
    if cnt2 % 2 == 0:
        outF2.write("\n")
        outF2.write("\n")
    else:
        outF2.write("\n")

# write key3 info in 'note3_timeline.txt'
outF3.write("Time/End_time")
outF3.write("\n\n")
cnt3 = 0
for line in song_info1.note3_info():
    cnt3 += 1
    outF3.write(str(line))
    if cnt3 % 2 == 0:
        outF3.write("\n")
        outF3.write("\n")
    else:
        outF3.write("\n")

# write key4 info in 'note4_timeline.txt'
outF4.write("Time/End_time")
outF4.write("\n\n")
cnt4 = 0
for line in song_info1.note4_info():
    cnt4 += 1
    outF4.write(str(line))
    if cnt4 % 2 == 0:
        outF4.write("\n")
        outF4.write("\n")
    else:
        outF4.write("\n")

outF.close()
outF1.close()
outF2.close()
outF3.close()
outF4.close()
