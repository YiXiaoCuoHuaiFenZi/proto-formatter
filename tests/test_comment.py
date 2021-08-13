from proto_formatter.comment import CommentParser

s1 = """

   /*
   The price availability API request message
   
   
    // aaaaaaaaaaaaaa
   */
   // asdasdasd
   /*
The price availability API request messageadssd
*/
   // asdasdasd //asdsad

   // y API request messageadssd
"""
s2 = """


   /*
   The price availability API request message
    // aaaaaaaaaaaaaa
   */
   // asdasdasd
   /*
   
   
   
   
The price availability API request messageadssd
*/
   // asdasdasd //asdsad
message A{
   // y API request messageadssd
   
   message A{

"""

s3 = """
   /*
   asdddddddd
   price availability API request message
    */
   // sdfghjk
    syntax = "proto3";//The price availability API request message //asd /*asdfghj*/阿斯蒂芬
"""


def test_comment_pick_up_1():
    lines = s1.split('\n')
    c = CommentParser()
    comment_lines = c.pick_up_comment(lines)

    assert len(comment_lines) == 12


def test_comment_pick_up_2():
    lines = s2.split('\n')
    c = CommentParser()
    comment_lines = c.pick_up_comment(lines)

    assert len(comment_lines) == 13


def test_comment_pick_up_3():
    lines = s3.split('\n')
    c = CommentParser()
    comment_lines = c.pick_up_comment(lines)

    assert len(comment_lines) == 5
