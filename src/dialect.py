#-*- coding: cp949-*-

import re
from BaseHTMLProcessor import BaseHTMLProcessor

class Dialectizer(BaseHTMLProcessor):
    subs = ()

    def reset(self):
        # 확장 (조상의 __init__ 메쏘드로부터 호출된다)
        # 모든 데이터 속성을 초기화한다.
        self.verbatim = 0
        BaseHTMLProcessor.reset(self)

    def start_pre(self, attrs):            
        # HTML 소스에서 <pre> 태그마다 호출됨.
        # verbatim 모드 횟수를 증가시키고, 평소처럼 태그를 처리한다.
        self.verbatim += 1                 
        self.unknown_starttag("pre", attrs)

    def end_pre(self):                     
        # HTML 소스에서 </pre> 태그마다 호출됨.
        # verbatim 모드 횟수를 감소시킨다.
        self.unknown_endtag("pre")         
        self.verbatim -= 1                 

    def handle_data(self, text):                                        
        # 오버라이드한다.
        # HTML 소스에서 텍스트 블록마다 호출됨.
        # verbatim 모드에 있다면, 텍스트를 그대로 저장한다;
        # 그렇지 않으면 순서대로 교체하면서 텍스트를 처리한다.
        self.pieces.append(self.verbatim and text or self.process(text))

    def process(self, text):
        # handle_data으로부터 호출된다.
        # 일련의 정규 표현식 교체를 수행함으로써 텍스트 블록을 처리한다.
        # (실제로 교체하는 일은 자손에 정의된다)
        for fromPattern, toPattern in self.subs:
            text = re.sub(fromPattern, toPattern, text)
        return text

class ChefDialectizer(Dialectizer):
    """HTML을 스웨덴 주방장식-화법으로 변환한다.
    
    다음에 기반함 chef.x, copyright (c) 1992, 1993 John Hagerman
    """
    subs = ((r'a([nu])', r'u\1'),
            (r'A([nu])', r'U\1'),
            (r'a\B', r'e'),
            (r'A\B', r'E'),
            (r'en\b', r'ee'),
            (r'\Bew', r'oo'),
            (r'\Be\b', r'e-a'),
            (r'\be', r'i'),
            (r'\bE', r'I'),
            (r'\Bf', r'ff'),
            (r'\Bir', r'ur'),
            (r'(\w*?)i(\w*?)$', r'\1ee\2'),
            (r'\bow', r'oo'),
            (r'\bo', r'oo'),
            (r'\bO', r'Oo'),
            (r'the', r'zee'),
            (r'The', r'Zee'),
            (r'th\b', r't'),
            (r'\Btion', r'shun'),
            (r'\Bu', r'oo'),
            (r'\BU', r'Oo'),
            (r'v', r'f'),
            (r'V', r'F'),
            (r'w', r'w'),
            (r'W', r'W'),
            (r'([a-z])[.]', r'\1.  Bork Bork Bork!'))

class FuddDialectizer(Dialectizer):
    """HTML을 엘머 퍼드(Elmer Fudd)-화법으로 변환한다"""
    subs = ((r'[rl]', r'w'),
            (r'qu', r'qw'),
            (r'th\b', r'f'),
            (r'th', r'd'),
            (r'n[.]', r'n, uh-hah-hah-hah.'))

class OldeDialectizer(Dialectizer):
    """HTML을 중세 영어를 흉내내도록 변환한다"""
    subs = ((r'i([bcdfghjklmnpqrstvwxyz])e\b', r'y\1'),
            (r'i([bcdfghjklmnpqrstvwxyz])e', r'y\1\1e'),
            (r'ick\b', r'yk'),
            (r'ia([bcdfghjklmnpqrstvwxyz])', r'e\1e'),
            (r'e[ea]([bcdfghjklmnpqrstvwxyz])', r'e\1e'),
            (r'([bcdfghjklmnpqrstvwxyz])y', r'\1ee'),
            (r'([bcdfghjklmnpqrstvwxyz])er', r'\1re'),
            (r'([aeiou])re\b', r'\1r'),
            (r'ia([bcdfghjklmnpqrstvwxyz])', r'i\1e'),
            (r'tion\b', r'cioun'),
            (r'ion\b', r'ioun'),
            (r'aid', r'ayde'),
            (r'ai', r'ey'),
            (r'ay\b', r'y'),
            (r'ay', r'ey'),
            (r'ant', r'aunt'),
            (r'ea', r'ee'),
            (r'oa', r'oo'),
            (r'ue', r'e'),
            (r'oe', r'o'),
            (r'ou', r'ow'),
            (r'ow', r'ou'),
            (r'\bhe', r'hi'),
            (r've\b', r'veth'),
            (r'se\b', r'e'),
            (r"'s\b", r'es'),
            (r'ic\b', r'ick'),
            (r'ics\b', r'icc'),
            (r'ical\b', r'ick'),
            (r'tle\b', r'til'),
            (r'll\b', r'l'),
            (r'ould\b', r'olde'),
            (r'own\b', r'oune'),
            (r'un\b', r'onne'),
            (r'rry\b', r'rye'),
            (r'est\b', r'este'),
            (r'pt\b', r'pte'),
            (r'th\b', r'the'),
            (r'ch\b', r'che'),
            (r'ss\b', r'sse'),
            (r'([wybdp])\b', r'\1e'),
            (r'([rnt])\b', r'\1\1e'),
            (r'from', r'fro'),
            (r'when', r'whan'))

def translate(url, dialectName="chef"):
    """URL을 가져와서 사투리로 번역한다.
    
    dialect in ("chef", "fudd", "olde")"""
    import urllib                      
    sock = urllib.urlopen(url)         
    htmlSource = sock.read()           
    sock.close()                       
    parserName = "%sDialectizer" % dialectName.capitalize()
    parserClass = globals()[parserName]                    
    parser = parserClass()                                 
    parser.feed(htmlSource)
    parser.close()         
    return parser.output() 

def test(url):
    """URL에 대하여 모든 사투리를 테스트한다"""
    for dialect in ("chef", "fudd", "olde"):
        outfile = "%s.html" % dialect
        fsock = open(outfile, "wb")
        fsock.write(translate(url, dialect))
        fsock.close()
        import webbrowser
        webbrowser.open_new(outfile)

if __name__ == "__main__":
    test("http://diveintopython.org/odbchelper_list.html")