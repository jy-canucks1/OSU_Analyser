import fileinput


class BmsInfo:

    def __init__(self, f):
        self.fileinput = fileinput.input(files=f)
        self.fileinput1 = fileinput.input(files=f)
        self.fileinput2 = fileinput.input(files=f)
        self.fileinput3 = fileinput.input(files=f)
        self.fileinput4 = fileinput.input(files=f)
        self.infolist = []
        self.timing_list = []
        self.note_list = []
        self.note1_list = []
        self.note2_list = []
        self.note3_list = []
        self.note4_list = []

# information about title, artist, map creator, version, difficulty
    def info(self):
        for line in self.fileinput:
            i = 0
            str_input = line
            if str_input[0] != '[':
                while str_input[i] != ':':
                    if str_input[i] == '\n':
                        break
                    i += 1
                str_1 = str_input[0:i]
                str_2 = str_input[(i + 1):(len(str_input) - 1)]
                if str_1 == 'Title':
                    self.infolist.append([str_1, str_2])
                if str_1 == 'Artist':
                    self.infolist.append([str_1, str_2])
                if str_1 == 'Creator':
                    self.infolist.append([str_1, str_2])
                if str_1 == 'Version':
                    self.infolist.append([str_1, str_2])
                if str_1 == 'OverallDifficulty':
                    self.infolist.append([str_1, str_2])
                    return self.infolist

# information of timingPoints. each start of new bpm(mpb here)
    def spd_info(self):
        flag = 0
        for line in self.fileinput:
            i = 0
            str_input = line
            if str_input == '[TimingPoints]\n':
                flag = 1
                continue
            if flag == 1 and str_input == '\n':
                break
            if flag == 1:
                j = 0
                cnt = 0
                new_list = [0, 0]
                while cnt < 2:
                    if str_input[i] == ',':
                        cnt += 1
                        str_target = str_input[j:i]
                        if cnt == 1:
                            new_list[0] = int(str_target)
                            j = i + 1
                            i += 2
                        if cnt == 2:
                            interval = float(str_target)
                            if interval < 0:
                                interval = self.timing_list[len(self.timing_list) - 1][1] * (-100/interval)
                            new_list[1] = interval
                    i += 1
                self.timing_list.append(new_list)
        return self.timing_list

# information of all note : start_time // key / end_time(if it is slider)
    def note_info(self):
        flag = 0
        for line in self.fileinput:
            i = 0
            str_input = line
            if str_input == '[HitObjects]\n':
                flag = 1
                continue
            if flag == 1 and str_input == '\n':
                break
            if flag == 1:
                j = 0
                cnt = 0
                k = 0
                new_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                while str_input[i] != ':':
                    i += 1
                    if str_input[i] == ',':
                        cnt += 1
                        str_target = str_input[j:i]
                        if cnt == 1 and int(str_target) // 128 == 0:
                            new_list[1] = 1
                            k = 1
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 1:
                            new_list[3] = 1
                            k = 3
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 2:
                            new_list[5] = 1
                            k = 5
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 3:
                            new_list[7] = 1
                            k = 7
                            j = i + 1
                        elif cnt == 2 or cnt == 4 or cnt == 5:
                            j = i + 1
                        elif cnt == 3:
                            new_list[0] = int(str_target)
                            j = i + 1
                new_list[k + 1] = int(str_input[j:i])
                current_len = len(self.note_list)
                if current_len > 0 and new_list[0] == self.note_list[current_len - 1][0]:
                    for x in range(1, 9):
                        self.note_list[len(self.note_list) - 1][x] += new_list[x]
                else:
                    self.note_list.append(new_list)
        return self.note_list

# inforamtion of note 1 / start_time / end_time(if it is slider)
    def note1_info(self):
        flag = 0
        for line in self.fileinput1:
            i = 0
            str_input = line
            if str_input == '[HitObjects]\n':
                flag = 1
                continue
            if flag == 1 and str_input == '\n':
                break
            if flag == 1:
                j = 0
                cnt = 0
                k = 0
                while str_input[i] != ':':
                    i += 1
                    if str_input[i] == ',':
                        cnt += 1
                        str_target = str_input[j:i]
                        if cnt == 1 and int(str_target) // 128 == 0:
                            k = 1
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 1:
                            k = 2
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 2:
                            k = 3
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 3:
                            k = 4
                            j = i + 1
                        elif cnt == 2 or cnt == 4 or cnt == 5:
                            j = i + 1
                        elif cnt == 3:
                            if k == 1:
                                self.note1_list.append(int(str_target))
                            j = i + 1
                if k == 1:
                    self.note1_list.append(int(str_input[j:i]))
        return self.note1_list

# inforamtion of note 2 / start_time / end_time(if it is slider)
    def note2_info(self):
        flag = 0
        for line in self.fileinput2:
            i = 0
            str_input = line
            if str_input == '[HitObjects]\n':
                flag = 1
                continue
            if flag == 1 and str_input == '\n':
                break
            if flag == 1:
                j = 0
                cnt = 0
                k = 0
                while str_input[i] != ':':
                    i += 1
                    if str_input[i] == ',':
                        cnt += 1
                        str_target = str_input[j:i]
                        if cnt == 1 and int(str_target) // 128 == 0:

                            k = 1
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 1:
                            k = 2
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 2:
                            k = 3
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 3:
                            k = 4
                            j = i + 1
                        elif cnt == 2 or cnt == 4 or cnt == 5:
                            j = i + 1
                        elif cnt == 3:
                            if k == 2:
                                self.note2_list.append(int(str_target))
                            j = i + 1
                if k == 2:
                    self.note2_list.append(int(str_input[j:i]))

        return self.note2_list

# inforamtion of note 3 / start_time / end_time(if it is slider)
    def note3_info(self):
        flag = 0
        for line in self.fileinput3:
            i = 0
            str_input = line
            if str_input == '[HitObjects]\n':
                flag = 1
                continue
            if flag == 1 and str_input == '\n':
                break
            if flag == 1:
                j = 0
                cnt = 0
                k = 0
                while str_input[i] != ':':
                    i += 1
                    if str_input[i] == ',':
                        cnt += 1
                        str_target = str_input[j:i]
                        if cnt == 1 and int(str_target) // 128 == 0:
                            k = 1
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 1:
                            k = 2
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 2:
                            k = 3
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 3:
                            k = 4
                            j = i + 1
                        elif cnt == 2 or cnt == 4 or cnt == 5:
                            j = i + 1
                        elif cnt == 3:
                            if k == 3:
                                self.note3_list.append(int(str_target))
                            j = i + 1
                if k == 3:
                    self.note3_list.append(int(str_input[j:i]))
        return self.note3_list

# inforamtion of note 4 / start_time / end_time(if it is slider)
    def note4_info(self):
        flag = 0
        for line in self.fileinput4:
            i = 0
            str_input = line
            if str_input == '[HitObjects]\n':
                flag = 1
                continue
            if flag == 1 and str_input == '\n':
                break
            if flag == 1:
                j = 0
                cnt = 0
                k = 0
                while str_input[i] != ':':
                    i += 1
                    if str_input[i] == ',':
                        cnt += 1
                        str_target = str_input[j:i]
                        if cnt == 1 and int(str_target) // 128 == 0:
                            k = 1
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 1:
                            k = 2
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 2:
                            k = 3
                            j = i + 1
                        elif cnt == 1 and int(str_target) // 128 == 3:
                            k = 4
                            j = i + 1
                        elif cnt == 2 or cnt == 4 or cnt == 5:
                            j = i + 1
                        elif cnt == 3:
                            if k == 4:
                                self.note4_list.append(int(str_target))
                            j = i + 1
                if k == 4:
                    self.note4_list.append(int(str_input[j:i]))
        return self.note4_list
