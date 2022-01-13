import numpy as np 
from preprocessing import make_preprocessing_pipline 
from sklearn.metrics.pairwise import cosine_similarity 
from sklearn.externals import joblib 
from .helper import resource_path 
from database_interface import load_responce 
next_utrance_types = {'r': 'first responce', 'rr': 'second responce', 'q': 'queery'} 
yes_responces = ['نعم ', 'اجل ', 'بلى ', 'فعلا ', 'هى ', 'هو '] 
no_responces = ['لم ', 'لن ', 'لا', 'ما ', 'ليس ', 'ليست '] 
candidiates_turns = {4: (2, 2), 3: (1, 2), 2: (2, 0), 1:(1, 0)} 
classes = {0: ' العدوى من الحيوانات ',
           1: ' العدوى من أشخاصبدون أعراض ',
           2: ' إنهاء المحادثة ',
           3: ' عمر الفيروس ',
           4: ' شحن البضائع من و الى مناطق الوباء ',
           5: ' استخدام الكمامة ',
           6: ' فترة الحضانة ',
           7: ' استععمال المعقمات ',
           8: ' الإصابة أكثر من مرة بالمرض ',
           9: 'الوقاية ',
           10:' بدء المحادثة ',
           11: ' أعراضالمرض ',
           12: ' تأثير العوامل المناخية على الفيروس ',
           13: ' فحصوجود الفيروس ',
           14: ' طرق انتقال الوباء '} 
utrance_vectors = joblib.load(resource_path('utrances_vectors\\utrances_vectors.pkl')) 
utrance_vectorizer = joblib.load(resource_path('utrance_vectorizer\\utrance_vectorizer.pkl')) 
SIM_THRISH = 0.8 
special_classes_indices = [2, 10]
ERROR_MSG = ' لم أستطع فهمك !!.. إن كان ما تسأل عنه متعلقا بفيروس كورونا الرجاء أعد كتابته بصيغة مختلفة ' 
OR = ' أم ' 
CLARIFICATION = ' هل تريد ' 
HELLO_MSG = ' مرحبا اسمي لينه .. روبوت دردشة آلية صنع بجامعة السودان للعلوم والتكنولوجيا للإجابة عن اسئلة كورونا الشائعة ' 
BYE_MSG = ' شكرا لتواصك ' 
INFORMATION = ' معلومات عن ' 
class Conversation: 
    def __init__(self): 
        
        self.next_user_utrance_type = next_utrance_types['q'] 
        self.candidates = None 
        self.user_utrance = None 
        self.chatbot_utrance = None 
        self.turn1 = None 
        self.turn2 = None 
        self.returnd_classes = None 
        self.found = False 
    def set_candidates(self, indices): 
        indices.reverse() 
        self.candidates = indices 
    def set_user_utrance(self, utrance): 
        self.user_utrance = utrance 
    def __check_special(self): 
        if self.candidates[-1] in special_classes_indices: 
            return True, self.candidates[-1] 
        else: 
            return False, False 
    def __get_similar(self, utrance, vectors, vectorizer): 
        utrance_vector = vectorizer.transform(utrance) 
        similarties = cosine_similarity(utrance_vector, vectors[self.returnd_classes]) 
        return self.returnd_classes[np.argmax(similarties)], similarties[np.argmax(similarties)] 
    def __identify_class(self):
        if self.next_user_utrance_type == next_utrance_types['q']:
            print('q') 
            is_special, clas = self.__check_special() 
            if is_special: 
                return [clas] 
            self.turn1, self.turn2 = candidiates_turns[len(self.candidates)] 
            self.returnd_classes = [] 
            for i in range(self.turn1): 
                self.returnd_classes.append(self.candidates.pop()) 
                self.next_user_utrance_type = next_utrance_types['r'] 
                return self.returnd_classes 
        elif self.next_user_utrance_type == next_utrance_types['r']: 
            print('r') 
            if self.turn1 == 1:
                for r in yes_responces: 
                    if r in self.user_utrance.split(): 
                        self.found = True 
                        self.next_user_utrance_type = next_utrance_types['q'] 
                        return self.returnd_classes 
                for r in no_responces: 
                    if r in self.user_utrance.split(): 
                        if self.turn2 > 0: 
                            self.returnd_classes = [] 
                            for i in range(self.turn2): 
                                self.returnd_classes.append(self.candidates.pop()) 
                                self.next_user_utrance_type = next_utrance_types['rr'] 
                                return self.returnd_classes 
                        else: 
                            self.turn1, self.turn2 = candidiates_turns[len(self.candidates)] 
                            self.returnd_classes = [] 
                            for i in range(self.turn1): 
                                self.returnd_classes.append(self.candidates.pop()) 
                            self.next_user_utrance_type = next_utrance_types['r'] 
                            return self.returnd_classes 
            else: 
                for r in no_responces: 
                    if r in self.user_utrance.split(): 
                        if self.turn2 > 0: 
                            self.returnd_classes = [] 
                            for i in range(self.turn2): 
                                self.returnd_classes.append(self.candidates.pop())
                                self.next_user_utrance_type = user_utrance_types['rr'] 
                                return self.returnd_classes
                        else: 
                            self.next_user_utrance_type = user_utrance_types['q'] 
                            return [-1]
                    utrance, sim = self.__get_similar(self.user_utrance, utrance_vectors, utrance_vectorizer) 
                    if sim >= SIM_THRISH:
                        self.found = True 
                        return [utrance]
                    else: 
                        self.turn1, self.turn2 = candidiates_turns[len(self.candidates)] 
                        self.returnd_classes = [] 
                        for i in range(self.turn1): 
                            self.returnd_classes.append(self.candidates.pop()) 
                        self.next_user_utrance_type = user_utrance_types['r'] 
                        return self.returnd_classes
        elif self.next_user_utrance_type == user_utrance_types['rr']: 
            print('rr') 
            for r in no_responces: 
                if r in self.user_utrance.split(): 
                    self.next_user_utrance_type = user_utrance_types['q'] 
                    return [-1] 
                utrance, sim = self.__get_similar(self.user_utrance, utrance_vectors, utrance_vectorizer) 
                if sim >= SIM_THRISH: 
                    self.found = True 
                    return [utrance]
                else: 
                    self.turn1, self.turn2 = candidiates_turns[len(self.candidates)] 
                    self.returnd_classes = [] 
                    for i in range(self.turn1): 
                        self.returnd_classes.append(self.candidates.pop()) 
                    self.next_user_utrance_type = user_utrance_types['r'] 
                    return self.returnd_classes
    def generate_responce(self): 
        clas = self.__identify_class() 
        if len(clas) == 1: 
            if clas[0] == -1:
                return ERROR_MSG, self.next_user_utrance_type 
            elif clas[0] == 2: 
                return BYE_MSG, self.next_user_utrance_type 
            elif clas[0] == 10: 
                return HELLO_MSG, self.next_user_utrance_type 
            elif clas[0] in list(range(15)) and self.found == True: 
                self.found = False 
                return load_responce(clas[0]), self.next_user_utrance_type
            else: 
                return CLARIFICATION + INFORMATION + classes[clas[0]], self.next_user_utrance_type 
        else: return CLARIFICATION + INFORMATION + classes[clas[0]] + OR + INFORMATION + classes[clas[1]], self.next_user_utrance_type 
if __name__ == '__main__': pass
