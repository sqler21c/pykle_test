#-*- coding: cp949-*-
'''
Created on 2012. 6. 28.

@author: user
'''

from sgmllib import SGMLParser
import htmlentitydefs

class BaseHTMLProcessor(SGMLParser):
    def reset(self):                       
        # Ȯ���Ѵ� (SGMLParser.__init__���� ȣ��)
        self.pieces = []
        SGMLParser.reset(self)

    def unknown_starttag(self, tag, attrs):
        # ���� �±׸��� ȣ���.
        # attrs�� (attr, value) ���÷� ������ ����Ʈ�̴�.
        # ���� ���, <pre class="screen">�̶�� tag="pre", attrs=[("class", "screen")]�̴�.
        # �̻������� ���� �±׿� �Ӽ��� �籸���ϰ� ������,
        # �ҽ� �������� �ο��ȣ ó������ ���� �Ӽ� ���� ó���ؾ� �ϰų�,
        # �Ǵ� �Ӽ� �� ������ �ο��ȣ ������ �ٲ� ���� �ִ�.
        # (Ȭ����ǥ�� �����ǥ�� ���̴�.)
        # (Ŭ���̾�Ʈ-�� �ڹٽ�ũ��Ʈó��) HTML-�ƴ� �ڵ尡 �������ϰ� �Ӻ���Ǿ� ������,
        # ���� �޽�忡 ���Ͽ� �ùٸ��� �ʰ� �ؼ��� �� �־, 
        # ����ð� ��ũ��Ʈ ������ �߱�� �� �ִ�.
        # HTML-�ƴ� �ڵ�� ��� HTML �ּ� �±� (<!-- code -->) �ȿ� �� �־,
        # �� �ؼ��⸦ (handle_comment ����) �״�� ����ϴ��� Ȯ���ؾ� �Ѵ�.
        strattrs = "".join([' %s="%s"' % (key, value) for key, value in attrs])
        self.pieces.append("<%(tag)s%(strattrs)s>" % locals())

    def unknown_endtag(self, tag):         
        # �� �±׸��� ȣ���. ���� ��� </pre>�̶��, �±״� "pre"�� �� ���̴�.
        # ���� �� �±׸� �籸���Ѵ�.
        self.pieces.append("</%(tag)s>" % locals())

    def handle_charref(self, ref):         
        # ���� �������� ȣ���. ���� ���, "&#160;"�̶��, ref�� "160"�� �� ���̴�.
        # ���� ���� ������ �籸���Ѵ�.
        self.pieces.append("&#%(ref)s;" % locals())

    def handle_entityref(self, ref):       
        # ��ü �������� ȣ���. ���� ��� "&copy;"�̶��, ref�� "copy"�� �� ���̴�.
        # ���� ��ü ������ �籸���Ѵ�.
        self.pieces.append("&%(ref)s" % locals())
        # ǥ�� HTML ��ü�� �ֹ������� ������; �ٸ� ��ü���� �׷��� �ʴ�.
        if htmlentitydefs.entitydefs.has_key(ref):
            self.pieces.append(";")

    def handle_data(self, text):           
        # ����� �ؽ�Ʈ ��ϸ��� ȣ���. �ٽ� ����, �±��� �ٱ��� ������, 
        # ���� ������ ��ü ������ ���Ե��� �ʴ´�.
        # ���� �ؽ�Ʈ�� �׳� �״�� �����Ѵ�.
        self.pieces.append(text)

    def handle_comment(self, text):        
        # HTML �ּ����� ȣ���. ��, <!-- insert Javascript code here -->
        # ���� �ּ��� �籸���Ѵ�.
        # �ҽ� �������� �ּ��� (�ڹٽ�ũ��Ʈ ����) Ŭ���̾�Ʈ-�� �ڵ尡 ��� �־, 
        # �� ó���⸦ �״�� �����Ű���� Ư�� �߿��ϴ�;
        # �ڼ��� ���� unknown_starttag�� �ִ� �ּ��� �����϶�.
        self.pieces.append("<!--%(text)s-->" % locals())

    def handle_pi(self, text):             
        # ó�� ���þ�� ȣ���. ��, <?instruction>
        # ���� ó�� ���þ �籸���Ѵ�.
        self.pieces.append("<?%(text)s>" % locals())

    def handle_decl(self, text):
        # �����Ѵٸ�, DOCTYPE�� ���Ͽ� ȣ���. ��,
        # <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        #     "http://www.w3.org/TR/html4/loose.dtd">
        # ���� DOCTYPE�� �籸���Ѵ�
        self.pieces.append("<!%(text)s>" % locals())

    def output(self):              
        """ó���� HTML�� ���ڿ� �ϳ��� �����ش�"""
        return "".join(self.pieces)