class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        p1 = 0
        p2 = 0
        line_w = 0
        res = []

        while p2 < len(words):
            line_w = line_w + len(words[p2])
            # no. of min white space, at least one b/w each word
            min_spaces = p2 - p1
            # line width with min spaces
            line_w_spaces = line_w + min_spaces

            if line_w_spaces > maxWidth:
                # excluding words at p2, since including it is how we got line_w_spaces > maxWidth
                spaces = maxWidth - prev_w
                line = ""
                gaps = p2-p1-1

                if(gaps == 0):
                    line = words[p1] + " "*spaces
                else:
                    for i in reversed(range(p1, p2)):
                        if i != p1:
                            gap_space = spaces//gaps
                            line = " "*gap_space + words[i] + line
                            # the gap_spaces we just used
                            spaces = spaces - gap_space
                            # one gap is filled
                            gaps = gaps - 1
                        else:
                            # for the first word of line
                            line = words[i] + line

                res.append(line)
                p1 = p2
                line_w = 0

            else:
                prev_w = line_w
                p2 = p2 + 1

        # for the last line
        line = ""
        for i in range(p1, p2-1):
            line = line + words[i] + " "

        line = line + words[p2-1]
        s_add = maxWidth - len(line)
        line = line + " "*s_add
        res.append(line)

        return res
