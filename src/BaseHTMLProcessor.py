#-*- coding: cp949-*-
'''
Created on 2012. 6. 28.

@author: user
'''

from sgmllib import SGMLParser
import htmlentitydefs

class BaseHTMLProcessor(SGMLParser):
    def reset(self):                       
        # 확장한다 (SGMLParser.__init__에서 호출)
        self.pieces = []
        SGMLParser.reset(self)

    def unknown_starttag(self, tag, attrs):
        # 시작 태그마다 호출됨.
        # attrs는 (attr, value) 터플로 구성된 리스트이다.
        # 예를 들어, <pre class="screen">이라면 tag="pre", attrs=[("class", "screen")]이다.
        # 이상적으로 원래 태그와 속성을 재구성하고 싶지만,
        # 소스 문서에서 인용부호 처리되지 않은 속성 값을 처리해야 하거나,
        # 또는 속성 값 주위의 인용부호 종류를 바꿀 수도 있다.
        # (홑따옴표를 겹따옴표로 말이다.)
        # (클라이언트-쪽 자바스크립트처럼) HTML-아닌 코드가 부적절하게 임베드되어 있으면,
        # 조상 메쏘드에 의하여 올바르지 않게 해석될 수 있어서, 
        # 실행시간 스크립트 에러가 야기될 수 있다.
        # HTML-아닌 코드는 모두 HTML 주석 태그 (<!-- code -->) 안에 싸 넣어서,
        # 이 해석기를 (handle_comment 안을) 그대로 통과하는지 확인해야 한다.
        strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrs])
        self.pieces.append("<%(tag)s%(strattrs)s>" % locals())

    def unknown_endtag(self, tag):         
        # 끝 태그마다 호출됨. 예를 들어 </pre>이라면, 태그는 "pre"가 될 것이다.
        # 원래 끝 태그를 재구성한다.
        self.pieces.append("</%(tag)s>" % locals())

    def handle_charref(self, ref):         
        # 문자 참조마다 호출됨. 예를 들어, "&#160;"이라면, ref는 "160"이 될 것이다.
        # 원래 문자 참조를 재구성한다.
        self.pieces.append("&#%(ref)s;" % locals())

    def handle_entityref(self, ref):       
        # 개체 참조마다 호출됨. 예를 들어 "&copy;"이라면, ref는 "copy"가 될 것이다.
        # 원래 개체 참조를 재구성한다.
        self.pieces.append("&%(ref)s" % locals())
        # 표준 HTML 개체는 쌍반점으로 끝난다; 다른 개체들은 그렇지 않다.
        if htmlentitydefs.entitydefs.has_key(ref):
            self.pieces.append(";")

    def handle_data(self, text):           
        # 평범한 텍스트 블록마다 호출됨. 다시 말해, 태그의 바깥에 있으며, 
        # 문자 참조나 개체 참조가 포함되지 않는다.
        # 원래 텍스트를 그냥 그대로 저장한다.
        self.pieces.append(text)

    def handle_comment(self, text):        
        # HTML 주석마다 호출됨. 예, <!-- insert Javascript code here -->
        # 원래 주석을 재구성한다.
        # 소스 문서에서 주석에 (자바스크립트 같은) 클라이언트-쪽 코드가 담겨 있어서, 
        # 이 처리기를 그대로 통과시키려면 특히 중요하다;
        # 자세한 것은 unknown_starttag에 있는 주석을 참고하라.
        self.pieces.append("<!--%(text)s-->" % locals())

    def handle_pi(self, text):             
        # 처리 지시어마다 호출됨. 예, <?instruction>
        # 원래 처리 지시어를 재구성한다.
        self.pieces.append("<?%(text)s>" % locals())

    def handle_decl(self, text):
        # 존재한다면, DOCTYPE에 대하여 호출됨. 예,
        # <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        #     "http://www.w3.org/TR/html4/loose.dtd">
        # 원래 DOCTYPE을 재구성한다
        self.pieces.append("<!%(text)s>" % locals())

    def output(self):              
        """처리된 HTML을 문자열 하나로 돌려준다"""
        return "".join(self.pieces)