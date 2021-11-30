class LongestContigPlugin:
    def input(self, filename):
       self.infile = open(filename, 'r')

    def run(self):
        self.maxheader = "NULL"
        maxlength = -1
        self.maxseq = "NULL"
        header = "NULL"
        for line in self.infile:
            line = line.strip()
            if (line.startswith('>')):
                if (header != "NULL"):
                    if (len(seq) > maxlength):
                        self.maxheader = header
                        maxlength = len(seq)
                        self.maxseq = seq
                seq = ""
                header = line
            else:
                seq += line

    def output(self, filename):
        outfile = open(filename, 'w')
        outfile.write(self.maxheader+"\n")
        outfile.write(self.maxseq)
