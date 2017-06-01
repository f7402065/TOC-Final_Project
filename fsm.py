# -- coding: UTF-8 --
from transitions.extensions import GraphMachine

global user_name ;

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

#state3
    def is_going_from_state0_to_state3(self, update):
        print('Leaving state0 to state3')
        text = update.message.text
        return text.lower() == 'hi' or text.lower() == 'hello'

    def on_enter_state3(self, update):
        update.message.reply_text("Hello")
        update.message.reply_text("請問您怎稱呼？")

#state4
    def is_going_from_state3_to_state4(self, update):
        print('Leaving state3 to state4')
        text = update.message.text
        global user_name
        user_name = text
        return text.lower() != ''

    def on_enter_state4(self, update):
        update.message.reply_text("Hello,"+user_name)
        update.message.reply_text("很高興為你服務\n請問你今天想要做什麼呢？\na.看電影 b.聽音樂")

#state5
    def is_going_from_state4_to_state5(self, update):
        print('Leaving state4 to state5')
        text = update.message.text
        return text.lower() == 'a' or text.lower() == 'a.'+ u'看電影' or text.lower() == 'a.' or text.lower() == u'看電影' or text.lower() == u'電影'

    def is_going_from_state9_to_state5(self, update):
        print('Leaving state9 to state5')
        text = update.message.text
        return text.lower() == u'想' or text.lower() == 'yes' or text.lower() == u'是' or text.lower() == u'是的' or text.lower() == u'對'

    def is_going_from_state11_to_state5(self, update):
        print('Leaving state11 to state5')
        text = update.message.text
        return text.lower() == u'想' or text.lower() == 'yes' or text.lower() == u'是' or text.lower() == u'是的' or text.lower() == u'對'

    def is_going_from_state12_to_state5(self, update):
        print('Leaving state12 to state5')
        text = update.message.text
        return text.lower() == u'想' or text.lower() == 'yes' or text.lower() == u'是' or text.lower() == u'是的' or text.lower() == u'對'

    def is_going_from_state13_to_state5(self, update):
        print('Leaving state13 to state5')
        text = update.message.text
        return text.lower() == u'想' or text.lower() == 'yes' or text.lower() == u'是' or text.lower() == u'是的' or text.lower() == u'對'

    def is_going_from_state14_to_state5(self, update):
        print('Leaving state14 to state5')
        text = update.message.text
        return text.lower() == u'想' or text.lower() == 'yes' or text.lower() == u'是' or text.lower() == u'是的' or text.lower() == u'對'

    def is_going_from_state15_to_state5(self, update):
        print('Leaving state15 to state5')
        text = update.message.text
        return text.lower() == u'想' or text.lower() == 'yes' or text.lower() == u'是' or text.lower() == u'是的' or text.lower() == u'對'

    def on_enter_state5(self, update):
        update.message.reply_text("請問你今天的心情如何？\na.開心 b.難過")

#state6
    def is_going_from_state5_to_state6(self, update):
        print('Leaving state5 to state6')
        text = update.message.text
        return text.lower() == 'a' or text.lower() == 'a.'+u'開心' or text.lower() == 'a.' or text.lower() == u'開心' or text.lower() == 'a' + u'開心'

    def on_enter_state6(self, update):
        update.message.reply_text("那我推薦你看\"大獨裁者落難記\"")
        update.message.reply_text("這裡有他的預告片:\nhttps://www.youtube.com/watch?v=flwsXZfHZSg")
        update.message.reply_text("請問你還想聽聽音樂嗎？")

#state7
    def is_going_from_state5_to_state7(self, update):
        print('Leaving state5 to state7')
        text = update.message.text
        return text.lower() != 'a' and text.lower() != 'a.'+u'開心' and text.lower() != 'a.' and text.lower() != u'開心' and text.lower() != 'a' + u'開心'

    def on_enter_state7(self, update):
        update.message.reply_text("那我推薦你看\"如果這世界消失了\"")
        update.message.reply_text("這裡有他的預告片:\nhttps://www.youtube.com/watch?v=O1179VuZLME")
        update.message.reply_text("請問你還會難過嗎？")

#state8
    def is_going_from_state4_to_state8(self, update):
        print('Leaving state4 to state8')
        text = update.message.text
        return text.lower() != 'a' and text.lower() != 'a.'+ u'看電影' and text.lower() != 'a.' and text.lower() != u'看電影' and text.lower() != u'電影'


    def is_going_from_state6_to_state8(self, update):
        print('Leaving state6 to state8')
        text = update.message.text
        return text.lower() == u'想' or text.lower() == 'yes' or text.lower() == u'是' or text.lower() == u'是的' or text.lower() == u'對'

    def is_going_from_state7_to_state8(self, update):
        print('Leaving state7 to state8')
        text = update.message.text
        return text.lower() == u'想' or text.lower() == 'yes' or text.lower() == u'是' or text.lower() == u'是的' or text.lower() == u'對'

    def on_enter_state8(self, update):
        update.message.reply_text("那你想聽什麼風格的音樂？\n情調、舒眠、電音、爵士、古典、流行之類的")

#state9
    def is_going_from_state8_to_state9(self, update):
        print('Leaving state8 to state9')
        text = update.message.text
        return text.lower() == u'情調'

    def on_enter_state9(self, update):
        update.message.reply_text("那我推薦你徐佳瑩的\"失落沙洲\"")
        update.message.reply_text("可以聽聽看：\nhttps://www.youtube.com/watch?v=Ie1KcGvBN_k")
        update.message.reply_text("那你想看看電影嗎？")

#state10
    def is_going_from_state9_to_state10(self, update):
        print('Leaving state9 to state10')
        text = update.message.text
        return text.lower() != u'想' and text.lower() != 'yes' and text.lower() != u'是' and text.lower() != u'是的' and text.lower() != u'對'

    def is_going_from_state6_to_state10(self, update):
        print('Leaving state6 to state10')
        text = update.message.text
        return text.lower() != u'想' and text.lower() != 'yes' and text.lower() != u'是' and text.lower() != u'是的' and text.lower() != u'對'

    def is_going_from_state7_to_state10(self, update):
        print('Leaving state7 to state10')
        text = update.message.text
        return text.lower() != u'想' and text.lower() != 'yes' and text.lower() != u'是' and text.lower() != u'是的' and text.lower() != u'對'

    def is_going_from_state11_to_state10(self, update):
        print('Leaving state11 to state10')
        text = update.message.text
        return text.lower() != u'想' and text.lower() != 'yes' and text.lower() != u'是' and text.lower() != u'是的' and text.lower() != u'對'

    def is_going_from_state12_to_state10(self, update):
        print('Leaving state12 to state10')
        text = update.message.text
        return text.lower() != u'想' and text.lower() != 'yes' and text.lower() != u'是' and text.lower() != u'是的' and text.lower() != u'對'

    def is_going_from_state13_to_state10(self, update):
        print('Leaving state13 to state10')
        text = update.message.text
        return text.lower() != u'想' and text.lower() != 'yes' and text.lower() != u'是' and text.lower() != u'是的' and text.lower() != u'對'

    def is_going_from_state14_to_state10(self, update):
        print('Leaving state14 to state10')
        text = update.message.text
        return text.lower() != u'想' and text.lower() != 'yes' and text.lower() != u'是' and text.lower() != u'是的' and text.lower() != u'對'

    def is_going_from_state15_to_state10(self, update):
        print('Leaving state15 to state10')
        text = update.message.text
        return text.lower() != u'想' and text.lower() != 'yes' and text.lower() != u'是' and text.lower() != u'是的' and text.lower() != u'對'

    def on_enter_state10(self, update):
        update.message.reply_text("那感謝您的使用，歡迎再次使用！")
        self.go_back(update)

#state11
    def is_going_from_state8_to_state11(self, update):
        print('Leaving state8 to state11')
        text = update.message.text
        return text.lower() == u'舒眠'

    def on_enter_state11(self, update):
        update.message.reply_text("那我推薦你吉他版的\"Faded\"")
        update.message.reply_text("可以聽聽看：\nhttps://www.youtube.com/watch?v=44FPny8k4DM")
        update.message.reply_text("那你想看看電影嗎？")

#state12
    def is_going_from_state8_to_state12(self, update):
        print('Leaving state8 to state12')
        text = update.message.text
        return text.lower() == u'電音'

    def on_enter_state12(self, update):
        update.message.reply_text("那我推薦你Redfoo的\"Juicy Wiggle\"")
        update.message.reply_text("可以聽聽看：\nhttps://www.youtube.com/watch?v=tWyuglGCKgE")
        update.message.reply_text("那你想看看電影嗎？")

#state13
    def is_going_from_state8_to_state13(self, update):
        print('Leaving state8 to state13')
        text = update.message.text
        return text.lower() == u'爵士'

    def on_enter_state13(self, update):
        update.message.reply_text("那我推薦你Melody Gardot的La Vie en Rose\"玫瑰人生\"")
        update.message.reply_text("可以聽聽看：\nhttps://www.youtube.com/watch?v=Elc0oThyV3Q")
        update.message.reply_text("那你想看看電影嗎？")

#state14
    def is_going_from_state8_to_state14(self, update):
        print('Leaving state8 to state14')
        text = update.message.text
        return text.lower() == u'古典'

    def on_enter_state14(self, update):
        update.message.reply_text("那我推薦你帕海貝爾的\"卡農\"")
        update.message.reply_text("可以聽聽看：\nhttps://www.youtube.com/watch?v=LUkmXps_s70")
        update.message.reply_text("那你想看看電影嗎？")

#state15
    def is_going_from_state8_to_state14(self, update):
        print('Leaving state8 to state14')
        text = update.message.text
        return text.lower() != u'古典' and text.lower() != u'爵士' and text.lower() != u'古典' and text.lower() != u'電音' and text.lower() != u'舒眠' and text.lower() != u'情調'

    def on_enter_state14(self, update):
        update.message.reply_text("那我推薦你隨性樂團的\"想你點煙\"")
        update.message.reply_text("可以聽聽看：\nhttps://www.youtube.com/watch?v=m60hjpNtq5k")
        update.message.reply_text("那你想看看電影嗎？")














