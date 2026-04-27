class Solution:

    def encode(self, strs: List[str]) -> str:
        a = "";
        for s in strs:
            a+=str(len(s)).zfill(4);
            a += ",";
            a += s;
            a += ",";

        return a;

    def decode(self, s: str) -> List[str]:
        a = [];
        while s:
            chunk, s = s[0:4], s[5:];
            c = int(chunk);
            b, s = s[:c], s[c:];
            a.append(b);
            if(s[:1] == ","):
                s = s[1:];


        return a;